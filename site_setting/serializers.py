from rest_framework import serializers
from .models import SiteSettings


class SiteSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ('site_name','site_logo','site_address','site_email','site_phoneNum', 'site_socialMedia')