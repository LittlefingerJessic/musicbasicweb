# Generated by Django 3.1.3 on 2020-11-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20201130_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musictable',
            name='lrc',
            field=models.TextField(max_length=2048),
        ),
    ]
