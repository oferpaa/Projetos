# Generated by Django 4.2.1 on 2023-05-03 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True, verbose_name='Data do Pedido')),
                ('transaction_id', models.CharField(max_length=100, null=True, verbose_name='ID da Transação')),
                ('quantity', models.PositiveIntegerField()),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('C', 'Criado'), ('A', 'Aprovado'), ('R', 'Reprovado'), ('P', 'Pendente'), ('E', 'Enviado'), ('F', 'Finalizado')], default='C', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('product_id', models.PositiveIntegerField()),
                ('varitation', models.CharField(max_length=255)),
                ('variation_id', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.CharField(max_length=2000)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'verbose_name': 'Item do Pedido',
                'verbose_name_plural': 'Itens do Pedido',
            },
        ),
    ]
