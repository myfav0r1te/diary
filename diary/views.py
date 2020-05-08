from django.shortcuts import render
from .models import Diary

def home(request):
    diarys = Diary.objects
    return render(request, 'home.html', {'diarys' : diarys})
