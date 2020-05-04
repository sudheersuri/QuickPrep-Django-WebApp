from django.shortcuts import render,redirect
from .models import Status

# Create your views here.
def home(request):
    items=Status.objects.all().order_by('date_posted')
    items.totallikes=items.totallikes()
    return render(request,'home.html',{'items':items})

def likestatus(request):
    print(request.POST['likebtn'])
    statusobj=Status.objects.get(id=request.POST.get('likebtn',False))
    if(statusobj.likes.filter(id=request.user.id).exists()):
        statusobj.likes.remove(request.user)
    else:
        statusobj.likes.add(request.user)
    return redirect('home')