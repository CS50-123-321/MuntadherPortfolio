# Generated by Django 3.2.6 on 2022-08-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mun_app', '0008_auto_20220821_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmanagementsystem',
            name='Body',
            field=models.TextField(null=True),
        ),
    ]