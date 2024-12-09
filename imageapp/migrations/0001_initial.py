# Generated by Django 5.1.3 on 2024-12-02 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('image', models.ImageField(upload_to='lion_images/', verbose_name='이미지')),
                ('description', models.TextField(verbose_name='설명')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '이미지 게시글',
                'verbose_name_plural': '이미지 게시글들',
                'ordering': ['-create_at'],
            },
        ),
    ]
