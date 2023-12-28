from django.shortcuts import render
from PIL import Image
from io import BytesIO
import base64
import numpy as np

def upload_image(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        selected_color = request.POST.get('color', '#ffffff')
        # Return original image if no processing options are selected
        processed_image = Image.open(uploaded_image)
        if 'grayscale' in request.POST:
            image = Image.open(uploaded_image)
            processed_image = image.convert('L')
        else:
            image = Image.open(uploaded_image).convert("RGB")
            np_image = np.array(image)
            if 'redscale' in request.POST:
                np_image[:, :, 1] = 0  # Remove green channel
                np_image[:, :, 2] = 0  # Remove blue channel

            elif 'greenscale' in request.POST:
                np_image[:, :, 0] = 0  # Remove red channel
                np_image[:, :, 2] = 0  # Remove blue channel

            elif 'bluescale' in request.POST:
                np_image[:, :, 0] = 0  # Remove red channel
                np_image[:, :, 1] = 0  # Remove green channel
            # Check for custom color
            elif 'color' in request.POST:
                rgb_color = tuple(int(selected_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                np_image = np.multiply(np_image / 255, rgb_color).astype('uint8')

            # Convert the NumPy array back to a PIL Image
            processed_image = Image.fromarray(np_image)

        # Save the processed image to a BytesIO object
        img_io = BytesIO()
        processed_image.save(img_io, format='JPEG', quality=70)
        img_io.seek(0)

        # Convert the image to a data URL
        img_data = base64.b64encode(img_io.getvalue()).decode()
        img_url = 'data:image/jpeg;base64,' + img_data

        context = {
            'image_data_url': img_url,
            'selected_color': selected_color
        }
        return render(request, 'image_app/upload_image.html', context)

    else:
        context = {
            'image_data_url': None,
            'selected_color': '#ff8800'
        }
        return render(request, 'image_app/upload_image.html', context)
