# Generated by Django 3.2.6 on 2022-08-25 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mun_app', '0015_explore_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='picture',
            new_name='media',
        ),
    ]
