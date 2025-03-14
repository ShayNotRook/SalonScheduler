# Generated by Django 5.1.3 on 2024-11-14 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_alter_salon_options_salonavailabletimes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='scheduler.appointmentslot'),
        ),
    ]
