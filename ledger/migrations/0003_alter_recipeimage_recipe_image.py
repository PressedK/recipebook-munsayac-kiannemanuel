# Generated by Django 5.1.6 on 2025-04-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_recipeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeimage',
            name='recipe_image',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]
