from django.contrib.auth import authenticate, login as auth_login

from django.shortcuts import render, redirect

from .models import User

# Create your views here.

# Create a login view

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.filter(email=email).first()
                     
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)

                return redirect('/')
            else:
                return render(request, 'account/login.html', {'error': 'User not found'})
            
        return redirect('list_app:index')
    
    
    
    return render(request, 'account/login.html')


# Create a signup view
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                return render(request, 'account/signup.html', {'error': 'Email is already taken'})
            else:
                user = User.objects.create_user(name=name, email=email, password=password1)
                user.save()
                return redirect('account:login')
        else:
            return render(request, 'account/signup.html', {'error': 'Passwords do not match'})
        
    return render(request, 'account/signup.html')