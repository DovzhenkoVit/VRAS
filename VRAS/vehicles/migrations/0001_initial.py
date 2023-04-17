# Generated by Django 4.2 on 2023-04-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('year', models.IntegerField(max_length=9)),
                ('licence_plate', models.CharField(max_length=8)),
                ('rental_rate', models.IntegerField(max_length=10)),
            ],
        ),
    ]
