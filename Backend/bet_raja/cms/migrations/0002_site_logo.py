# Generated by Django 4.1.5 on 2023-10-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
