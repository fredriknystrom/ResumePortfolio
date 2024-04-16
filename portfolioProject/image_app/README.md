# Image Editor

## Overview
Image editor application offers a user-friendly interface for uploading images and applying transformations such color scale adjustments, resizing, blurring and format conversion.Leveraging the capabilities of the Python Imaging Library (PIL) alongside NumPy, the app provides quality image processing with an focus on maintaining the aspect ratio and image integrity.

## Features

- **File Type Validation:** Accepts only JPEG and PNG image formats for upload, ensuring compatibility and processing efficiency.
- **Dynamic Color Scale Modification:** Users can easily switch their images to grayscale, redscale, greenscale, bluescale, or apply a custom color scale, providing versatility in visual presentation.
- **Aspect Ratio Preservation:** Incorporates an intelligent resizing feature that adjusts the width of an image while maintaining its aspect ratio, avoiding distortion.
- **Custom Color Selection:** Offers a color picker for those choosing the custom color scale option, enabling precise and personalized color adjustments.
- **Blurring Adjustment:** Users can adjust the blur intensity from 0% to 100% using a slider, enabling subtle softening or significant smoothing of images instantly.
- **Format Conversion:** Allows users to select their preferred output format between JPEG and PNG.
- **Real-time Preview and Download:** After processing, the application displays a preview of the modified image, which can be downloaded in the chosen format and dimensions.

## User Guide

1. **Uploading an Image:** Start by uploading the image you want to edit.

2. **Selecting a Color Scale:** Choose from the following color scale options for your image:
   - `Original`: Keeps the image's original colors.
   - `Grey`: Converts the image to grayscale.
   - `Red`: Applies a red hue to the image.
   - `Green`: Applies a green hue to the image.
   - `Blue`: Applies a blue hue to the image.
   - `Custom`: If this option is selected, choose a color using the color picker for a unique effect.

3. **Adjusting Image Width:** Alter the image's width as desired, while the original aspect ratio is preserved. Leave the width field blank to keep the image's original width.

4. **Applying a Blur Effect:** Adjust the blur intensity using a slider from 0% for no blur to 100% for maximum blur, allowing you to soften or smooth the image as needed.

5. **Choosing the Output Format:** Select your preferred output format for the edited image. Options include JPEG and PNG.


## Example

### Originally I have this image of size 1792 × 1024.

![ORIGINAL IMG](/md-images/Python2.png)

### Appying custom colorscale, resizing image to 600 x 342 and output as PNG.

![SETTINGS IMG](/md-images/image-editor.png)

### This is the resulting image - Python2_custom.png

![FINAL IMG](/md-images/Python2_custom.png)





