# Generated by Django 4.2.5 on 2023-10-03 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_alter_férias_dias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='férias',
            old_name='data',
            new_name='data_in',
        ),
    ]
