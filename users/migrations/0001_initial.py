# Generated by Django 4.0 on 2021-12-22 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('firstLastName', models.CharField(max_length=50)),
                ('secondLastName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=150)),
                ('lastLogin', models.DateTimeField(auto_now=True)),
                ('registeredAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
