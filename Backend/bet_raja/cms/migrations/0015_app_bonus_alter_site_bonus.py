# Generated by Django 4.1.5 on 2023-10-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_alter_app_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='bonus',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='bonus',
            field=models.CharField(max_length=1000),
        ),
    ]
