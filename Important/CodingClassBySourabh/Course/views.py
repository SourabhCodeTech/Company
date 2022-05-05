from django.shortcuts import redirect, render

# Create your views here.


def course(request):
    if request.user.is_authenticated:
        return render(request, 'Course.html')
    else:
        return redirect('signup')


def random_password_generator(request):
    if request.user.is_authenticated:
        return render(request, 'courses/pythonproject/RandomPasswordGenerator.html')
