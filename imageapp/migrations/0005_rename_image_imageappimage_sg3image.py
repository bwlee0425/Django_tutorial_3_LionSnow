# Generated by Django 5.1.3 on 2025-01-15 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0004_rename_image_imageappimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageappimage',
            old_name='image',
            new_name='sg3image',
        ),
    ]
