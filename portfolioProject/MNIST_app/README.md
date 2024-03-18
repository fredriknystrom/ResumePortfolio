# Overview
This project is a basic machine learning model, trained using the MNIST dataset with 28x28 pixel images, to accurately predict handwritten numbers from the user between 0 to 9. 

![MNIST IMG](/md-images/mnist.png)

## Dataset
The original dataset is 60 000 images but I added some synthetic data by rotating the images slightly within a range of 10 degrees. For training 660 000 images were used and for testing 110 000 images were used.

## Model
The neural network is implemented with the help of Keras API and the layers are taken from this Kaggle post:
https://www.kaggle.com/code/cdeotte/how-to-choose-cnn-architecture-mnist


## Rescale image from UI
The drawingboard for the users is 560x560 pixels on computer screens and 280x280 pixels on mobile devices. The input needs to be rescaled to 28x28 for the model, the image is first cropped to the smallest square determined by existing pixel values. After that some padding is added to the input. Finally the input is resized to a 28x28 dimension, which the model can process.

