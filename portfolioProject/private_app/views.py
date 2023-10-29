from django.shortcuts import render

def private_view(request):
    return render(request, 'private_app/base.html')

def terminal_view(request):
    return render(request, 'private_app/terminal.html')

def math_view(request):
    return render(request, 'private_app/math.html')