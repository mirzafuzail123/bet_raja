from django.db import models
from django.utils.text import slugify

# Create your models here.



#Payment Methods
class PaymentMethod(models.Model):
    name=models.CharField(max_length=50)
    logo=models.TextField()

    def __str__(self):
        return self.name
    
    


# Sports
class Sport(models.Model):
    name=models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    description=models.TextField()
    logo=models.TextField(null=True , blank=True)

    pros=models.JSONField(null=True , blank=True)
    cons=models.JSONField(null=True , blank=True)
    
    whatIsApp=models.TextField(null=True , blank=True)
    howToChose=models.JSONField(null=True , blank=True)
    howToDownload=models.TextField(null=True , blank=True)

    androidDownloadSteps=models.JSONField(null=True , blank=True)
    iosDownloadSteps=models.JSONField(null=True , blank=True)

    howToStartPlaying=models.TextField(null=True , blank=True)
    bonuses=models.TextField(null=True , blank=True)
    bonusList=models.JSONField(null=True , blank=True)
    howToDeposit=models.JSONField(null=True , blank=True)
    paymentMethods=models.JSONField(null=True , blank=True)
    security=models.TextField(null=True , blank=True)
    faq=models.JSONField(null=True , blank=True)
    opinion=models.TextField(null=True , blank=True)
    created=models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

# Site
class Site(models.Model):
    name=models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description=models.TextField()
    logo=models.TextField(null=True  , blank=True)
    bonus=models.CharField(max_length=1000)
    promoCode=models.CharField(max_length=50)
    websiteUrl=models.TextField()
    rating=models.FloatField()
    pros=models.JSONField(null=True , blank=True)
    cons=models.JSONField(null=True , blank=True)
    features=models.TextField(null=True , blank=True)
    paymentMethods=models.JSONField(null=True , blank=True)
    android=models.BooleanField(default=True)
    ios=models.BooleanField(default=True)
    window=models.BooleanField(default=True)
    ipl=models.BooleanField(default=True)
    sports=models.ManyToManyField(Sport ,  related_name="sites")
    created=models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Site, self).save(*args, **kwargs)


    def __str__(self):
        return self.name



# Site Overview
class SiteOverview(models.Model):
    site=models.OneToOneField(Site , on_delete=models.CASCADE ,  related_name="siteOverview")
    bannerImage=models.TextField(null=True , blank=True)
    overview=models.TextField(null=True , blank=True)
    mainInformation=models.JSONField(null=True , blank=True)
    screenshot=models.TextField(null=True , blank=True)
    legality=models.TextField(null=True , blank=True)
    officialReview=models.TextField(null=True , blank=True)
    registration=models.TextField(null=True , blank=True)
    howToLogin=models.JSONField(null=True , blank=True)
    accountVerification=models.TextField(null=True , blank=True)
    howToPlaceBet=models.JSONField(null=True , blank=True)
    bonuses=models.TextField(null=True , blank=True)
    bonusList=models.JSONField(null=True , blank=True)
    bettingMarket=models.TextField(null=True , blank=True)
    sportsBetting=models.TextField(null=True , blank=True)    
    mobileApp=models.TextField(null=True , blank=True)    
    depositMethods=models.TextField(null=True , blank=True)
    howToMakeDeposit=models.JSONField(null=True , blank=True)
    withdrawMethods=models.TextField(null=True , blank=True)
    howToMakeWithdraw=models.JSONField(null=True , blank=True)
    licenseSecurity=models.TextField(null=True , blank=True)
    customerService=models.TextField(null=True , blank=True)
    faq=models.JSONField(null=True , blank=True)
    opinion=models.TextField(null=True , blank=True)
    created=models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.site


# App
class App(models.Model):
    site=models.OneToOneField(Site , on_delete=models.CASCADE , related_name="app")
    description=models.TextField(null=True , blank=True)
    downloads=models.BigIntegerField()
    reviews=models.IntegerField()
    version=models.CharField(max_length=50)
    size=models.CharField(max_length=100)
    bonus=models.CharField(max_length=1000 , null=True , blank=True)
    appLogo=models.TextField()
    pros=models.JSONField(null=True , blank=True)
    cons=models.JSONField(null=True , blank=True)
    coverImage=models.TextField(null=True , blank=True)

    # def __str__(self):
    #     return self.site


# App Overview
class AppOverview(models.Model):
    app=models.OneToOneField(App , on_delete=models.CASCADE , related_name="appOverview")
    bannerImage=models.TextField(null=True , blank=True)
    appMainInformation=models.JSONField(null=True , blank=True)

    androidDownloadSteps=models.JSONField(null=True , blank=True)
    androidSystemRequirements=models.JSONField(null=True , blank=True)
    supportedAndroidDevices=models.TextField(null=True , blank=True)

    iosDownloadSteps=models.JSONField(null=True , blank=True)
    iosSystemRequirements=models.JSONField(null=True , blank=True)
    supportedIosDevices=models.TextField(null=True , blank=True) 

    bonuses=models.TextField(null=True , blank=True)
    bonusList=models.JSONField(null=True , blank=True)

    howToBet=models.JSONField(null=True , blank=True) 
    accountRegistration=models.JSONField(null=True , blank=True)  
    paymentMethods=models.JSONField(null=True , blank=True)  

    features=models.TextField(null=True , blank=True)
    customerSupport=models.TextField(null=True , blank=True)

    faq=models.JSONField(null=True , blank=True)
    opinion=models.TextField(null=True , blank=True)
    created=models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.site


# Promo Code
class PromoCode(models.Model):
    site=models.OneToOneField(Site , on_delete=models.CASCADE , related_name="sitePromoCode")
    description=models.TextField(null=True , blank=True)
    promoCode=models.TextField(null=True , blank=True)
    about=models.TextField(null=True , blank=True)
    bonuses=models.TextField(null=True , blank=True)
    bonusList=models.JSONField(null=True , blank=True)
    howToClaimBonus=models.JSONField(null=True , blank=True)
    paymentMethods=models.TextField(null=True , blank=True)
    faq=models.JSONField(null=True , blank=True)
    opinion=models.TextField(null=True , blank=True)
    created=models.DateField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.site


