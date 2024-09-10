# Generated by Django 4.2.16 on 2024-09-10 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tgusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RBPaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=255, verbose_name='Номер счета')),
                ('field1', models.CharField(max_length=255, verbose_name='поле 1')),
                ('field2', models.CharField(max_length=255, verbose_name='поле 2')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=255, verbose_name='Номер чека')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Количество')),
                ('is_paid', models.BooleanField(default=False, verbose_name='оплата заказа')),
                ('type', models.CharField(choices=[('EU', 'EU'), ('RB', 'RB')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgusers.telegramuser', verbose_name='Пользователь')),
            ],
        ),
    ]
