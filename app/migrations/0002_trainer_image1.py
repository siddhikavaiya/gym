# Generated by Django 3.0.3 on 2021-04-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='image1',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
