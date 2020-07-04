from django.shortcuts import render,redirect,HttpResponse
import requests
from user.views import userAuth
# Create your views here.

def tournamentDetail(request):
    if request.COOKIES.get('user', None) == None:
        return redirect(userAuth)
    res = requests.post('http://api.e-sportsindia.in/user/tournament/single',json={'id':1,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
    data = res.json()
    print(data)
    data= data['data'] 
    teamMembers = data['registration']
    startDate = data['startDate']
    startDate=startDate[0:10]
    noOfPlayers=teamMembers['totalPlayers']
    print(noOfPlayers)
    phone = request.COOKIES['user']
    user= requests.post('http://api.e-sportsindia.in/user/data',json={'phone':phone,'token':"11712f60-942d-49ff-b026-139dca2e0a39"})
    user = user.json()
    print(user)
    uid= user['data']['id']
    if noOfPlayers == 4:
        list = ['1','2','3']
    elif noOfPlayers == 5:
        list = ['1','2','3','4']
    elif noOfPlayers == 6:
        list = ['1','2','3','4','5']
    
    if request.method == "POST":
        f = request.POST
        
        
        """dataJson = {
            "tournamentID" : "f['tournamentID']",
            "userID" : "f['userID']",
            "teamName": "f['teamName']", 
            "teamCountry" : "f['teamCountry']",
            "teamLogo" :  "avitry",
            "teamNumber" : "f['teamNumber']", 
            "teamEmail" : "f['teamEmail']", 
            "iglIGN" : "f['iglIGN']", 
            "iglCharID" : "f['iglCharID']",
            "iglCountry" :teamCountry, 
            "iglEmail" : teamEmail, 
            "iglDiscord" : iglDiscord, 
            "ilgNumber" : teamNumber, 
            "iglRealName" :iglRealName, 
            "player1IGN" :f['player1IGN'], 
            "player1CharID" :f['player1CharID'], 
            "player1Email" : player1Email,
            "player1Number" :player1Number,
            "player1Discord" :player1Discord,
            "player1Country" :player1Country, 
            "player1RealName" :player1RealName, 
            "player2IGN" : f['player2IGN'], 
            "player2CharID" : f['player2CharID'], 
            "player2Email" : player2Email,
            "player2Number" : player2Number, 
            "player2Discord" :player2Discord, 
            "player2Country" : player2Country, 
            "player2RealName" : player2RealName, 
            "player3IGN" : f['player3IGN'], 
            "player3CharID" : f['player3CharID'], 
            "player3Email" : player3Email, 
            "player3Number" : player3Number, 
            "player3Discord" : player3Discord, 
            "player3Country" : player3Country, 
            "player3RealName" : player3RealName, 
            "player4IGN" : f['player4IGN'], 
            "player4CharID":f['player4CharID'], 
            "player4Email" : player4Email, 
            "player4Number" : player4Number, 
            "player4Discord" : player4Discord, 
            "player4RealName" : player4RealName,
            "player4Country" :player4Country,
            "player5IGN" : f['player5IGN'], 
            "player5CharID" :f['player5CharID'], 
            "player5Email": player5Email,
            "player5Number": player5Number,
            "player5Discord": player5Discord, 
            "player5RealName":player5RealName,
            "player5Country":player5Country,
            'token':"11712f60-942d-49ff-b026-139dca2e0a39"
        }"""       


        if not f['teamCountry']:
            teamCountry = ""
        else:
            teamCountry = f['teamCountry']
        

        if not f['teamNumber']:
            teamNumber = ""
        else: 
            teamNumber = f['teamNumber']
        

        if not f['teamEmail']: 
            teamEmail = ""
        else:
            teamEmail = f['teamEmail']
        

        if not f['iglDiscord']:
            iglDiscord = ""
        else:
            iglDiscord = f['iglDiscord']
        
        if not f['iglRealName']:
            iglRealName = ""
        else:
            iglRealName = f['iglRealName']
        
        if not f['player1Discord']:
            player1Discord = ""
        else:
            player1Discord = f['player1Discord']

        if not f['player1Email']:
            player1Email = ""
        else:
            player1Email = f['player1Email']

        if not f['player1Number']:
            player1Number = ""
        else:
            player1Number = f['player1Number']
        
        if not f['player1Country']:
            player1Country = ""
        else:
            player1Country = f['player1Country']
        
        if not f['player1RealName']:
            player1RealName = ""
        else:
            player1RealName = f['player1RealName']

        if not f['player2Discord']:
            player2Discord = ""
        else:
            player2Discord = f['player2Discord']

        if not f['player2Email']:
            player2Email = ""
        else:
            player2Email = f['player2Email']
        
        if not f['player2Number']:
            player2Number = ""
        else:
            player2Number = f['player2Number']

        if not f['player2Country']:
            player2Country = ""
        else:
            player2Country = f['player2Country']

        if not f['player2RealName']:
            player2RealName = ""
        else:
            player2RealName = f['player2RealName']

        if not f['player3Discord']:
            player3Discord = ""
        else:
            player3Discord = f['player3Discord']

        if not f['player3Email']:
            player3Email = ""
        else:
            player3Email = f['player3Email']

        if not f['player3Number']:
            player3Number = ""
        else:
            player3Number = f['player3Number']

        if not f['player3Country']:
            player3Country = ""
        else:
            player3Country = f['player3Country']

        if not f['player3RealName']:
            player3RealName = ""
        else:
            player3RealName = f['player3RealName']

        if not f['player4Discord']:
            player4Discord = ""
        else:
            player4Discord = f['player4Discord']

        if not f['player4Email']:
            player4Email = ""
        else:
            player4Email = f['player4Email']

        if not f['player4Number']:
            player4Number = ""
        else:
            player4Number = f['player4Number']

        if not f['player4Country']:
            player4Country = ""
        else:
            player4Country = f['player4Country']

        if not f['player4RealName']:
            player4RealName = ""
        else:
            player4RealName = f['player4RealName']

        if not f['player5Discord']:
            player5Discord = ""
        else:
            player5Discord = f['player5Discord']

        if not  f['player5Email']:
            player5Email = ""
        else:
            player5Email = f['player5Email']

        if not f['player5Number']:
            player5Number = ""
        else:
            player5Number = f['player5Number']

        if not f['player5Country']:
            player5Country = ""
        else:
            player5Country = f['player5Country']

        if not f['player5RealName']:
            player5RealName = ""
        else:
            player5RealName = f['player5RealName']
        

          

        response = requests.post('http://api.e-sportsindia.in/user/tournament/register/',  json = {
            "tournamentID" : f['tournamentID'],
            "userID" : f['userID'],
            "teamName": f['teamName'], 
            "teamCountry" : f['teamCountry'],
            "teamLogo" :  "avitry",
            "teamNumber" : f['teamNumber'], 
            "teamEmail" : f['teamEmail'], 
            "iglIGN" : f['iglIGN'], 
            "iglCharID" : f['iglCharID'],
            "iglCountry" :teamCountry, 
            "iglEmail" : teamEmail, 
            "iglDiscord" : iglDiscord, 
            "ilgNumber" : teamNumber, 
            "iglRealName" :iglRealName, 
            "player1IGN" :f['player1IGN'], 
            "player1CharID" :f['player1CharID'], 
            "player1Email" : player1Email,
            "player1Number" :player1Number,
            "player1Discord" :player1Discord,
            "player1Country" :player1Country, 
            "player1RealName" :player1RealName, 
            "player2IGN" : f['player2IGN'], 
            "player2CharID" : f['player2CharID'], 
            "player2Email" : player2Email,
            "player2Number" : player2Number, 
            "player2Discord" :player2Discord, 
            "player2Country" : player2Country, 
            "player2RealName" : player2RealName, 
            "player3IGN" : f['player3IGN'], 
            "player3CharID" : f['player3CharID'], 
            "player3Email" : player3Email, 
            "player3Number" : player3Number, 
            "player3Discord" : player3Discord, 
            "player3Country" : player3Country, 
            "player3RealName" : player3RealName, 
            "player4IGN" : f['player4IGN'], 
            "player4CharID":f['player4CharID'], 
            "player4Email" : player4Email, 
            "player4Number" : player4Number, 
            "player4Discord" : player4Discord, 
            "player4RealName" : player4RealName,
            "player4Country" :player4Country,
            "player5IGN" : f['player5IGN'], 
            "player5CharID" :f['player5CharID'], 
            "player5Email": player5Email,
            "player5Number": player5Number,
            "player5Discord": player5Discord, 
            "player5RealName":player5RealName,
            "player5Country":player5Country,
            'token':"11712f60-942d-49ff-b026-139dca2e0a39"
        })
        print(response.headers['content-type'])
        print(response.text)
        if response.status_code==200:
            res = response.json()
            if res['desc'] =="Team Registed": 
               return redirect(tournamentDetail)
        else:
            return HttpResponse("Not worked")
    else:
        return render(request,'tournament/tournamentDetail.html',{'data':data,'teamMembers':teamMembers,'startDate':startDate, 'list':list,'uid':uid})



