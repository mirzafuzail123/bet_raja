# Generated by Django 4.1.5 on 2023-10-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_alter_site_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='paymentMethods',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
