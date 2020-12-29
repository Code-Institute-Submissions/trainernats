from django.contrib import admin
from .models import Day, TNS_Class

# Register your models here.
class DayAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'class_time',
        'pk',
    )

    ordering = ('pk',)
    
class TNS_ClassAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'day',
        'class_description',
        'price',
    )


admin.site.register(Day, DayAdmin)
admin.site.register(TNS_Class, TNS_ClassAdmin)