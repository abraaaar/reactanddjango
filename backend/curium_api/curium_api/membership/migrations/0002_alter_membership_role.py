# Generated by Django 5.0.1 on 2024-04-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('NORMALUSER', 'Normal User'), ('RADIOLOGIST', 'Radiologist'), ('SURGEON', 'Surgeon'), ('TELERADIOLOGIST', 'Teleradiologist')], max_length=20),
        ),
    ]
