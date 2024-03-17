import matplotlib.pyplot as plt
import numpy as np
import cv2

def display_images(images, num=20):
    """Display a random set of images."""
    
    fig, axes = plt.subplots(1, num, figsize=(20, 2))
    #indices = np.random.choice(images.shape[0], size=num, replace=False)
    indices = range(0,20)
    
    for ax, idx in zip(axes, indices):
        ax.imshow(images[idx], cmap='gray')
        ax.axis("off")
        
    plt.show()

 # Display some images along with their labels
def check_image_labelling(labels, images):
    for idx in range(0, 100, 10):
        print(f"Label: {labels[idx]}")
        plt.imshow(images[idx], cmap='gray')
        plt.show()

def cv2_crop(data):
    # Find the bounding box of non-zero values
    non_zero_indices = np.nonzero(data)
    min_y, min_x = np.min(non_zero_indices, axis=1)
    max_y, max_x = np.max(non_zero_indices, axis=1)

    # +1 to include last values
    delta_x = max_x-min_x + 1
    delta_y = max_y-min_y + 1

    # Calculate the maximum dimension (width or height)
    max_dimension = max(delta_x, delta_y)

    # Calculate the padding size to make it square
    padding_size = int(1.1 * max_dimension)

    # Calculate vertical and horizontal padding while maintaining aspect ratio
    horizontal_padding = int((padding_size - delta_x) / 2)
    vertical_padding = int((padding_size - delta_y) / 2)
        
    # Create a new square image with padding
    padded_array = np.zeros((padding_size, padding_size), dtype=np.uint8)

    # Copy the cropped image to the center of the padded array
    padded_array[vertical_padding:vertical_padding + delta_y,
                 horizontal_padding:horizontal_padding + delta_x] = data[min_y:max_y+1, min_x:max_x+1]    

    # Resize the padded image to 28x28
    resized_array = cv2.resize(padded_array, (28, 28), interpolation=cv2.INTER_LINEAR)

    return resized_array