# Generated by Django 4.1 on 2022-09-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_gato_perro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=60)),
                ('especialidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gimnasio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fechaCreacion', models.DateField()),
                ('Localicacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Maquinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('zonaDeTrabajo', models.CharField(max_length=60)),
                ('pesoMax', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Familiar',
        ),
        migrations.DeleteModel(
            name='Gato',
        ),
        migrations.DeleteModel(
            name='Perro',
        ),
    ]