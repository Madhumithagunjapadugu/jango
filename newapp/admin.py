from django.contrib import admin

# Register your models here.
from newapp.models import schl

class schl_admin(admin.ModelAdmin):
    list_display=['schl_id','schl_name']
admin.site.register(schl,schl_admin)