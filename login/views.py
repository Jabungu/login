from django.shortcuts import render, HttpResponse, redirect
from login.models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def registration(request):
    return render(request, 'register.html')
def addUser(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        print("this is where userpic should be")
        print(request.POST.get('image'))
        newuser= User.objects.create(username = request.POST['username'], first_name = request.POST['firstName'], last_name = request.POST["lastName"], Email=request.POST["email"], password=pw_hash, Address_Line_1= request.POST['ad1'], Address_Line_2 = request.POST['ad2'], City = request.POST['city'], State = request.POST['state'], Zip = request.POST['zip'], Country = request.POST['country'], image=request.POST.get('image'))
        request.session['id'] = newuser.userId
        request.session['registered_user']= newuser.username
        return redirect("/")
def login(request):
    return render(request, 'login.html')
def passwordReset(request):
    return render(request, 'pwdreset.html')
def pwResetEmail(request):
    return render(request, 'pwdResetEmail.html')
def emailSent(request):
    return render(request, 'emailSent.html')
def authentication(request):
    user = User.objects.filter(username = request.POST['username'])
    errors = User.objects.login_validator(request.POST)
    if user:
        logged_user = user[0]
        print ("username found")
    else:
        print("username not found")
        return redirect('/login')   

    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session['id'] = logged_user.userId
        print("The user ID is below:")
        print (request.session["id"])
        return redirect('/verified')   
    else:
        password_incorrect = "Incorrect password. Please try again."
        print(password_incorrect)
        
        if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # HOMEWORK: Add password and username error message, add login with email capability
    return redirect('/login')
def home(request):
    return render(request, 'home.html')
def logout(request):
    request.session.clear
    return render(request, "login.html")
