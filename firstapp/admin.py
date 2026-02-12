from django.contrib import admin
from firstapp.models import Stud, Stud2, Insertstud, Employee

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sno','sname','age','email']

admin.site.register(Stud,StudentAdmin)



class Student2Admin(admin.ModelAdmin):
    list_display = ['snm','semail']

admin.site.register(Stud2,Student2Admin)



class StudentInsert(admin.ModelAdmin):
    list_display = ['no','name', 'fees']

admin.site.register(Insertstud,StudentInsert)



class EmployeeInsert(admin.ModelAdmin):
    pass
    # list_display = ['ename','esalary']

admin.site.register(Employee,EmployeeInsert)