# Generated by Django 3.0.5 on 2020-04-30 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200429_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]