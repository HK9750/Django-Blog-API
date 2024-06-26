# Generated by Django 5.0.6 on 2024-05-08 11:28

import datetime
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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 5, 8, 11, 28, 35, 59133, tzinfo=datetime.timezone.utc))),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
