# Generated by Django 3.2.6 on 2021-09-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
