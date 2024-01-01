# Generated by Django 5.0 on 2024-01-01 09:32

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
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='スキル')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('description', models.CharField(max_length=500, verbose_name='説明')),
                ('demo_link', models.URLField(verbose_name='リンク')),
                ('github_repo', models.URLField(verbose_name='GitHub')),
                ('content', models.TextField(verbose_name='テキスト')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='更新日')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio_app.skill')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
