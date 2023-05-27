from django.contrib import admin
from .models import my_store
# Register your models here.
@admin.register(my_store)
class show(admin.ModelAdmin):
    list_display=['id','my_name','city','slug']
    
