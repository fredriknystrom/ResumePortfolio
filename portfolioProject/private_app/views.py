from django.shortcuts import render

def terminal_view(request):
    return render(request, 'private_app/terminal.html')