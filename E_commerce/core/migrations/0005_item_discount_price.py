# Generated by Django 3.0.5 on 2020-04-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]