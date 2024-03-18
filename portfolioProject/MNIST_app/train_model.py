import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.callbacks import EarlyStopping
from utils import check_image_labelling, log_model_params, plot_loss_curves, preprocess_data
import matplotlib.pyplot as plt

# Simple model
def simple_model():
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

def advanced_model():
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

def main():
    # Load data from files
    train_images = np.load('data/5-1degree-rotated-train-images.npy')
    train_labels = np.load('data/5-1degree-rotated-train-labels.npy')
    print(len(train_images))
    print(len(train_labels))

    test_images = np.load('data/5-1degree-rotated-test-images.npy')
    test_labels = np.load('data/5-1degree-rotated-test-labels.npy')
    print(len(test_images))
    print(len(test_labels))
    
    #check_image_labelling(test_images, test_labels)
    
    # Normalize the data - Scale images to the [0, 1] range
    preprocessed_train_images = preprocess_data(train_images)
    preprocessed_test_images = preprocess_data(test_images)

    # Create model
    model = advanced_model()

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
    epochs = 5 # 5-20

    history = model.fit(preprocessed_train_images, train_labels, 
            batch_size=batch_size, 
            epochs=epochs,
            validation_data=(preprocessed_test_images, test_labels), 
            callbacks=[early_stopping])

    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(preprocessed_test_images, test_labels, verbose=2)
    print("\nTest accuracy:", test_accuracy)

    # Create a common file name for model logs, weights and graphs
    filename = f'new-weights-b{batch_size}-e{epochs}'
    # Log model parameters and result
    log_model_params(batch_size, epochs, test_accuracy, test_loss, history, train_images, test_images, filename)

    # Save the model's weights
    model.save(f'model_weights/{filename}.keras')

    # Plot training data and save the plot
    plot_loss_curves(history, filename)

if __name__ == '__main__':
    main()