from django.contrib import admin
from .models import Children, Crime, Fire_damage, Flood, Alcohol, House, Population

admin.site.register(Children)
admin.site.register(Crime)
admin.site.register(Fire_damage)
admin.site.register(Flood)
admin.site.register(Alcohol)
admin.site.register(House)
admin.site.register(Population)

# Register your models here.
