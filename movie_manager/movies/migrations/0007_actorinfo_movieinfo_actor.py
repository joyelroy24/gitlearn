# Generated by Django 5.0 on 2023-12-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movieinfo_directed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actorinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='actor',
            field=models.ManyToManyField(related_name='movie_actor', to='movies.actorinfo'),
        ),
    ]
