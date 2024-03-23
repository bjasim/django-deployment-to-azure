# Generated by Django 5.0.2 on 2024-02-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseServer', '0006_computespecifications_provider_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkingspecifications',
            old_name='bandwidth',
            new_name='sku',
        ),
        migrations.RenameField(
            model_name='networkingspecifications',
            old_name='technology',
            new_name='unit_of_measure',
        ),
        migrations.AddField(
            model_name='networkingspecifications',
            name='unit_price',
            field=models.CharField(default='0.0', max_length=50),
        ),
    ]
