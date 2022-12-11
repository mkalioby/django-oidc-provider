# Generated by Django 4.1.4 on 2022-12-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0027_code_acr_values_alter_client_id_alter_code_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='_acr_values',
            field=models.TextField(default=None, verbose_name='ACR'),
        ),
        migrations.AddField(
            model_name='token',
            name='_acr_values',
            field=models.TextField(default=None, verbose_name='ACR'),
        ),
        migrations.AddField(
            model_name='userconsent',
            name='_acr_values',
            field=models.TextField(default=None, verbose_name='ACR'),
        ),
    ]
