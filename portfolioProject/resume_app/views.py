from django.shortcuts import render
from django.http import HttpResponse

def resume_view(request):
    return HttpResponse("This is my resume")