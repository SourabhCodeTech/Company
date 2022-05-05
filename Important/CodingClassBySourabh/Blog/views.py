from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def blog(request):
    return render(request, 'Blogs.html')


def htmlTutorialInHindi(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        # if comment:
    return render(request, 'blogs/HTML-Tutorial.html')
