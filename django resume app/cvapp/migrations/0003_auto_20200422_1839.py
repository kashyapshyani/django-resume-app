# Generated by Django 2.2.4 on 2020-04-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_auto_20170727_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.CharField(max_length=6),
        ),
    ]
