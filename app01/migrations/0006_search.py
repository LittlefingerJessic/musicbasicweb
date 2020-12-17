# Generated by Django 3.1.3 on 2020-12-01 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_music_mp3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=256)),
                ('singer', models.CharField(max_length=256)),
                ('mp3', models.CharField(max_length=256)),
                ('lrc', models.TextField()),
            ],
        ),
    ]
