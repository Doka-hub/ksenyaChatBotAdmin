# Generated by Django 4.2.16 on 2024-09-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображние')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Видео')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, verbose_name='ТГ юзер айди')),
                ('username', models.CharField(max_length=30, verbose_name='Ник пользователя')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Фамилия пользователя')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('is_blocked', models.BooleanField(verbose_name='Заблокировал Бота')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('role', models.CharField(choices=[('CLIENT', 'Клиент'), ('MANAGER', 'Менеджер')], max_length=20, verbose_name='Роль')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tguser',
            },
        ),
    ]
