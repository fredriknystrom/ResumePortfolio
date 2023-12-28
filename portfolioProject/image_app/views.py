from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

# Import necessary libraries
import os
import json


def upload_image(request):
    
    if request.method == 'POST':
        context = {
            'image': "test post"
        }
        return render(request, 'image_app/upload_image.html', context)
    else:
        context = {
            'image': "test get"
        }
        return render(request, 'image_app/upload_image.html', context)