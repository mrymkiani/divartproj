
from django.contrib.admin import register , ModelAdmin
from .models import Advertisment


@register(Advertisment)
class AdvertismentAdmin(ModelAdmin):
    list_display = [  #-----------------vaght namayesh in sooton ha ro ham neshoon mide
    'title' ,
    'description',
    'price',
    'user'
    ]
    
# Register your models here.
