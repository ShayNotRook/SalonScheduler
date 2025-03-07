# Generated by Django 5.1.2 on 2024-10-31 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration_time', models.PositiveIntegerField()),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.salon')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.salon')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.service')),
            ],
        ),
    ]
