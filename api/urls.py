from django.urls import path
from firstapp import views

urlpatterns = [
    path('getemp/',views.get_employees,name='getemployee'),
    path('listemp/',views.listemployees.as_view(),name='listemployee'),

]