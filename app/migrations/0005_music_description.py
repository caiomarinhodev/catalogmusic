# Generated by Django 3.1.7 on 2021-10-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211008_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
