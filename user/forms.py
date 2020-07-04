from django import forms

class userRegisterForm(forms.Form):
    phone = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class' : 'myfieldclass','placeholder':'+91 7021915752'}),label='')


class userLoginForm(forms.Form):
    phone = forms.CharField(max_length=10)

class userOtpForm(forms.Form):
    otp = forms.CharField(max_length=6,widget=forms.TextInput(attrs={'class' : 'myfieldclass','placeholder':'Enter Otp'}),label='')

class userRegForm(forms.Form):
    name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class' : 'myfieldclass','placeholder':'Your Name'}),label='')
    email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={'class' : 'myfieldclass','placeholder':'Your Email'}),label='')
#let me try

#   myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))


class ScrimsForm(forms.Form):
    teamName = forms.CharField(widget=forms.TextInput(attrs={'class':'imgg','placeholder':'Team Name'}),label='')
    iglName =forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'igl Name'}),label='')
    iglCharId = forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'igl CharID'}),label='')
    player1Name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'Player1 Name'}),label='')
    player1CharId = forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'Player1 CharID'}),label='')
    player2Name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'Player2 Name'}),label='')
    player2CharId = forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'Player2 CharID'}),label='')
    player3Name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'Player3 Name'}),label='')
    player3CharId = forms.CharField(widget=forms.TextInput(attrs={'class' : 'imgg','placeholder':'Player3 CharID'}),label='')