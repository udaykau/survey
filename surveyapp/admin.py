from django.contrib import admin
from .models import survey
# Register your models here.

class Survey(admin.ModelAdmin):
    list_display = ('sno', 'Active', 'Name', 'Care_Of', 'Mobile_Number', 'Email', 'Pan_Number', 'date')


admin.site.register(survey, Survey)