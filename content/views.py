from django.shortcuts import render,redirect
from django.views.generic import  ListView
from django.core.paginator import Paginator
from .models import Questions,Subjects

def home(request):
    questions_list = Questions.objects.filter(subject_id=1)
    subjects_list = Subjects.objects.all()
    selectedsub=1
    if request.method=='POST':
        selectedsub = request.POST["selectedsubject"]
        questions_list=Questions.objects.filter(subject_id=selectedsub)
    paginator = Paginator(questions_list,5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj,'subjects':subjects_list,'currsub':int(selectedsub)})

def search(request):
    if(request.method=='POST'):
        searchtext=request.POST["searchtext"]
        questionobj=Questions.objects.filter(question__icontains=searchtext)
        print(questionobj)
        return render(request,'search.html',{'items':questionobj})
    else:
        return render(request,'search.html')


