# Generated by Django 5.0.6 on 2024-08-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firsts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(max_length=122)),
                ('pass1', models.CharField(max_length=122)),
            ],
        ),
    ]
