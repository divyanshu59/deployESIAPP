from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
import requests
import json
from user.forms import ScrimsForm
from django.urls import reverse
from datetime import date
from django.core.files.images import ImageFile


# Create your views here.

def home(request):
    return redirect('/user/auth/')


def Profile(request):
    if request.COOKIES.get('user', None) == None:
        return redirect('/user/auth/')
    if request.method =="POST":
        userForm = request.POST
        username=userForm['username']
        email=userForm['email']
        userid=userForm['id']
        profileimg=userForm['profileimg']

        
        if bool(request.FILES.get('profile', False)) == True:
            profile = ImageFile(request.FILES['profile'])
            print(profile)
            profilePic = requests.post('http://api.e-sportsindia.in/user/upload/img', data = {
                'token':"11712f60-942d-49ff-b026-139dca2e0a39",
                'image':profile
            }, headers = { "Content-Type": "application/x-www-form-urlencoded"})

            print(profilePic.headers['content-type'])
            if profilePic.status_code==200:
                res = profilePic.json()
                url = res['url']
                updateInfo = requests.post('http://api.e-sportsindia.in/user/profile/edit',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39",'name':username,'email':email,'profile':url})
                updateInfo = updateInfo.json()
                print(updateInfo)
                return render(request,'user/profile.html')
            else:
                #print(profilePic.text)
                return HttpResponse(profilePic.text)
        else:
            updateInfo = requests.post('http://api.e-sportsindia.in/user/profile/edit',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39",'name':username,'email':email,'profile':profileimg, 'id': userid})
            updateInfo = updateInfo.json()
            print(updateInfo)
            return redirect('/user/profiles/')
    else:
        phone = request.COOKIES['user']
        phone = int(phone)
        response = requests.post('http://api.e-sportsindia.in/user/data/', json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
        if response.status_code ==200:
            data = response.json()
            #print(data)
            renewDate=data['data']['subdata']['reNewDate']
            renewDate = renewDate[0:10]
            email = data['data']['email']
            name  = data['data']['name']
            return render(request,'user/profile.html',{'data':data,'renewDate':renewDate, 'username': name, 'useremail': email})
        else:
            return HttpResponse("User Denied!")
        

         
def notifications(request):
    if request.COOKIES.get('user', None) == None:
        return redirect('/user/auth/')
    phone = request.COOKIES['user']
    phone = int(phone)
    userData = requests.post('http://api.e-sportsindia.in/user/data/',json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
    uid = userData.json()
    uid=uid['data']['id']
    print(uid)
    res = requests.post('http://api.e-sportsindia.in/user/notification/',json={'id':uid,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
    notify = res.json()
    print(notify)
    phone = request.COOKIES['user']
    phone = int(phone)
    response = requests.post('http://api.e-sportsindia.in/user/data/', json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
    if response.status_code ==200:
        data = response.json()
       
        email = data['data']['email']
        name  = data['data']['name']
        print(email)
    if notify['error'] == True:
        desc = notify['desc']
        return render(request,'user/notifications.html',{'desc':desc , 'username': name, 'useremail': email})
    else:
        notify = notify['data']
        return render(request,'user/notifications.html',{'notify':notify, 'username': name, 'useremail': email})



def rankings(request):
    data = requests.post('http://api.e-sportsindia.in/user/rank/week/current/',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39","group":"E1"})
    data = data.json()
    data = data['data']
    data1 = requests.post('http://api.e-sportsindia.in/user/rank/month/current/',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39","group":"E1"})
    data1 = data1.json()
    data1 = data1['data']
    phone = request.COOKIES['user']
    phone = int(phone)
    response = requests.post('http://api.e-sportsindia.in/user/data/', json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
    if response.status_code ==200:
        data = response.json()
        email = data['data']['email']
        name  = data['data']['name']
    return render(request,'user/rankings.html',{'month':data1,'week':data, 'username': name, 'useremail': email})




#API_KEY ="4ad9e2d0d832d87744cb6119c593f354"

#AUTH_TOKEN = "565034e56d4d3513139d284a8f28695d"

#api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://instamojo.com/api/1.1/')

def practiceScrims(request):
    if request.COOKIES.get('user', None) == None:
        return redirect('/user/auth/')
    if request.method == "POST":
        form = ScrimsForm(request.POST)
        uid = request.COOKIES['user'];
        if form.is_valid():

            usercurr = requests.post('http://api.e-sportsindia.in/user/current/',json={"uid":uid,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
            userData = usercurr.json()
            #print(userData)
            month = userData[0]['month']
            year = userData[0]['year']
            cost = userData[0]['cost']
            renew = userData[0]['renew']
            selled = userData[0]['selled']
            planid = userData[0]['id']
            totalTeam = userData[0]['totalTeam']
            today = date.today()

            
            data = form.cleaned_data
            teamName = data['teamName']
            iglName = data['iglName']
            iglCharId = data['iglCharId']
            player1Name = data['player1Name']
            player1CharId = data['player1CharId']
            player2Name = data['player2Name']
            player2CharId = data['player2CharId']
            player3Name = data['player3Name']
            player3CharId = data['player3CharId']
            uid = request.COOKIES['user']
            uid = int(uid)

            user = requests.post('http://api.e-sportsindia.in/user/data/',json={'phone':uid,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
            uID = user.json()
           
            userid=uID['data']['id']
            uEmail = uID['data']['email']
            
            if selled < totalTeam:
                usersplus = requests.post('http://api.e-sportsindia.in/user/splus/new/',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39",
                'planid':planid,'userid':userid,'month':month,'year':year,'amount':cost,
                'teamname':teamName,'igl':iglName,'buydate':'today',
                'iglid':iglCharId,'player1':player1Name,'player1id':player1CharId,
                'player2':player2Name,'player2id':player2CharId,
                'player3':player3Name,'player3id':player3CharId
                })
                userplusans = usersplus.json()
                
                selled += 1
                usersplusupdate = requests.post('http://api.e-sportsindia.in/user/splus/update',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39",'planid':planid,'month':month ,'userid':userid, 'year':year,'payed':1})
                usercurrupdate = requests.post('http://api.e-sportsindia.in/user/current/update',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39",'planid':planid})
                print(usercurrupdate.json())
                return redirect('/user/practiceScrims/')
            else:
                return render(request, 'user/practiceScrimsNoSlot.html')

    else:
        phone = request.COOKIES['user']
        phone = int(phone)
        response = requests.post('http://api.e-sportsindia.in/user/data/', json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
        if response.status_code ==200:
            data = response.json()
            email = data['data']['email']
            name  = data['data']['name']
        phone = request.COOKIES['user'];
        checkplan = requests.post('http://api.e-sportsindia.in/user/splus/check',json={'token':"11712f60-942d-49ff-b026-139dca2e0a39",'phone':phone})
        checkplan =  checkplan.json()
        if checkplan['error'] == True:
            form = ScrimsForm()
            return render(request,'user/practiceScrims.html',{'form':form, 'username': name, 'useremail': email})
        else:
            return render(request,'user/practiceScrimsregistred.html', {'username': name, 'useremail': email})



def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('user')
    return response



