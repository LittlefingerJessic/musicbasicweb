# Generated by Django 3.1.3 on 2020-11-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musictable',
            name='lrc',
            field=models.CharField(max_length=2048),
        ),
    ]