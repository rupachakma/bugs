from django.contrib import admin

from App.models import Items

# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display=('id','name','description','quantity','price')

admin.site.register(Items,ItemsAdmin)