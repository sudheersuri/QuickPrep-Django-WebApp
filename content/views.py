from django.shortcuts import render
from django.views.generic import  ListView
from .models import Questions,Subjects

# Create your views here.
class QuestionsListView(ListView):
    model = Questions
    template_name = 'home.html' 
    context_object_name = 'items'
    paginate_by = 5
