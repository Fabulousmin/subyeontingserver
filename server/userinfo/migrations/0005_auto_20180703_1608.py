# Generated by Django 2.0.6 on 2018-07-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_auto_20180703_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.TextField(),
        ),
    ]
