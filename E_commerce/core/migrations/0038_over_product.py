# Generated by Django 3.0.5 on 2020-05-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_slide_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Over_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='images/')),
                ('label', models.CharField(blank=True, choices=[('p', 'primary'), ('d', 'danger'), ('w', 'warning'), ('b', 'blue')], max_length=30, null=True)),
            ],
        ),
    ]