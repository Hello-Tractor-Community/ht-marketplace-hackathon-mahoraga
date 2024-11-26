# Generated by Django 5.1.3 on 2024-11-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_dealer_address_dealer_addresses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='addresses',
        ),
        migrations.AddField(
            model_name='dealer',
            name='address',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dealer',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]