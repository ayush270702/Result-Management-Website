from cProfile import label
import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


from .models import Marks

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label = '',help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Email','class':'input'}))
    first_name = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'First name','class':'input'}))
    last_name = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Last name','class':'input'}))
    phone = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Phone','class':'input'}))
    organization = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Organization','class':'input'}))
    password1 = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Password','type':'password','class':'input', 'id':'myInput'}))
    check69 = forms.BooleanField(label='Show Password',widget= forms.CheckboxInput(attrs={'onclick':'myFunction()'}))
    password2 = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={'placeholder':'Confirm password','type':'password','class':'input'}))
    username = forms.CharField(max_length=200, label = '', help_text='Required',widget= forms.TextInput(attrs={  'placeholder':'Username','class':'input'}))
    CHOICES = [('Male','Male'),('Female','Female')]

    CHOICES1 = [('teacher','teacher'), ('student', 'student')]

    CHOICES2 = [('A','A'), ('B', 'B')]
    

    
    div=forms.CharField(label='Division', widget=forms.RadioSelect(choices=CHOICES2), required=False)
    faculty=forms.CharField(label='Register as', widget=forms.RadioSelect(choices=CHOICES1,attrs={'class':'input2'}))

    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES,attrs={'class':'input2'}))


    # gender = forms.ChoiceField(choices=(("Male","Male"),("Female", "Female")), widget=forms.RadioSelect(attrs={"label":"Gender"}))
    # gender = forms.ChoiceField(label='gender',widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model=User
        fields = ('first_name','last_name','username','email','organization','phone','password1','check69', 'password2','gender','faculty')

class OrderForm(ModelForm):
    sub1 = forms.IntegerField(label='Suject1',widget= forms.TextInput(attrs={'class':''}))
    sub2 = forms.IntegerField(label='Suject2',widget= forms.TextInput(attrs={'class':''}))
    sub3 = forms.IntegerField(label='Suject3',widget= forms.TextInput(attrs={'class':''}))
    class Meta:
        model = Marks
        fields = ('sub1', 'sub2', 'sub3')