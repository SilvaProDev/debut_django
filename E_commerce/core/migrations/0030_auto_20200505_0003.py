# Generated by Django 3.0.5 on 2020-05-05 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20200505_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('', 'null'), ('P', 'primary'), ('S', 'secondary'), ('D', 'danger'), ('W', 'warning')], max_length=1),
        ),
    ]