# Generated by Django 4.2.11 on 2024-04-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestemp', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]