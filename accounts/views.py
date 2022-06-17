import random
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib import auth
from .models import Marks, Profile, Student, Teacher
from django.template.loader import render_to_string
from .forms import OrderForm
from django.urls import reverse

def home(request):
    return render(request, 'accounts/home.html')

def rand1():
    list1 = {"git":"https://github.com/ayush270702","link":"https://www.linkedin.com/in/ayush-shende-317589208/"}
    list2 = {"git":"https://github.com/sid-3q5","link":"https://www.linkedin.com/in/siddhant-chauhan-4614041b9/"}
    list3 = [ list1, list2]
    return random.choice(list3)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate account'
            message = render_to_string('accounts/acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'f': rand1(),
                'domain':"{0}".format("http://127.0.0.1:8000"),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage( mail_subject,message,to=[to_email])
            email.content_subtype = 'html'
            
            email.mixed_subtype = 'related'


            email.send()



            organization = form.cleaned_data.get('organization')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            faculty = form.cleaned_data.get('faculty')
            div = form.cleaned_data.get('div')
            fname = form.cleaned_data.get('first_name')
            profile = Profile.objects.create(user=user, phone=phone, organization=organization, gender=gender, faculty=faculty, div=div)
            if faculty == 'teacher':
                teacher = Teacher.objects.create(teacher=user)
            elif faculty == 'student':
                student = Student.objects.create(student=user, fname=fname)
                marks = Marks.objects.create(stud=student)

            
            

            # return HttpResponse('please confirm your mail')
            return render(request,'accounts/confirm.html')
    else:
        form = SignupForm()   
    return render(request,'accounts/signup.html',{'form':form})


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('login')
    else:  
        return HttpResponse('Activation link is invalid!')      



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        profile = Profile.objects.get(user=user)
        if user is not None:
            if profile.faculty == "student":
                auth.login(request, user)
                pk = request.user.id
                return redirect(f"stud_profile/{request.user.id}/")
            elif profile.faculty == "teacher":
                auth.login(request, user)
                pk = request.user.id
                return redirect(f"teacher_profile/{request.user.id}/")

        else:
            context = {'error': True}
            return render(request, 'accounts/login.html',context)  
    return render(request, 'accounts/login.html')  


def stud_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        profile = Profile.objects.get(user=user)
        if user is not None:
            if profile.faculty == "student":
                auth.login(request, user)
                pk = request.user.id
                return redirect(f"stud_profile/{request.user.id}/")
            else:
                context = {'error': "only for student"}
            return render(request, 'accounts/login.html',context) 
        else:
            context = {'error': True}
            return render(request, 'accounts/login.html',context)  
    return render(request, 'accounts/login.html')       


def teach_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        profile = Profile.objects.get(user=user)
        if user is not None:
            if profile.faculty == "teacher":
                auth.login(request, user)
                pk = request.user.id
                return redirect(f"teacher_profile/{request.user.id}/")
            else:
                e="only for teacher"
                context = {'error': e}
            return render(request, 'accounts/login.html',context) 
        else:
            context = {'error': True}
            return render(request, 'accounts/login.html',context)  
    return render(request, 'accounts/login.html') 


def stud_profile(request ,pk):
    if  request.user.is_authenticated:
        student = User.objects.get( pk=pk)
        profile = Profile.objects.get(user=student)
        stud = Student.objects.get(student=student)
        marks = Marks.objects.get(stud=stud)
        context={"student":student, "profile":profile, "marks":marks}
        return render(request, 'accounts/stud_profile.html', context)
    else:
        return redirect("login")    

def teacher_profile(request ,pk):
    if  request.user.is_authenticated:
        teacher = User.objects.get( pk=pk)
        profile = Profile.objects.get(user=teacher)
        l = Student.objects.values_list('student_id')
        c = Student.objects.count()
        # marks = Marks.objects.get(stud=s)
        stud = User.objects.all()
        pr = Profile.objects.all()
        # stud_prof = Profile.objects.get(user=stud)
        du = zip(pr,stud)

        a = Profile.objects.filter(div="A").count()
        b = Profile.objects.filter(div="B").count()

        # a = request.POST['next']
        # print(a)
        context={"teacher":teacher, "profile":profile,  "du":du, "a":a, "b":b}
        return render(request, 'accounts/teacher.html', context)

    else:
        return redirect("login")   

def logout(request):
    auth.logout(request)
    return redirect("/") 


def test(request,pk):
    if  request.user.is_authenticated:
        student = User.objects.get( pk=pk)
        profile = Profile.objects.get(user=student)
        stud = Student.objects.get(student=student)
        marks = Marks.objects.get(stud=stud)
        form = OrderForm(instance=marks)
        context={"student":student, "profile":profile, "form":form}

        if request.method == "POST":
            form = OrderForm(request.POST, instance=marks)
            if form.is_valid:
                form.save()
                
                return HttpResponseRedirect(reverse('div', args=[profile.div]))
                

        return render(request, 'accounts/mark_form.html', context)    
    else:
        return redirect("login")      

def div(request, div):
    if  request.user.is_authenticated:
        student = Student.objects.all()
        profile = Profile.objects.filter(div=div)
        t = zip(student,profile)
        context = {'student':student, 'profile':profile, 't':t}

        return render(request, 'accounts/div.html', context)
    else:
        return redirect("login")  
        
def profile1(request,pk):
    if  request.user.is_authenticated:
        teacher = User.objects.get( pk=pk)
        profile = Profile.objects.get(user=teacher)
        l = Student.objects.values_list('student_id')
        c = Student.objects.count()
        # marks = Marks.objects.get(stud=s)
        stud = User.objects.all()
        pr = Profile.objects.all()
        # stud_prof = Profile.objects.get(user=stud)
        du = zip(pr,stud)
        # a = request.POST['next']
        # print(a)
        context={"teacher":teacher, "profile":profile,  "du":du}
    return render(request, 'accounts/prof1.html',context)
