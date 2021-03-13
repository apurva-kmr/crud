from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from orderapp.forms import SignUpForm,CoustumerForm
from django.http import HttpResponseRedirect
from orderapp.models import Coustumer
from django.core.mail import send_mail
#from orderapp.forms import CoustumerForm
# Create your views here.

def Index_page(request):
    return render(request,'orderapp/index.html')
@login_required
def Login(request):
    return render(request,'orderapp/index.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'orderapp/signup.html',{'form':form})


def Logout(request):
    return render(request,'orderapp/logout.html')

def show_view(request):
    coustumer=Coustumer.objects.all()
    return render(request,'orderapp/home.html',{'coustumer':coustumer})

def insert_view(request):
    form=CoustumerForm()
    if request.method=='POST':
        form=CoustumerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request,'orderapp/insert.html',{'form':form})

def delete_view(request,id):
    coustumer=Coustumer.objects.get(id=id)
    coustumer.delete()
    return redirect('/home')


def update_view(request,id):
    coustumer=Coustumer.objects.get(id=id)
    if request.method=='POST':
        form=CoustumerForm(request.POST,instance=coustumer)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request,'orderapp/update.html',{'coustumer':coustumer})


def mail_send_view(request):
    send_mail('Order conformation','Thanks for shopping with APURVA STORE.Visit Again','testingapurva@gmail.com',['apurva143n@gmail.com'],fail_silently=False)
    return render(request,'orderapp/sharebymail.html')
