from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.forms import TextInput,FileInput,Select,EmailInput,PasswordInput
from django.contrib.auth.models import User

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        widgets = {
            'username' : TextInput(attrs={'class': 'input','placeholder':'Kullanıcı adınız'}),
            'email' : EmailInput(attrs={'class': 'input','placeholder':'Email girin.'}),
            'first_name' : TextInput(attrs={'class': 'input','placeholder':'İsminizi giriniz.'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'Soyisminizi giriniz.'})
        }
CITY = [
    ('Istanbul','Istanbul'),
    ('Ankara','Ankara'),
    ('Izmir','Izmir'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','address','city','country','image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Telefonunuzu giriniz..'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Adresinizi giriniz.'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'Şehrinizi giriniz.'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'Ülkenizi giriniz.'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'Fotoğrafınız .'})
        }