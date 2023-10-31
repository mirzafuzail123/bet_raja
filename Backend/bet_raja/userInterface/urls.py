from django.urls import path
from .sites.views import NavOptionsView ,  AllSiteListView , IplSiteListView , SiteOverviewView
from .apps.views import AllAppsListView , IplAppListView , AppOverviewView
from .promoCode.views import PromoCodeView
from .sports.views import SportView

urlpatterns = [
    # NavOptions
    path("navOptions/" , NavOptionsView.as_view() , name="navOptions") , 
    # Sites
    path("sites/" , AllSiteListView.as_view() , name="sites") , 
    path("iplSites/" , IplSiteListView.as_view() , name="iplSites") , 
    path("siteOverview/<slug>/" , SiteOverviewView.as_view() , name="siteOverview") , 
    # Apps
    path("apps/" , AllAppsListView.as_view() , name="apps") , 
    path("iplApps/" , IplAppListView.as_view() , name="iplApps") , 
    path("appOverview/<slug>/" , AppOverviewView.as_view() , name="appOverview") , 
    # Promo Code
    path("promoCode/<slug>/" , PromoCodeView.as_view() , name="promoCode")  ,   
    # Sports
    path("sports/<slug>/" , SportView.as_view() , name="sports")
]
