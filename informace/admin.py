from django.contrib import admin

from .models import City, Divadlo

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "nazev", "kraj", "rozloha", "pocet", "region", "divadlo")
    list_filter = ("nazev", "pocet")
    
class DivadloAdmin(admin.ModelAdmin):
    list_display = ("id", "nazev", "umisteni")
    

   

admin.site.register(City, CityAdmin)
admin.site.register(Divadlo, DivadloAdmin)


    


