from django.http import HttpResponse


# from django.shortcuts import render


# Create your views here.


def home_page(request):
    # return render(request, 'home_page.html')
    return HttpResponse("This is HomePage. Welcome!")