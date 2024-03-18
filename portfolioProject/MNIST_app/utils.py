import matplotlib.pyplot as plt
import numpy as np
import cv2

def preprocess_data(data):
    # Normalize the data - Scale images to the [0, 1] range
    norm_data = data.astype("float32") / 255

    # Make sure images have shape (28, 28, 1)
    dim_data = np.expand_dims(norm_data, -1)
    return dim_data

def log_model_params(batch_size, epochs, test_accuracy,
                      test_loss, history, train_images, test_images, filename):
    """
    Logs parameters of interest to a txt file in the model_logs dir
    """

    with open(f'model_logs/{filename}.txt', 'w') as file:
        # Write each string to the file followed by a newline character
        file.write(f'Data\n')
        file.write(f'Train: {len(train_images)} images\n')
        file.write(f'Test: {len(test_images)} images\n')
        file.write(f'\n')

        file.write(f'Training\n')
        file.write(f'Training loss: {history.history["loss"]}\n')
        file.write(f'Training accuracy: {history.history["accuracy"]}\n')
        file.write(f'\n')

        file.write(f'Validation\n')
        file.write(f'Validation loss: {history.history["val_loss"]}\n')
        file.write(f'Validation accuracy: {history.history["val_accuracy"]}\n')
        file.write('\n')

        file.write(f'Batch size: {batch_size}\n')
        file.write(f'Epochs: {epochs}\n')
        file.write(f'Test accuracy: {test_accuracy}\n')
        file.write(f'Test loss: {test_loss}\n')


def plot_loss_curves(history, filename):
    """
    Plotting loss for training and validation data and saves the plot as png
    """
    # Extract loss values from the history object
    training_loss = history.history['loss']
    validation_loss = history.history['val_loss']

    # Plot the training and validation loss
    plt.figure(figsize=(10, 6))
    plt.plot(training_loss, label='Training Loss', color='blue')
    plt.plot(validation_loss, label='Validation Loss', color='red')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.savefig(f'{filename}.png')
    plt.show()

def display_images(images, num=20, rand=False):
    """Display a first or random n images."""
    
    fig, axes = plt.subplots(1, num, figsize=(20, 2))
    if rand:
        indices = np.random.choice(images.shape[0], size=num, replace=False)
    else:
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
    """
    Crops number on the canvas from the frontend and adds some padding to 
    make the format of the image more alike the mnist set which the model
    is trained on.
    """
    
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
    padding_size = int(1.2 * max_dimension)

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

    #print(resized_array)

    return resized_array