# Generated by Django 5.1.5 on 2025-03-29 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        blank=True, max_length=101, null=True, verbose_name="nome"
                    ),
                ),
                (
                    "telefone1",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="telefone 1"
                    ),
                ),
                (
                    "telefone2",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="telefone 2"
                    ),
                ),
                (
                    "celular",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="telefone 3"
                    ),
                ),
                (
                    "email1",
                    models.EmailField(
                        blank=True, max_length=255, null=True, verbose_name="e-mail 1"
                    ),
                ),
                (
                    "email2",
                    models.EmailField(
                        blank=True, max_length=255, null=True, verbose_name="e-mail 2"
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "sexo_outros",
                    models.CharField(
                        blank=True,
                        help_text="Digite o sexo aqui.",
                        max_length=5000,
                        null=True,
                        verbose_name="Tipo sexo",
                    ),
                ),
                (
                    "data_nascimento",
                    models.CharField(
                        blank=True,
                        help_text="Digite no formato dd/mm/aaaa",
                        max_length=15,
                        null=True,
                        verbose_name="Data de nascimento",
                    ),
                ),
                ("idade", models.IntegerField(editable=False, null=True)),
                (
                    "endereco",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="endereço"
                    ),
                ),
                (
                    "cidade",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="cidade"
                    ),
                ),
                (
                    "bairro",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="bairro"
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Estado"
                    ),
                ),
                (
                    "cep",
                    models.CharField(
                        blank=True, max_length=14, null=True, verbose_name="CEP"
                    ),
                ),
                (
                    "rg",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="RG"
                    ),
                ),
                (
                    "cpf",
                    models.CharField(max_length=14, unique=True, verbose_name="CPF"),
                ),
                (
                    "num_passaporte",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="número de passaporte",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "anexo1",
                    models.FileField(
                        blank=True,
                        help_text="Envie um arquivo relacionado ao Cliente.",
                        null=True,
                        upload_to="anexos/",
                        verbose_name="Anexo",
                    ),
                ),
                (
                    "anexo2",
                    models.FileField(
                        blank=True,
                        help_text="Envie um arquivo relacionado ao Cliente.",
                        null=True,
                        upload_to="anexos/",
                        verbose_name="Anexo",
                    ),
                ),
                (
                    "anexo3",
                    models.FileField(
                        blank=True,
                        help_text="Envie um arquivo relacionado ao Cliente.",
                        null=True,
                        upload_to="anexos/",
                        verbose_name="Anexo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Anexo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("arquivo", models.FileField(upload_to="anexos/")),
                ("data_upload", models.DateTimeField(auto_now_add=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="anexos",
                        to="client.cliente",
                    ),
                ),
            ],
        ),
    ]
