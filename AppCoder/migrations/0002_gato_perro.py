# Generated by Django 4.1 on 2022-09-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
