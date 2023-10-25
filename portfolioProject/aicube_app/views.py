from django.shortcuts import render
import random

def ai_cube_view(request):
    return render(request, 'aicube_app/cube.html')

# Information Pages
def ai_view(request):
    context = {
        "heading" : "Foundations of AI",
        "quote" : gen_quote()
    }
    return render(request, 'aicube_app/ai.html', context)

def ml_view(request):
    context = {
        "heading" : "Machine Learning",
        "quote" : gen_quote()
    }
    return render(request, 'aicube_app/ml.html', context)

def nn_view(request):
    context = {
        "heading" : "Neural Networks",
        "quote" : gen_quote()
    }
    return render(request, 'aicube_app/nn.html', context)

def nlp_view(request):
    context = {
        "heading" : "Natural Language Processing & Large Lanugage Models",
        "quote" : gen_quote()
    }
    return render(request, 'aicube_app/nlp.html', context)

def cv_view(request):
    context = {
        "heading" : "Computer Vision",
        "quote" : gen_quote()
    }
    return render(request, 'aicube_app/cv.html', context)

def rob_view(request):
    context = {
        "heading" : "Robotics",
        "quote" : gen_quote()
    }
    return render(request, 'aicube_app/rob.html', context)

def gen_quote():
    # List of AI quotes
    ai_quotes = [
        "The future is here with AI.",
        "AI is the new electricity.",
        "Machine learning is the way forward.",
        "AI will change the world as we know it.",
        "Artificial intelligence is the future of technology.",
        "Deep learning is revolutionizing AI.",
    ]

    return random.choice(ai_quotes)