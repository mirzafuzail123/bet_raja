# Generated by Django 4.1.5 on 2023-10-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_remove_appoverview_faq_remove_promocode_faq_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='appLogo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='appoverview',
            name='bannerImage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='logo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='logo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='websiteUrl',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='siteoverview',
            name='bannerImage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='logo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
