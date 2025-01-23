from django.db import models


# INFO: Dados das agencias
class Agencia(models.Model):
    id = models.AutoField(primary_key=True)
    nome_contato = models.CharField(max_length=101, verbose_name="nome do contato")
    nome_fantasia = models.CharField(max_length=200, verbose_name="nome fantasia da agência")
    email = models.EmailField(unique=True, verbose_name="e-mail", max_length=255)
    
    telefone1 = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="telefone 1",
    )
    telefone2 = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="telefone 2",
    )
    telefone3 = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="telefone 3",
    )
    
    contato_ano = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="ano de contato",
        help_text="Formato: DD/MM/YYYY"
    )
    
    cnpj = models.CharField(
        max_length=18,
        unique=True,
        null=False,
        verbose_name="CNPJ",
    )
    cep = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="CEP",
        help_text="Formato: XXXXX-XXX"
    )
    municipio = models.CharField(max_length=100, verbose_name="município")
    uf = models.CharField(max_length=2, verbose_name="UF")
    logradouro = models.CharField(max_length=255, verbose_name="Logradouro", help_text="Rua | Avenida | Alameda | Travessa")
    numero = models.CharField(max_length=10, verbose_name="número")
    complemento = models.CharField(max_length=255, null=True, blank=True, verbose_name="complemento")
    bairro = models.CharField(max_length=100, verbose_name="bairro")
