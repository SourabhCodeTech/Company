from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            if fname and lname and email and password and cpassword:
                if cpassword != password:
                    messages.success(
                        request, "Password Doesn't Match!")
                    return redirect("signup")
                else:
                    user = User.objects.create_user(username, email, password)
                    user.first_name = fname
                    user.last_name = lname
                    user.save()
                    if user:
                        messages.success(request, "Account Has Created")
                        return redirect("login")
        return render(request, 'signup.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.warning(request, "First Create Your Account")
                return redirect("login")
        return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect("home")


def myprofile(request):
    if request.user.is_authenticated:
        return render(request, 'myprofile.html')
    else:
        return redirect("signup")
