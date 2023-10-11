import numpy as np
from tensorflow.keras.datasets import mnist
from scipy.ndimage import rotate
from utils import display_images

def rotate_images(images, max_rotation_degree, rotation_interval):

    # Initialize a list to hold the rotated images
    rotated_images = []

    counter = 0  # For printing progress
    for image in images:
        for angle in range(-max_rotation_degree, max_rotation_degree + 1, rotation_interval):
            rotated = rotate(image, angle, reshape=False)  # Keep original shape
            rotated_images.append(rotated)
            
            counter += 1
            if counter % 10000 == 0:
                print(f"Processed {counter}/{len(images) + len(images) * 2 * max_rotation_degree // rotation_interval} images.")
    return np.array(rotated_images)

def main():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    max_rotation_degree = 20
    max_rotation_interval = 5
    assert max_rotation_degree % max_rotation_interval == 0
    n_replicas = max_rotation_degree/max_rotation_interval * 2 + 1
    
    
    # Process and save training data
    rotated_train_images = rotate_images(train_images, max_rotation_degree, max_rotation_interval)
    rotated_train_labels = np.repeat(train_labels, n_replicas)  # For each image, there are 13 versions (1 original + 8 rotations)
    display_images(rotated_train_images)
    np.save('data/rotated_train_images.npy', rotated_train_images)
    np.save('data/rotated_train_labels.npy', rotated_train_labels)
    
    # Process and save test data
    rotated_test_images = rotate_images(test_images, max_rotation_degree, max_rotation_interval)
    rotated_test_labels = np.repeat(test_labels, n_replicas)  # Similarly, for each test image
    display_images(rotated_test_images)  # If you want to display some of the rotated test images
    np.save('data/rotated_test_images.npy', rotated_test_images)
    np.save('data/rotated_test_labels.npy', rotated_test_labels)

    print("Data saved successfully!")

if __name__ == '__main__':
    main()
