import os
from uuid import uuid4
from django.db import models
from django.utils.deconstruct import deconstructible
import json


@deconstructible
class CustomLogoName:
    def __init__(self, path, custom_text):
        self.path = path
        self.custom_text = custom_text

    def __call__(self, instance, filename):
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}_{self.custom_text}{ext}"
        return os.path.join(self.path, new_filename)


class SiteAddress(models.Model):
    address  = models.CharField (max_length=100, verbose_name="آدرس سایت")
    def __str__(self):
        return f'{self.address}'
    
class SitePhoneNum(models.Model):
    PhoneNum  = models.CharField (max_length=100, verbose_name="تلفن سایت")
    
    def __str__(self):
        return f'{self.PhoneNum}'
    
class SiteSocialMedia(models.Model):
    SocialMediaLink  = models.CharField (max_length=100, verbose_name="شبکه های اجتماعی سایت")
    
    def __str__(self):
        return f'{self.SocialMediaLink}'
    
    
class SiteLogos(models.Model):
    logo_light = models.ImageField(upload_to=CustomLogoName('assets/images/logo/', "light"), verbose_name=('لوگو مود لایت'))
    logo_dark  = models.ImageField(upload_to=CustomLogoName('assets/images/logo/', "dark") , verbose_name=('لوگو مود دارک'))
    
    def __str__(self):
        return f'{self.logo_light},{self.logo_dark}'
    
    
class SiteSettings(models.Model):
    site_name        = models.CharField (max_length=100,verbose_name="نام سایت")
    site_logo        = models.ManyToManyField(SiteLogos, verbose_name=('لوگو سایت'), blank=True, null=True)
    site_address     = models.ManyToManyField(SiteAddress,verbose_name="آدرس سایت", blank=True, null=True)
    site_email       = models.EmailField(max_length=100, verbose_name="ایمیل سایت", blank=True, null=True)
    site_phoneNum    = models.ManyToManyField (SitePhoneNum, verbose_name="تلفن سایت", blank=True, null=True)
    site_socialMedia = models.ManyToManyField(SiteSocialMedia,verbose_name="شبکه های اجتماعی سایت", blank=True, null=True)