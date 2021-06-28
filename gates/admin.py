from django.contrib import admin
from . models import items

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display=("types","title","datepost")
    prepopulated_fields = {'slug':('title',)}
    #list_editable=("description",)


admin.site.register(items,ItemAdmin)
