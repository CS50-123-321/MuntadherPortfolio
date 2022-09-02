# Generated by Django 3.2.6 on 2022-08-20 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mun_app', '0005_alter_experience_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogRelated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Comment', models.TextField()),
                ('BlogName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mun_app.blog')),
            ],
        ),
    ]