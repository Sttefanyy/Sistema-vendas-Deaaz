from datetime import datetime
from apps.service.models import OPC_SERVICES, Venda, Anexo
from apps.service.widgets import MultipleFileField
from django import forms
from django.db.models import Q

from apps.worker.models import Funcionario



class VendaForm(forms.ModelForm):
    arquivos = MultipleFileField(
        required=False,
        label="Anexos",
        help_text="Selecione um ou mais arquivos para anexar."
    )
    Agencia_recomendada = forms.CharField(
        required=False,
        label="Agência Recomendada",
        help_text="Digite o nome da agência que recomendou."
    )
    recomendação_da_Venda = forms.CharField(
        required=False,
        label="Recomendação da Venda",
        help_text="Digite o nome da pessoa que recomendou."
    )
    custo_padrao_venda = forms.FloatField(
        required=False,
        help_text="Valor bruto da venda.",
        label="Custo padrão venda",
        widget=forms.TextInput(attrs={"placeholder": "Digite o Valor padrão da venda."})
    )
    desconto = forms.FloatField(
        required=False,
        label="Desconto",
        widget=forms.TextInput(attrs={"placeholder": "Digite o desconto, será considerada em porcentagem (%)."})
    )
    custo_sobre_venda = forms.FloatField(
        required=False,
        label="Custo sobre Venda",
        widget=forms.TextInput(attrs={"placeholder": "Digite o custo sobre a venda decorrido da agencia ou afins."})
    )

    class Meta:
        model = Venda
        fields = [
            "vendedor", "situacaoMensal", "custo_padrao_venda", "desconto", "custo_sobre_venda",
            "tipo_pagamento", "Agencia_recomendada", "recomendação_da_Venda", "arquivos"
        ]

    def clean(self):
        cleaned_data = super().clean()
        agencia = cleaned_data.get("Agencia_recomendada")
        recomendacao = cleaned_data.get("recomendação_da_Venda")
        tipo_servico = self.data.get("tipo_servico")  # Pegando o valor do POST

        # Verifica se algum dos critérios está presente
        tem_agencia_ou_recomendacao = bool(agencia or recomendacao)
        tipo_servico_valido = tipo_servico and tipo_servico.strip() in [item.strip() for item in OPC_SERVICES]
        
        if tem_agencia_ou_recomendacao or tipo_servico_valido:
            self.instance.status_executivo = True
        else:
            self.instance.status_executivo = False

        return cleaned_data

    def save(self, commit=True):
        venda = super().save(commit=commit)
        arquivos = self.files.getlist("arquivos")
        for arquivo in arquivos:
            if not Anexo.objects.filter(venda=venda, arquivo=arquivo.name).exists():
                Anexo.objects.create(arquivo=arquivo, venda=venda)
        return venda
    
    
class VendaAtualizar(forms.ModelForm):
    arquivos = MultipleFileField(
        required=False,
        label="Anexos",
        help_text="Selecione um ou mais arquivos para anexar."
    )
    Agencia_recomendada = forms.CharField(
        required=False,
        label="Agencia Recomendada",
        help_text="Digite o nome da agência que recomendou."
    )

    recomendação_da_Venda = forms.CharField(
        required=False,
        label="Recomendação da Venda",
        help_text="Digite o nome da pessoa que recomendou."
    )
    custo_padrao_venda = forms.FloatField(
        required=False,
        label="Custo da venda",
        help_text="Valor bruto da venda.",
        widget=forms.TextInput(attrs={"placeholder": "Digite o Valor padrão da venda."})
    )

    valor = forms.FloatField(
        required=False,
        label="Valor",
        help_text="Valor liquido da venda.",
        widget=forms.TextInput(attrs={"placeholder": "Digite o Valor padrão da venda."})
        
    )
    data_venda = forms.CharField(
        required=False,
        label="Data da Venda",
    widget=forms.TextInput(attrs={"placeholder": "Preencha apenas com números, a formatação será automática"})
    )
    finished_at = forms.CharField(
        required=False,
        label="Data Finalizado",
    widget=forms.TextInput(attrs={"placeholder": "Preencha apenas com números, a formatação será automática"})
    )
    desconto = forms.FloatField(
    required=False,
    label="Desconto",
    widget=forms.TextInput(attrs={"placeholder": "Digite o desconto, será considerada em porcentagem (%)."}),
    )
    custo_sobre_venda = forms.FloatField(
    required=False,
    label="Custo sobre Venda",
    widget=forms.TextInput(attrs={"placeholder": "Digite o custo sobre a venda decorrido da agencia ou afins."}),
    )
    class Meta:
        model = Venda
        fields = [
            "vendedor", "executivo", "situacaoMensal", "data_venda", "finished_at", "custo_padrao_venda", "valor", "desconto", "custo_sobre_venda", "tipo_pagamento", "Agencia_recomendada", "recomendação_da_Venda", "arquivos"
        ]
    def clean(self):
            cleaned_data = super().clean()
            agencia      = cleaned_data.get("Agencia_recomendada")
            recomendacao = cleaned_data.get("recomendação_da_Venda")
            tipo_servico = (self.data.get("tipo_servico") or "").strip()

            # MESMA lógica unificada
            if agencia or recomendacao or tipo_servico in [s.strip() for s in OPC_SERVICES]:
                self.instance.status_executivo = True
            else:
                self.instance.status_executivo = False
                # zera o campo executivo no form, para desabilitar no template
                cleaned_data["executivo"] = None

            return cleaned_data

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # controla queryset de 'executivo' conforme o status_executivo
            if not self.instance.status_executivo:
                self.fields['executivo'].queryset = Funcionario.objects.none()
            else:
                self.fields['executivo'].queryset = Funcionario.objects.filter(departamento='Exec')

            # vendedores sempre disponíveis
            self.fields['vendedor'].queryset = Funcionario.objects.filter(
                Q(departamento='Vend') | Q(departamento='Adm')
            )


    def save(self, commit=True):
     venda = super().save(commit=commit)

 # Atualizar arquivos anexados
     arquivos = self.files.getlist('arquivos')
     for arquivo in arquivos:
         if not Anexo.objects.filter(venda=venda, arquivo=arquivo.name).exists():
            Anexo.objects.create(arquivo=arquivo, venda=venda)
     return venda
   
   