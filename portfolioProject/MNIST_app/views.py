from django.shortcuts import render

from django.http import HttpResponse

def mnist_view(request):
    return HttpResponse("This is my MNIST")
