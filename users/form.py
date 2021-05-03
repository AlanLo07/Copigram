from django import forms
from django.contrib.auth.models import User
from users.models import Profile
class SignUpForm(forms.Form):
    usernaname = forms.CharField(max_length=50,min_length=5,)
    password = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput()
    )
    first_name = forms.CharField(max_length=50,min_length=2,)
    last_name = forms.CharField(max_length=50,min_length=2,)
    email = forms.CharField(
        max_length=70,
        min_length=6,
        widget=forms.EmailInput(),
    )

    def clean_user(self):
        username=self.cleaned_data['username']
        username_query = User.objects.filter(username=username).exists()
        if username_query:
            raise forms.ValidationError('Username is already in use')
        return username
    
    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password_confirmation!=password:
            raise forms.ValidationError('Password do not match')
        return data

    def safe(self):
        data = self.cleaned_data
        data.pop("password_confirmation")
        user= User.objects.create_user(**data)
        profile= Profile(user=user,)
        profile.save()
class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200,required=True)
    bio = forms.CharField(max_length=500,required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()