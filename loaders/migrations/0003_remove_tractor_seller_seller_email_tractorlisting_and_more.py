# Generated by Django 5.0.2 on 2024-11-21 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0002_monthlysalesrecord_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tractor',
            name='seller',
        ),
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.EmailField(default='johndoe@gmail.com', max_length=254),
        ),
        migrations.CreateModel(
            name='TractorListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('hours_used', models.IntegerField()),
                ('description', models.TextField()),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=50)),
                ('additional_features', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('views', models.IntegerField(default=0)),
                ('inquiries', models.IntegerField(default=0)),
                ('sales', models.IntegerField(default=0)),
                ('status', models.CharField(default='Active', max_length=50)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tractors', to='loaders.seller')),
            ],
        ),
        migrations.DeleteModel(
            name='MonthlySalesRecord',
        ),
        migrations.DeleteModel(
            name='Tractor',
        ),
    ]
