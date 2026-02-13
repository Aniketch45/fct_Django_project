from django.shortcuts import render
from firstapp.models import Stud, Stud2, Insertstud, Employee
from django.http import *
from firstapp.forms import StudentForm2, StudentForm
from django.conf import settings
from django.core.mail import send_mail
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

def home(request):
    student = Stud.objects.all()
    return render(request,'firstapp/index.html',{'stud' : student})

def home2(request):
    return render(request,'firstapp/home.html')

def addstud(request):
    sn = 45
    snm = "Om"
    age = 34
    gmail = 'abc1234@gmail.com'

    s = Stud(sno = sn,sname = snm,age = age,email = gmail)
    s.save()
    return HttpResponse("<h2>Record Inserted Successfully</h2>")

def updatestud(request,myid):
    sn = 8
    snm = "Om"
    age = 80
    gmail = 'abc1234@gmail.com'

    s = Stud(id = myid,sno = sn,sname = snm,age = age,email = gmail)
    s.save()
    return HttpResponse("<h1>Records updated successfully</h1>")

def deletestud(request,myid):
    s = Stud.objects.get(id=myid)
    s.delete()
    return HttpResponse("<h1>Record Deleted</h1>")

def showforms(request):
    if request.method == "POST":
        st = StudentForm(request.POST)
        if st.is_valid():
            name = st.cleaned_data['sname']
            email = st.cleaned_data['semail']
            st2 = Stud2(snm = name, semail = email)
            st2.save()

    else:
        print("This is get request")
        st = StudentForm()

    return render(request,'firstapp/home.html',{'so':st})

def insertstud(request):
    if request.method == "POST":
        st2 = StudentForm2(request.POST)
        if st2.is_valid():
            no3 = st2.cleaned_data['sno']
            name3 = st2.cleaned_data['name'] 
            fees3 = st2.cleaned_data['sfees']
            st3 = Insertstud(no = no3, name = name3, fees = fees3)
            st3.save()

    else:    
        print("this is get request")
        st2 = StudentForm2()

    return render(request,'firstapp/insert.html',{'sar':st2})

def update(request, sid):
    if request.method == 'POST':
        sno = request.POST.get('t1')
        sname = request.POST.get('t2')
        sfees = request.POST.get('t3')
        st = Stud(id = sid, no = sno, name = sname, fees = sfees)
        st.save()
        return HttpResponseRedirect('/firstapp/stud.html')
    
    else:
        studobject = Insertstud.objects.get(id=sid)
        st = StudentForm2()
        
    return render(request,'firstapp/stud.html', {'io': studobject, 'form': st})


def home3(request):
    return render(request,'firstapp/stud.html')

def image(request):
    if request.method == "POST":
        to = request.POST.get('txt1')
        msg = request.POST.get('txt2')
        # print("To:",to)
        # print("Message :",msg)
        send_mail("testmail",msg,settings.EMAIL_HOST_USER,[to])
        return render(request,'firstapp/image_display.html')
    else:
        return render(request,'firstapp/image_display.html')
    
@api_view(['GET','POST'])
def get_employees(request):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp,many=True)
    return Response({'data':serializer.data})

class listemployees(APIView):
    def get(self,request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response({'data':serializer.data})


    def post(self,request):
        serialize_data = EmployeeSerializer(data=request.data)
        if serialize_data.is_valid(raise_exception=True):
            obj = serialize_data.save()
            return Response({ 'success':"{} data inserted succesfully".format(obj.ename)})
        return Response(serialize_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
class UpdateEmployees(APIView):
    def get(self,request,id):
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp)
        return Response({'data':serializer.data})
    
    def put(self,request,id):
        emp = Employee.objects.get(id=id)
        serialize_data = EmployeeSerializer(emp,data=request.data)
        if serialize_data.is_valid(raise_exception=True):
            obj = serialize_data.save()
            return Response({ 'success':"{} data inserted succesfully".format(obj.ename)})
        return Response(serialize_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response(status=status.HTTP_200_OK)
        
