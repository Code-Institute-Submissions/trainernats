from django.contrib import admin
from .models import Day, TNS_Class, Class_Type

# Register your models here.


class DayAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'pk',
    )

    ordering = ('pk',)


class Class_TypeAdmin(admin.ModelAdmin):
    list_display = (
        'class_type',
    )


class TNS_ClassAdmin(admin.ModelAdmin):
    list_display = (
        'class_name',
        'day',
        'class_description',
        'price',
        'class_time',
    )


admin.site.register(Day, DayAdmin)
admin.site.register(Class_Type, Class_TypeAdmin)
admin.site.register(TNS_Class, TNS_ClassAdmin)
