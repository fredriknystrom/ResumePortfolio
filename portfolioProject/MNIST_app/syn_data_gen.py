import numpy as np
from tensorflow.keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
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

    max_rotation_degree = 5
    max_rotation_interval = 1
    assert max_rotation_degree % max_rotation_interval == 0
    n_replicas = max_rotation_degree/max_rotation_interval * 2 + 1
    
    # Process and save training data
    rotated_train_images = rotate_images(train_images, max_rotation_degree, max_rotation_interval)
    rotated_train_labels = np.repeat(train_labels, n_replicas)

    # Shuffle the training images so they dont line up
    np.random.seed(35)
    indices = np.arange(len(rotated_train_images))
    np.random.shuffle(indices)

    shuffled_rotated_images = rotated_train_images[indices]
    shuffled_rotated_labels = rotated_train_labels[indices]

    print(shuffled_rotated_labels[:20])
    display_images(shuffled_rotated_images, 20)
  
    np.save(f'data/{max_rotation_degree}-{max_rotation_interval}degree-rotated-train-images.npy', rotated_train_images)
    np.save(f'data/{max_rotation_degree}-{max_rotation_interval}degree-rotated-train-labels.npy', rotated_train_labels)
    
    # Process and save test data
    rotated_test_images = rotate_images(test_images, max_rotation_degree, max_rotation_interval)
    rotated_test_labels = np.repeat(test_labels, n_replicas)  # Similarly, for each test image
    display_images(rotated_test_images)  # If you want to display some of the rotated test images
    np.save(f'data/{max_rotation_degree}-{max_rotation_interval}degree-rotated-test-images.npy', rotated_test_images)
    np.save(f'data/{max_rotation_degree}-{max_rotation_interval}degree-rotated-test-labels.npy', rotated_test_labels)

    print("Data saved successfully!")

if __name__ == '__main__':
    main()
