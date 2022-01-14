from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account import views


# Create your views here.
def register(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'register.html', context)
    



def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('user')
        password=request.POST.get('pass')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('user')
        else:
            return render(request,'login.html')

    return render(request,'login.html')


def user(request):
    data = User.objects.all()
    context={'data':data}
    return render(request,'user.html', context)

def Update(request,pk):
    data=User.objects.get(id=pk)
    form =CreateUserForm(instance=data)
    if request.method == 'POST':
        form1=CreateUserForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('user')          
    context={'form':form}
    return render(request,'update.html',context)

def Delete(request,pk):
    data=User.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('user')

    context={'data':data}
    return render(request,'delete.html',context)

