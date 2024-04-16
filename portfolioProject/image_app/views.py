from django.shortcuts import render
from PIL import Image, ImageFilter
from io import BytesIO
import base64
import numpy as np


def resize_image_aspect_ratio(image, base_width):
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    return image.resize((base_width, h_size), Image.Resampling.LANCZOS)


def image_view(request):
    if request.method == 'POST':
        # Check if an image was uploaded
        if 'image' in request.FILES:

            uploaded_image = request.FILES['image']
            content_type = uploaded_image.content_type
            allowed_mime_types = ['image/jpeg', 'image/png']

            if content_type not in allowed_mime_types:
                # Return an error message if the uploaded file is not a PNG or JPEG image
                context = {
                    'error_message': "Invalid file type. Please upload an image in PNG or JPEG format.",
                }
                return render(request, 'image_app/image-editor.html', context)

            file_format = request.POST.get('fileFormat', 'PNG').lower()
            original_image_name, _ = uploaded_image.name.rsplit('.', 1)
            color_scale = request.POST.get('colorscale')
            custom_color = request.POST.get('customcolor')

            # Return original image if no processing options are selected
            processed_image = Image.open(uploaded_image)
            image_name = original_image_name + '_original.' + file_format
            if color_scale != 'original':
                if color_scale == 'grayscale':
                    image_name = original_image_name + '_gray.' + file_format
                    image = Image.open(uploaded_image)
                    processed_image = image.convert('L')
                else:
                    image = Image.open(uploaded_image).convert("RGB")
                    np_image = np.array(image)
                    if color_scale == 'redscale':
                        image_name = original_image_name + '_red.' + file_format
                        np_image[:, :, 1] = 0  # Remove green channel
                        np_image[:, :, 2] = 0  # Remove blue channel
                    elif color_scale == 'greenscale':
                        image_name = original_image_name + '_green.' + file_format
                        np_image[:, :, 0] = 0  # Remove red channel
                        np_image[:, :, 2] = 0  # Remove blue channel
                    elif color_scale == 'bluescale':
                        image_name = original_image_name + '_blue.' + file_format
                        np_image[:, :, 0] = 0  # Remove red channel
                        np_image[:, :, 1] = 0  # Remove green channel
                    elif color_scale == 'custom':
                        image_name = original_image_name + '_custom.' + file_format
                        rgb_color = tuple(int(custom_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                        np_image = np.multiply(np_image / 255, rgb_color).astype('uint8')
                        
                    # Convert the NumPy array back to a PIL Image
                    processed_image = Image.fromarray(np_image)

            new_width = request.POST.get('newWidth')
            if new_width and int(new_width) > 0:
                new_width = int(new_width)
                processed_image = resize_image_aspect_ratio(processed_image, new_width)
            elif new_width and int(new_width) < 0:
                context = {
                    'image_data_url': None,
                    'color_scale': None,
                    'custom_color': None,
                    'error_message': f"Invalid width of image {new_width}. Width must be positive."
                }
                return render(request, 'image_app/image-editor.html', context)

            # Applying blurr to the image
            blur_percentage = int(request.POST.get('blurPercentage', 0))
            if blur_percentage > 0:
                blur_radius = (blur_percentage / 100.0) * 10
                processed_image = processed_image.filter(ImageFilter.GaussianBlur(radius=blur_radius))

            # Get the dimensions of the processed image
            width, height = processed_image.size

            # Save the processed image to a BytesIO object
            img_io = BytesIO()
            if file_format == 'jpeg':
                # for JPEG, we need to specify the quality
                print('Saving JPEG')
                processed_image.save(img_io, format='JPEG', quality=100)
            else:
                print('Saving PNG')
                processed_image.save(img_io, format='PNG')
            img_io.seek(0)

            # Convert the image to a data URL
            img_data = base64.b64encode(img_io.getvalue()).decode()
            img_url = f"data:image/{file_format.lower()};base64," + img_data
            print(color_scale)
            context = {
                    'image_data_url': img_url,
                    'color_scale': color_scale,
                    'custom_color': custom_color,
                    'image_name': image_name,
                    'image_width': width,
                    'image_height': height,
                    'error_message': None
                }
        else:
            # No image was uploaded
            context = {
                'image_data_url': None,
                'color_scale': 'original',
                'custom_color': '#ffffff',
                'error_message': "No image selected."
            }
        return render(request, 'image_app/image-editor.html', context)
    else:
        context = {
            'image_data_url': None,
            'color_scale': 'original',
            'custom_color': '#ffffff',
            'error_message': None
        }
        return render(request, 'image_app/image-editor.html', context)
