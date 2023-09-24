from django.shortcuts import render,redirect,get_object_or_404
from .forms import CurriculumnForm
from django.contrib import messages
from register.models import customuser,Developer
from .models import Curriculumn

from django.shortcuts import render
from django.http import HttpResponse
from .connect_api import main as google_calendar_main
# Create your views here.
def developerpanel(request):
    if request.method=="POST":
        form=CurriculumnForm(request.POST)
        if form.is_valid():
            
            body=form.cleaned_data['body']
            user_email=request.session.get('user_email')
            user=customuser.objects.get(email=user_email)
            curriculumn=Curriculumn(body=body)
            curriculumn.save()
            curriculumn.user.add(user)
            print(curriculumn)
            return redirect('/')      
    form=CurriculumnForm()
    curriculumn=get_object_or_404(Curriculumn,id=16)
    form=CurriculumnForm(instance=curriculumn)
    return render(request,'developerpanel.html',{'form':form})

def index(request):
    return render (request,'home.html')


def integrate_with_google_calendar(request):
    if request.method=="GET":
        google_calendar_main()
        return redirect("developerpanel")
    
def dashboard(request):
    if request.method=="GET":
        return render(request,'developer_dahboard.html')