from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
# Create your views here.
from django.contrib.auth.models import User
from users.models import Profile
from users.form import ProfileForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid User and password'})
    return render(request, 'users/login.html') 

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password_confirmation!=password:
            return render(request, 'users/signup.html', {'error':"Password confirmation does not match"})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':"Useraname already exists"})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        profile = Profile(user=user)
        profile.save()
        return redirect("login") 
    return render(request, 'users/signup.html')

@login_required
def update_me_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            data= form.cleaned_data
            profile.website = data["website"]
            profile.phone_number = data["phone_number"]
            profile.bio = data["bio"]
            profile.website = data["website"]
            profile.picture = data["picture"]
            profile.save()
            return redirect("profile")
    else:
        form = ProfileForm()
    return render(
        request=request, 
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form,
        }
    )