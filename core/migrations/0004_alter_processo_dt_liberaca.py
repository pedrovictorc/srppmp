# Generated by Django 4.0 on 2022-01-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_processo_n_liberacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='dt_liberaca',
            field=models.DateField(verbose_name='Data da Liberação'),
        ),
    ]