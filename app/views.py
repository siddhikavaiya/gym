from django.shortcuts import render,redirect
from .models import *
import razorpay
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import random
import smtplib

def about(request):
    cat=exe.objects.all()
    sub=subexe.objects.all()
    return render(request,'about.html',{"cat":cat})

def contact(request):
    cat=exe.objects.all()
    sub=subexe.objects.all()
    return render(request,'contact.html',{"cat":cat})

def index(request):
    cat=exe.objects.all()
    print(cat,"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    sub=subexe.objects.all()
    return render(request,'index.html',{"cat":cat})

def member1(request):
    cat=exe.objects.all()
    sub=subexe.objects.all()
    return render(request,'membership.html',{"cat":cat})


def workout1(request):
    cid =  request.GET.get("cid")
    cat=exe.objects.all()
    sub=subexe.objects.all()
    data = workout.objects.filter(ename__id=cid)
    return render(request,'blog_details.html',{'cat':cat,'sub':sub,"data":data})

def register(request):
    cat=exe.objects.all()
    sub=subexe.objects.all()
    if request.method =="POST":

        name =  request.POST['name']
        gender=request.POST['gender']
        phone=request.POST['phone']
        email =  request.POST['email']
        password =  request.POST['password']
        user=reg(name=name,gender=gender,phone=phone,email=email,password=password)
        user.save()
        return redirect('payment')

    else:
        return render(request,"registration.html",{"cat":cat})

def login(request):
    cat=exe.objects.all()
    sub=subexe.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        error = None
        try:
            user = reg.objects.get(email=email)
            if user.password==password:
                request.session['user']=email
                return redirect('/')
            else:
                return render(request,'login.html',{'error':"Invalid Password"})
        except:
            return render(request, 'login.html',{'error':"Invalid Email or Password"})
    else:
        return render(request,"login.html",{"cat":cat}) 

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    else:
        return redirect('/')
    return redirect('/')


def payment(request):
    cat=exe.objects.all()
    sub=subexe.objects.all()
    cat=exe.objects.all()
    sub=subexe.objects.all()
    if request.method =="POST":

        name =  request.POST['name']
        gender=request.POST['gender']
        phone=request.POST['phone']
        email =  request.POST['email']
        password =  request.POST['password']
        user=reg(name=name,gender=gender,phone=phone,email=email,password=password)
        user.save()
        
    
    amount = 500*100 #100 here means 1 dollar,1 rupree if currency INR
    client = razorpay.Client(auth=('rzp_test_vfui8bnxOeKPqd','3tY6nOpjgTurmBqXLzkEWZc1'))
    response = client.order.create({'amount':amount,'currency':'USD','payment_capture':1})
    print(response)
    context = {'response':response,"cat":cat}
    return render(request,"payment.html",context)



@csrf_exempt
def payment_success(request):
    cat=exe.objects.all()
    sub=subexe.objects.all()
    if request.method =="POST":
        print(request.POST)
        return render(request,'payment_success.html',{"cat":cat})
    return redirect('/')

def forpass(request):
    if request.method=='POST':
        email_id=request.POST['email']
        otp=random.randint(0000,9999)
        user=reg.objects.get(email=email_id)
        if user is not None:
            emsend=send_mail(
                'OTP verification',
                f'Your OTP:{otp}',
                'siddhikavaiya1@gmail.com',
                [email_id],)
            request.session['otp']=otp
            request.session['user']=user.email
            return redirect('emotp')
        else:
            error="Invalid Email"
            return render(request,'forpass.html',{'error':error})
    else:
        return render(request,'forpass.html')      

def emotp(request):
    inotp=request.session['otp']
    if request.method=='POST':
        otp=request.POST['eotp']
        if inotp == int(otp):
            return redirect('matchpass')
        else:
            return redirect('emotp')
    else:
        return render(request,'emotp.html')          

def matchpass(request):
    if request.method=='POST':
        eemail=request.session['user']
        user=reg.objects.get(email=eemail)
        if request.method=='POST':
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            if pass1==pass2:
                user.password=pass2
                print(user.password,'FFFFFFFFFFFFFFFFFFFF')
                user.save()
                return redirect('login')
            else:
                return redirect('matchpass')
        else:
            return redirect('emotp')

    return render(request,'passmatch.html')