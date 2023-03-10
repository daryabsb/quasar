# Generated by Django 4.1.5 on 2023-02-07 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_prescription_created_prescription_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientHealthStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_condition', models.CharField(max_length=100)),
                ('blood_sugar', models.IntegerField()),
                ('blood_pressure', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('smoking_status', models.BooleanField()),
                ('alcohol_consumption', models.BooleanField()),
                ('physical_activity', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
            ],
        ),
    ]
