# Generated by Django 3.1.7 on 2021-10-08 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('chords', models.TextField(blank=True, null=True)),
                ('cifraclub_chords_url', models.URLField(blank=True, null=True)),
                ('tone', models.CharField(blank=True, max_length=255, null=True)),
                ('bpm', models.CharField(blank=True, max_length=255, null=True)),
                ('bar_lenght', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_id', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.artist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
