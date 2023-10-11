from django.shortcuts import render
from django.http import HttpResponse

def resume_view(request):
    return render(request, 'resume_app/resume.html')