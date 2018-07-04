# Generated by Django 2.0.6 on 2018-07-04 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinfo', '0005_auto_20180703_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.CharField(blank=True, max_length=100)),
                ('lked', models.CharField(blank=True, max_length=100)),
                ('matching', models.CharField(blank=True, max_length=100)),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
        ),
    ]
