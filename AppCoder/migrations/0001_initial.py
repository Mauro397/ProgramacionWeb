# Generated by Django 4.1 on 2022-09-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('fecha', models.CharField(max_length=30)),
            ],
        ),
    ]
