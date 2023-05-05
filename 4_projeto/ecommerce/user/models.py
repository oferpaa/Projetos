from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re
from utils.validacpf import valida_cpf
from utils.validaemail import valida_email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name='Usuário')
    name = models.CharField(max_length=250, null=True, verbose_name='Nome')
    email = models.CharField(max_length=200)
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=11, verbose_name='CPF')

    def __str__(self):
        return f'{self.user}'

    def clean(self):
        error_messages = {}

        cpf_enviado = self.cpf or None
        cpf_salvo = None
        profile = Profile.objects.filter(cpf=cpf_enviado).first()

        email_enviado = self.email or None
        email_salvo = None
        email = Profile.objects.filter(email=email_enviado).first()

        if email:
            email_salvo = email.email

            if email_salvo is not None and self.pk != email.pk:
                error_messages['email'] = 'Email já cadastrado.'

        if not valida_email:
            error_messages['email'] = 'Email inválido.'

        if profile:
            cpf_salvo = profile.cpf

            if cpf_salvo is not None and self.pk != profile.pk:
                error_messages['cpf'] = 'CPF já cadastrado.'

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, verbose_name='Usuário')
    address = models.CharField(
        max_length=50, null=False, verbose_name='Endereço')
    number = models.CharField(max_length=5, null=False, verbose_name='Número')
    address_complement = models.CharField(
        max_length=30, verbose_name='Complemento')
    district = models.CharField(
        max_length=30, null=False, verbose_name='Bairro')
    zipcode = models.CharField(max_length=8, null=False, verbose_name='CEP')
    city = models.CharField(max_length=30, null=False, verbose_name='Cidade')
    state = models.CharField(
        verbose_name='Estado',
        max_length=2,
        default='',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    def clean(self):
        error_messages = {}

        if re.search(r'[^0-9]', self.zipcode) or len(self.zipcode) < 8:
            error_messages['zipcode'] = 'CEP inválido.'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
