# Generated by Django 4.1.5 on 2023-10-22 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('downloads', models.BigIntegerField()),
                ('reviews', models.IntegerField()),
                ('version', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=100)),
                ('appLogo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1024)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('bonus', models.CharField(max_length=250)),
                ('promoCode', models.CharField(max_length=50)),
                ('websiteUrl', models.URLField()),
                ('rating', models.FloatField()),
                ('android', models.BooleanField(default=True)),
                ('ios', models.BooleanField(default=True)),
                ('window', models.BooleanField(default=True)),
                ('ipl', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('logo', models.URLField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='sitePros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pros', models.TextField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitePros', to='cms.site')),
            ],
        ),
        migrations.CreateModel(
            name='SiteOverview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerImage', models.URLField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('mainInformation', models.JSONField(blank=True, null=True)),
                ('screenshot', models.TextField(blank=True, null=True)),
                ('legality', models.TextField(blank=True, null=True)),
                ('officialReview', models.TextField(blank=True, null=True)),
                ('registration', models.TextField(blank=True, null=True)),
                ('howToLogin', models.JSONField(blank=True, null=True)),
                ('accountVerification', models.TextField(blank=True, null=True)),
                ('howToPlaceBet', models.JSONField(blank=True, null=True)),
                ('bonuses', models.TextField(blank=True, null=True)),
                ('bonusList', models.JSONField(blank=True, null=True)),
                ('bettingMarket', models.TextField(blank=True, null=True)),
                ('sportsBetting', models.TextField(blank=True, null=True)),
                ('mobileApp', models.TextField(blank=True, null=True)),
                ('depositMethods', models.TextField(blank=True, null=True)),
                ('howToMakeDeposit', models.JSONField(blank=True, null=True)),
                ('withdrawMethods', models.TextField(blank=True, null=True)),
                ('howToMakeWithdraw', models.JSONField(blank=True, null=True)),
                ('licenseSecurity', models.TextField(blank=True, null=True)),
                ('customerService', models.TextField(blank=True, null=True)),
                ('opinion', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('faq', models.ManyToManyField(to='cms.faq')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='siteOverview', to='cms.site')),
            ],
        ),
        migrations.CreateModel(
            name='siteCons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cons', models.TextField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='siteCons', to='cms.site')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='sports',
            field=models.ManyToManyField(related_name='sites', to='cms.sport'),
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('promoCode', models.TextField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('bonuses', models.TextField(blank=True, null=True)),
                ('bonusList', models.JSONField(blank=True, null=True)),
                ('howToClaimBonus', models.JSONField(blank=True, null=True)),
                ('paymentMethods', models.TextField(blank=True, null=True)),
                ('opinion', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('faq', models.ManyToManyField(to='cms.faq')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.site')),
            ],
        ),
        migrations.CreateModel(
            name='AppOverview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerImage', models.URLField(blank=True, null=True)),
                ('appMainInformation', models.JSONField(blank=True, null=True)),
                ('androidDownloadSteps', models.JSONField(blank=True, null=True)),
                ('androidSystemRequirements', models.JSONField(blank=True, null=True)),
                ('supportedAndroidDevices', models.TextField(null=True)),
                ('iosDownloadSteps', models.JSONField(blank=True, null=True)),
                ('iosSystemRequirements', models.JSONField(blank=True, null=True)),
                ('supportedIosDevices', models.TextField(null=True)),
                ('bonuses', models.TextField(blank=True, null=True)),
                ('bonusList', models.JSONField(blank=True, null=True)),
                ('howToBet', models.JSONField(blank=True, null=True)),
                ('accountRegistration', models.JSONField(blank=True, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('customerSupport', models.TextField(blank=True, null=True)),
                ('opinion', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.app')),
                ('faq', models.ManyToManyField(to='cms.faq')),
                ('paymentMethods', models.ManyToManyField(to='cms.paymentmethod')),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.site'),
        ),
    ]
