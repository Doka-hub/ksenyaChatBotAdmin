# Generated by Django 5.1.1 on 2024-09-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_payment_amount_alter_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='оплата заказа'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='stripe_id',
            field=models.CharField(max_length=255, verbose_name='Номер чека'),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='value',
            field=models.CharField(max_length=100, verbose_name='Значение'),
        ),
    ]
