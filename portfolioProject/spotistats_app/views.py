from django.shortcuts import render
from django.http import HttpResponse

def spotistats_view(request):
    return HttpResponse("This is my spotistats")
