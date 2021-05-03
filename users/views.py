from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from users.form import ProfileForm, SignUpForm
from django.contrib.auth.models import User

class UserDetailView(LoginRequiredMixin,DetailView):
    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid User and password'})
    return render(request, 'users/login.html') 

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        else:
            print(form.errors)
            return render(
                request=request, 
                template_name='users/signup.html', 
                context={
                    'form': form,
                }
            )
    else:
        form = SignUpForm()   
    return render(
        request=request, 
        template_name='users/signup.html',
        context={
            'form': form,
        }
    )

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
            profile.picture = data["picture"]
            profile.save()
            url = reverse("users:detail",kwargs={'username:detail': request.user.username})
            return redirect(url)
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