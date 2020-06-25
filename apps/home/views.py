from django.shortcuts import render

# Create your views here.

def page_not_found(request,exception,template_name='home/404_error.html'):
    return render(request, 'home/404_error.html')


def test(request,template_name='home/404_error.html'):
    return render(request, 'home/404_error.html')