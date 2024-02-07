from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Task
from .forms import SignUpForm, AddTask


# Create your views here.
def home(request):
    tasks = Task.objects.all()
    #verificar si tas loggeado
    if request.method == 'POST':
        usrname = request.POST['usrname']
        passwd = request.POST['password']
        #auth
        user = authenticate(request,username=usrname, password=passwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"No eres usuario we UnU")
            return redirect('home')
    else:
        return render(request,'home.html',{'tasks':tasks})
    
def logout_usr(request):
    logout(request)
    return redirect('home')


def register_usr(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if  form.is_valid():
            form.save()
            #loggiando despues de regitrarse
            usrname = form.cleaned_data['username']
            passwd = form.cleaned_data['password1']
            user = authenticate(request,username=usrname, password=passwd)
            login(request,user)
            messages.success(request, "Te registraste con exito wuuuu")
            return redirect('home')
    else:
        form = SignUpForm()
        # return redirect(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def add_task(request):
    form = AddTask(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_record = form.save()
            messages.success(request,"Tarea agregada :)")
            return redirect('home')
        return render(request, 'add_task.html',{'form':form})
    else:
        return redirect('home')