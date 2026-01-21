from django.contrib import admin
from firstapp.models import Stud

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sno','sname','age','email']

admin.site.register(Stud,StudentAdmin)