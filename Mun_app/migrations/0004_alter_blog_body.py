# Generated by Django 3.2.6 on 2022-08-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mun_app', '0003_auto_20220820_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
        ),
    ]