# Generated by Django 5.1.3 on 2024-11-22 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=20)),
                ('menu_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=20)),
                ('option_price', models.IntegerField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.menu')),
            ],
        ),
    ]
