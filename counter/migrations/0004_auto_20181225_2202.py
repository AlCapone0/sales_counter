# Generated by Django 2.1.4 on 2018-12-25 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_auto_20181225_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companies',
            options={'verbose_name': 'Компанию', 'verbose_name_plural': 'Компании'},
        ),
    ]