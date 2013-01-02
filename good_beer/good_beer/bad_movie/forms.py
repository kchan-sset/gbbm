from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models.signals import post_save

from good_beer.bad_movie.models import create_user_profile

class RegForm(forms.ModelForm):
    #CREATING CUSTOMIZED FORM FIELDS
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
            ),
        label='Password',
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
            ),
        label='Confirm Password',
        required=True
    )
    
    #using the User object to create the other form fields
    class Meta:
        model = User
        #SETTING THE ORDER OF FORM FIELDS
        #DON'T NEED TO put the password fields since they will be
        #appended to the end of the fields list
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    #validating the fields by calling clean_<fieldname>    
    def clean_username(self):
        #fetch the cleaned for data for the username field
        c_username = self.cleaned_data['username']
        try:
            User.objects.get(username=c_username)
        except User.DoesNotExist:
            return c_username
        raise validators.ValidationError("The username %s has already been taken." % c_username)
            
    def clean_password2(self):
        pw1 = self.cleaned_data['password1']
        pw2 = self.cleaned_data['password2']
        
        if pw1 != pw2:
            raise validators.ValidationError("Password values don't match")
        
        return pw2
            
    def save(self):
        user = super(RegForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        
        return user
        