# Generated by Django 5.1.4 on 2025-02-16 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
        ('scheduler', '0029_delete_salonavailabletimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationcode',
            name='used',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='AppointmentLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=40)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='logs', to='scheduler.salon')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='app_logs', to='scheduler.appointmentslot')),
            ],
        ),
    ]
