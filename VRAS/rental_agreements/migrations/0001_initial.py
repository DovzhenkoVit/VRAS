# Generated by Django 4.2 on 2023-04-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentalAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_duration', models.DurationField()),
                ('rental_fee', models.IntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('payment_receipt', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
