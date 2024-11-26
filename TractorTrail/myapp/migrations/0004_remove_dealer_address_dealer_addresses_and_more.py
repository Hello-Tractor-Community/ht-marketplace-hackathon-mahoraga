# Generated by Django 5.1.3 on 2024-11-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_dealer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='address',
        ),
        migrations.AddField(
            model_name='dealer',
            name='addresses',
            field=models.TextField(blank=True, help_text='Enter multiple addresses separated by commas', null=True),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]