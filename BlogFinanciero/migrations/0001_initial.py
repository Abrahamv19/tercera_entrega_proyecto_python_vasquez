# Generated by Django 4.1.7 on 2023-03-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post_bloguero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('emailContacto', models.EmailField(max_length=254)),
                ('tema_interes', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Post_lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('emailContacto', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Post_temas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=60)),
                ('titulo', models.CharField(max_length=60)),
            ],
        ),
    ]
