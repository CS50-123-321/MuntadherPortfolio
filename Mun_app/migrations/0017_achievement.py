# Generated by Django 3.2.6 on 2022-08-25 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mun_app', '0016_rename_picture_experience_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('experience_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Mun_app.experience')),
            ],
            bases=('Mun_app.experience',),
        ),
    ]
