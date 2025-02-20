from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpRequest
from ems_app.forms import ProfileForm
from ems_app.models import Profile

# Create your views here.

def home(request):
    return render(request, 'home.html')

def showpro(request):
    profile=Profile.objects.all()
    return render(request,'showpro.html', {'pro':profile})

def register(request):
    if (request.method == "POST"):
        emp_name = request.POST.get('employee_name')
        emp_id = request.POST.get('employee_id')
        email = request.POST.get('email')
        emp_password = request.POST.get('password')
        emp_doj = request.POST.get('doj')
        if Profile.objects.filter(eID=emp_id).exists():
            messages.error(request, "Employee ID already exists.")
        elif Profile.objects.filter(emp_email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=emp_id,email=email ,password=emp_password)
            user.save()
            Profile.objects.create(eID=emp_id,emp_name=emp_name,emp_doj=emp_doj)
            messages.success(request, "Registration successful! You can now login.")
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if (request.method=='POST'):
        employee_id=request.POST.get("employee_id")
        password=request.POST.get('password')
        if not Profile.objects.filter(eID=employee_id).exists():
            #return HttpResponse("User does not exist")
            messages.error(request,"User doesn't exist.")
            return render(request,'login.html')
        user=authenticate(request,eID=employee_id,wmp_passw=password)
        if user==None:
            #return HttpResponse("Please enter a valid password")
            messages.error(request,"Please enter a valid password")
            return render(request,'login.html')
        else:
            return HttpResponse("Logged in Successfully.")
            #return redirect('home.html')
    return render(request,'login.html')

def update(request,eid):
    try:
        obj=Profile.objects.get(eID=eid)
    except Profile.DoesNotExist:
        return HttpResponse("Employee not found.")
    form=ProfileForm(isinstance=obj)
    if (request.method == 'POST'):
        form=ProfileForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse("Updated Successfully")
    return render(request,'showpro.html',{'showpro':form})


def delete(request,eid):
    try:
        obj=Profile.objects.get(eID=eid)
        obj.delete()
        return redirect('profile.html')
    except Profile.DoesNotExist:
        return HttpResponse("Employee Does not Exist!")