from django.shortcuts import render,redirect,HttpResponse
import requests
from .forms import userRegisterForm,userLoginForm,userRegForm,userOtpForm
import json

def userAuth(request): 
    if request.COOKIES.get('user', None) != None:
        return redirect(userDashboard)
    if request.method=="POST":
        form = userRegisterForm(request.POST)
        phone = request.POST.get('phone')  
        phone = int(phone)
        request.session['phone']= phone
        response = requests.post('http://api.e-sportsindia.in/user/auth/', json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
        if response.status_code == 200:
            data = response.json()
            print(data) 
            if data['desc'] =="User Not Found":
                return redirect(userRegister)
            elif data['desc'] == "User Found": 
                res = requests.post('http://api.e-sportsindia.in/user/auth/login/', json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
                res = res.json()
                print(res)
                request.session['otp']= res['otp']
                return redirect(userLoginOtp)
        else:
            data = response.json()
            return render(request,'registration/auth.html')
    else:
        form = userRegisterForm
        return render(request,'registration/auth.html',{'form':form})

def userRegister(request):
    if request.COOKIES.get('user', None) != None:
        return redirect(userDashboard)
    if not request.session.get('phone'):
        return redirect(userAuth)
    if request.method == "POST":
        form = userRegForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.session['phone']  
        response = requests.post('http://api.e-sportsindia.in/user/auth/register/',json={'name':name,'email':email,'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
        if response.status_code == 200:
            register = response.json()
            print(register)
            if register['desc'] == "User Registed":
                otp = register['otp']
                request.session['otpreg']=otp
                return redirect(userRegisterOtp)
            elif register['desc'] == "User Not Found":
                return redirect(userRegister)
            elif register['desc'] == "Invalid Data":
                return redirect(userRegister)
    else:
        form = userRegForm()
        return render(request,'registration/register.html',{'form':form})
    
def userLoginOtp(request):
    if request.COOKIES.get('user', None) != None:
        return redirect(userDashboard)
    phone = request.session['phone']
    if request.method == "POST":
        form = userOtpForm(request.POST)
        otp = request.POST.get('otp')     
        phone = request.session['phone']
        otp = int(otp)
        if otp == request.session['otp']:
            response = redirect(userDashboard)
            response.set_cookie('user',phone, 3600 * 24 * 15)
            return response
    else:
        form = userOtpForm
        phone = request.session['phone']
        return render(request,'registration/login.html',{'phone':phone,'form':form})    


def userRegisterOtp(request):
    if request.COOKIES.get('user', None) != None:
        return redirect(userDashboard)
    if request.method == "POST":         
        form = userOtpForm(request.POST)
        otp = request.POST.get('otp')
        phone = request.session['phone']
        restOtp = request.session['otpreg']
        otp = int(otp)
        if otp == restOtp:
            otpApi = requests.post('http://api.e-sportsindia.in/user/auth/otp/',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39","phone":phone,"verify":1 })
            return redirect(userDashboard) 
        else:
            return redirect(userRegisterOtp)
    else:
        form = userOtpForm
        phone = request.session['phone']
        return render(request,'registration/registerOtp.html',{'form':form,'phone':phone})


def userDashboard(request):
    #json_data = open("tournament.json").read()
    if request.COOKIES.get('user', None) == None:
        return redirect(userAuth)
    phone = request.COOKIES['user']
    phone = int(phone)
    response = requests.post('http://api.e-sportsindia.in/user/data/', json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
    if response.status_code ==200:
        data = response.json()
       
        email = data['data']['email']
        name  = data['data']['name']
        print(email)
    data={
            "tor": [{
                    "image": "https://bilwg.com/img/logo.png",
                    "url": "https://bilwg.com/img/logo.png"
                },
                {
                    "image": "https://bilwg.com/img/logo.png",
                    "url": "https://bilwg.com/img/logo.png"
                },
                {
                    "image": "https://bilwg.com/img/logo.png",
                    "url": "https://bilwg.com/img/logo.png"
                }
            ]
        }
    #data = data.json()
    return render(request,'user/dashboard.html', {'data': data, 'username': name, 'useremail': email})


