# Generated by Django 4.1.5 on 2023-10-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_remove_appoverview_paymentmethods_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoverview',
            name='supportedAndroidDevices',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appoverview',
            name='supportedIosDevices',
            field=models.TextField(blank=True, null=True),
        ),
    ]
