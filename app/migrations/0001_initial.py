# Generated by Django 3.1 on 2021-02-08 22:54

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='SiteWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1500)),
                ('url', models.CharField(max_length=1500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(blank=True, null=True, upload_to=app.models.SiteWeb.upload_path)),
                ('visible', models.IntegerField(default=1)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorie')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
