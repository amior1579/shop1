from django.urls import path, include
from . import views
from site_setting import views

app_name = 'siteSetting-web'

urlpatterns = [
    
    # API
    path("api_SiteSettings", views.view_siteSettings, name="site-Settings"),
]
