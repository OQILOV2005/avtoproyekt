# Generated by Django 4.2.3 on 2023-08-16 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_servis_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='img',
        ),
    ]