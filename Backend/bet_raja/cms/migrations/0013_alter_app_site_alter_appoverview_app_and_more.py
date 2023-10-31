# Generated by Django 4.1.5 on 2023-10-30 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_remove_sitepros_site_app_cons_app_coverimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to='cms.site'),
        ),
        migrations.AlterField(
            model_name='appoverview',
            name='app',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appOverview', to='cms.app'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sitePromoCode', to='cms.site'),
        ),
    ]