# Generated by Django 5.0.2 on 2024-11-25 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0016_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]