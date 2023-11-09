from django.shortcuts import render
import random

def ai_cube_view(request):
    return render(request, 'aicube_app/cube.html')

# Information Pages
def ai_view(request):
    context = {
        "heading" : "Foundations of AI",
        
    }
    return render(request, 'aicube_app/ai.html', context)

def ml_view(request):
    context = {
        "heading" : "Machine Learning",
        
    }
    return render(request, 'aicube_app/ml.html', context)

def nn_view(request):
    context = {
        "heading" : "Neural Networks",
        
    }
    return render(request, 'aicube_app/nn.html', context)

def nlp_view(request):
    context = {
        "heading" : "Natural Language Processing",
        
    }
    return render(request, 'aicube_app/nlp.html', context)

def rob_view(request):
    context = {
        "heading" : "Large Language Models",
        
    }
    return render(request, 'aicube_app/llm.html', context)

def cv_view(request):
    context = {
        "heading" : "Computer Vision",
        
    }
    return render(request, 'aicube_app/cv.html', context)
