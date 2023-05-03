# Generated by Django 4.2 on 2023-05-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_agreements', '0002_rentalagreement_customer_rentalagreement_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalagreement',
            name='rental_duration',
        ),
        migrations.AddField(
            model_name='rentalagreement',
            name='rental_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='rentalagreement',
            name='rental_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='rentalagreement',
            name='payment_receipt',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
