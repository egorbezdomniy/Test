from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Evaporator)
admin.site.register(models.EvaporatorBrand)
admin.site.register(models.Pod)
admin.site.register(models.PodBrand)
admin.site.register(models.Single)
admin.site.register(models.SingleBrand)
admin.site.register(models.Liquid)
admin.site.register(models.LiquidBrand)
admin.site.register(models.Sale)
