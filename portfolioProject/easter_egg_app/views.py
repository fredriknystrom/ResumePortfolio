from django.shortcuts import render

def cheese_and_mouse(request):
    return render(request, 'easter_egg_app/cheese_and_mouse.html')
