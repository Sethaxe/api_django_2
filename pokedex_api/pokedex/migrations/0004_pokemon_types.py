# Generated by Django 5.0.4 on 2024-04-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='pokemon_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.IntegerField()),
                ('type_id', models.IntegerField()),
                ('slot', models.IntegerField()),
            ],
        ),
    ]