from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms


class UserRegisterForm(UserCreationForm):
    User._meta.get_field('email')._unique = True
    email=forms.EmailField(max_length=75)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

def register(request):
    if(request.method=='POST'):
        userobj=User.objects.filter(email=request.POST["email"])
        print(userobj)
        form=UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})