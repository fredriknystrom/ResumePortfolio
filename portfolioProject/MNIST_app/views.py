from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

# Import necessary libraries
import numpy as np
import tensorflow as tf
from django.views.decorators.csrf import csrf_exempt
from MNIST_app.utils import cv2_crop
import os
import json

# Load the pre-trained model
filename = 'new-weights-b64-e6.keras'
model_path = os.path.join(settings.BASE_DIR, 'MNIST_app', 'ml_models', filename)
model = tf.keras.models.load_model(model_path)

@csrf_exempt
def mnist_view(request):
    if request.method == 'POST':
        # Get the JSON data from the request
        data = json.loads(request.body)

        # Extract the pixel data and convert it to a NumPy array
        pixel_data = np.array(data.get('pixel_data', []))

        # Perform any required preprocessing (e.g., cropping)
        preprocessed_data = cv2_crop(pixel_data)

        # Make predictions using your model
        predictions = model.predict(np.expand_dims(preprocessed_data, axis=0))

        # Convert predictions to a format you want to return to the frontend
        predicted_number = np.argmax(predictions[0])

        # Return the predicted result as JSON
        return JsonResponse({'prediction': int(predicted_number)})
    else:
        return render(request, 'MNIST_app/canvas.html')
