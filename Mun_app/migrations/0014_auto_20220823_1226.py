# Generated by Django 3.2.6 on 2022-08-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mun_app', '0013_alter_tvseries_ventspace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Explore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Choose', models.CharField(choices=[('Feedback', 'Feedback'), ('Question', 'Question')], max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogRelated',
        ),
    ]