from django.contrib import admin
from .models import SiteSettings,SiteAddress,SitePhoneNum,SiteSocialMedia,SiteLogos

admin.site.register(SiteSettings)
admin.site.register(SiteAddress)
admin.site.register(SitePhoneNum)
admin.site.register(SiteSocialMedia)
admin.site.register(SiteLogos)
