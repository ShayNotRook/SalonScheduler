# Generated by Django 5.1.4 on 2025-01-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0023_service_provider_alter_appointmentslot_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='telegram_link',
            field=models.URLField(blank=True),
        ),
    ]
