from django.shortcuts import render,redirect
from .forms import CreateEducatorForm
from django.contrib.auth import authenticate, login
from .models import Developer
from django.contrib.auth.hashers import make_password,check_password 
# Create your views here.
def signup(request):
    if request.method=='GET':
        form = CreateEducatorForm()
        context={
            
            'form':form
        }
        return render(request,'signup.html',context)
    
    else:
        form=CreateEducatorForm(request.POST)
        if form.is_valid():
            # Save the CustomUser instance
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            password=form.cleaned_data['password']
            
            institute=form.cleaned_data['institute']
            
            user=Developer(username=username,email=email,phone=phone,password=password,institute=institute)
            user.save()
            
            return render(request,'home.html')
                
def login_view(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        user_data=request.POST
        error_msg=""
        password=user_data.get('password')
        email=user_data.get('email')
        user=Developer.objects.get(email=email,password=password)
        
        print(user)
        if user:
            login(request,user)
            return redirect("dashboard")
        else:
            error_msg="wrong email or password"
        
        return render(request, 'login.html', {'error': error_msg})