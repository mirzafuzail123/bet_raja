from django.urls import path
from .auth.views import LoginView
from .sites.views import SiteListView , SingleSiteView, CreateSiteView ,EditSiteView , SiteOverviewListView  , CreateSiteOverviewView , SingleSiteOverviewView , EditSiteOverviewView
from .sports.views import SportsListView , SingleSportsView  , CreateSportsView , EditSportsView
from .apps.views import AppsListView , SingleAppsView  ,CreateAppView , AppOverviewListView , CreateAppOverviewView , SingleAppOverviewView
from .promoCode.views import PromoCodeListView , SinglePromoCodeView , CreatePromoCodeView


urlpatterns = [
    # auth
    path('login/' ,LoginView.as_view() , name="login" ) , 
    # Sites
    path('sites/' ,SiteListView.as_view() , name="siteList" ) , 
    path('sites/<int:pk>/' ,SingleSiteView.as_view() , name="siteList" ) ,
    path('sites/create/' ,CreateSiteView.as_view() , name="createSite" ) ,
    path('sites/edit/<int:pk>/' ,EditSiteView.as_view() , name="editSIte" ) ,
 
    # Site Overview
    path('siteOverview/' ,SiteOverviewListView.as_view() , name="siteOverview" ) , 
    path('siteOverview/<int:pk>/' ,SingleSiteOverviewView.as_view() , name="siteOverview_single" ) , 
    path('siteOverview/create/' ,CreateSiteOverviewView.as_view() , name="siteOverview_create" ) , 
    path('siteOverview/edit/<int:pk>/' ,EditSiteOverviewView.as_view() , name="siteOverview_edit" ) , 
    # apps
    path('apps/' ,AppsListView.as_view() , name="apps" ) , 
    path('apps/<int:pk>/' ,SingleAppsView.as_view() , name="apps_single" ) , 
    path('apps/create/' ,CreateAppView.as_view() , name="apps_create" ) , 
    path('apps/edit/<int:pk>/' ,SingleAppsView.as_view() , name="apps_edit" ) , 
       # apps Overview
    path('appOverview/' ,AppOverviewListView.as_view() , name="appOverview" ) , 
    path('appOverview/<int:pk>/' ,SingleAppOverviewView.as_view() , name="appOverview_single" ) , 
    path('appOverview/create/' ,CreateAppOverviewView.as_view() , name="appOverview_create" ) , 
    path('appOverview/edit/<int:pk>/' ,SingleAppOverviewView.as_view() , name="appOverview_edit" ) ,
    # Sports
    path('sports/' ,SportsListView.as_view() , name="sportsList" ) , 
    path('sports/<int:pk>/' ,SingleSportsView.as_view() , name="sports" ) , 
    path('sports/create/' ,CreateSportsView.as_view() , name="sportsCreate" ) , 
    path('sports/edit/<int:pk>/' ,EditSportsView.as_view() , name="sportsEdit" ) , 
    # Promo Code
    path('promoCode/' ,PromoCodeListView.as_view() , name="promoCode" ) , 
    path('promoCode/<int:pk>/' ,SinglePromoCodeView.as_view() , name="promoCode_single" ) , 
    path('promoCode/create/' ,CreatePromoCodeView.as_view() , name="promoCode_create" ) , 
    path('promoCode/edit/<int:pk>/' ,SinglePromoCodeView.as_view() , name="promoCode_edit" ) , 
]
