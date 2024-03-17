import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.callbacks import EarlyStopping
from utils import check_image_labelling
import matplotlib.pyplot as plt

# Build the model
def create_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')
    ])
    return model


# Based on: https://www.kaggle.com/code/cdeotte/how-to-choose-cnn-architecture-mnist

def create_improved_model():
    model = Sequential([
        Conv2D(32, kernel_size=3, activation='relu', input_shape=(28, 28, 1)),
        BatchNormalization(),
        Conv2D(32, kernel_size=3, activation='relu'),
        BatchNormalization(),
        Conv2D(32, kernel_size=5, strides=2, padding='same', activation='relu'),
        BatchNormalization(),
        Dropout(0.4),

        Conv2D(64, kernel_size=3, activation='relu'),
        BatchNormalization(),
        Conv2D(64, kernel_size=3, activation='relu'),
        BatchNormalization(),
        Conv2D(64, kernel_size=5, strides=2, padding='same', activation='relu'),
        BatchNormalization(),
        Dropout(0.4),

        Flatten(),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.4),
        Dense(10, activation='softmax')
    ])
    return model



def preprocess_data(data):
    # Normalize the data - Scale images to the [0, 1] range
    norm_data = data.astype("float32") / 255

    # Make sure images have shape (28, 28, 1)
    dim_data = np.expand_dims(norm_data, -1)
    return dim_data

def log_model_params(batch_size, epochs, test_accuracy, test_loss, history):

    with open(f'model_logs/weights_b{batch_size}_e{epochs}.txt', 'w') as file:
    
        # Write each string to the file followed by a newline character
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


def plot_loss_curves(history):
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
    plt.show()

def main():
    # Load data from files
    train_images = np.load('data/rotated_train_images.npy')
    print(len(train_images))
    train_labels = np.load('data/rotated_train_labels.npy')

    test_images = np.load('data/rotated_test_images.npy')
    print(len(test_images))
    test_labels = np.load('data/rotated_test_labels.npy')
    
    #check_image_labelling(loaded_rotated_test_labels, loaded_rotated_test_images)

    # Normalize the data - Scale images to the [0, 1] range
    preprocessed_train_images = preprocess_data(train_images)
    preprocessed_test_images = preprocess_data(test_images)

    # Create model
    model = create_improved_model()

    # Compile the model
    model.compile(optimizer=Adam(),
                loss=SparseCategoricalCrossentropy(),
                metrics=['accuracy'])

    # Introduce early stopping
    early_stopping = EarlyStopping(
        monitor='val_loss', 
        patience=10, 
        restore_best_weights=True
    )

    # Train the model
    batch_size = 64 # 64
    epochs = 20 # 20-30

    history = model.fit(preprocessed_train_images, train_labels, 
            batch_size=batch_size, 
            epochs=epochs,
            validation_data=(preprocessed_test_images, test_labels), 
            callbacks=[early_stopping])

    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(preprocessed_test_images, test_labels, verbose=2)
    print("\nTest accuracy:", test_accuracy)

    # Log model parameters and result
    log_model_params(batch_size, epochs, test_accuracy, test_loss, history)

    # Save the model's weights
    model.save(f'ml_models/weights-b{batch_size}-e{epochs}.keras')

    # Plot training data
    plot_loss_curves(history)

if __name__ == '__main__':
    main()