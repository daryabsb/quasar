# Generated by Django 4.1.5 on 2023-01-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_address_appointment_attachment_client_prescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
