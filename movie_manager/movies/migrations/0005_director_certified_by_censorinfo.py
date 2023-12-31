# Generated by Django 5.0 on 2023-12-11 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movieinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='certified_by',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Censorinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10, null=True)),
                ('movie_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='censor', to='movies.movieinfo')),
            ],
        ),
    ]
