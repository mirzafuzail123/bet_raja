from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(PaymentMethod)
admin.site.register(Sport)
admin.site.register(Site)

admin.site.register(SiteOverview)
admin.site.register(App)
admin.site.register(AppOverview)
admin.site.register(PromoCode)