# Generated by Django 3.1.7 on 2021-05-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.IntegerField(default=0),
        ),
    ]
