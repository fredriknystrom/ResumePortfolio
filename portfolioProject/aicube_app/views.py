from django.shortcuts import render

def ai_cube_view(request):
    return render(request, 'aicube_app/base.html')
