from django.shortcuts import render,redirect,get_object_or_404
from .forms import CurriculumnForm
from django.contrib import messages
from register.models import Developer
from .models import Curriculumn,Message
from pyeditorjs import EditorJsParser
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .connect_api import main as google_calendar_main
# Create your views here.
def developerpanel(request):
    if request.method=="POST":
        form=CurriculumnForm(request.POST)
        if form.is_valid():
            
            body=form.cleaned_data['body']
            parser = EditorJsParser(body) # initialize the parser
            
            user_email=request.user.email
            user=Developer.objects.get(email=user_email)
            curriculumn=Curriculumn(body=body)
            curriculumn.save()
            curriculumn.user.add(user)
            print(curriculumn)
            return redirect('/dashboard/develop/')      
    form=CurriculumnForm()
    
    curriculumn=get_object_or_404(Curriculumn,id=1)
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
        user=request.user
        user_friends=user.friends.all()
        return render(request,'dahboard.html',{'user':user})

def getmsgs(request,senderid,recieverid):
     
    if request.method=="GET":
        
        if int(senderid) > int(recieverid):
            room_name = f'{senderid}-{recieverid}'
        else:
            room_name = f'{recieverid}-{senderid}'

        room_group_name = 'chat_%s' % room_name
        msgs=Message.objects.filter(thread_name=room_group_name).order_by('timestamp')
        msg_list= list(msgs.values())
        return JsonResponse({'msg_list':msg_list,'status':'msg sent'})

