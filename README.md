# ocr-batch-cleaner

This program utilizes the Keras-OCR library and OpenCV to generate text masks for images. It identifies text regions in the images and creates binary masks where the text regions are marked as white pixels.

## Requirements

To run this program, make sure you have the following dependencies installed:

- Python 3.x
- Keras-OCR
- OpenCV
- Matplotlib

You can install the required Python packages using the following command:

```pip install keras-ocr opencv-python matplotlib```


## Usage

1. Place your images in the `raws` directory.
2. Run the program by executing the Python script `mask.py`.
3. The program will generate text masks for each image in the `text_masks` directory.
4. The masked images will be saved in the `masked_images` directory.

Here are some example images processed by the program:

*Original Image*
![2010-09-10-home](https://github.com/DaadfroGG/ocr-batch-cleaner/assets/101118957/5c9d82dc-591e-46e1-bde0-00b33e3fa4a6)

*Text Mask*
![2010-09-10-home](https://github.com/DaadfroGG/ocr-batch-cleaner/assets/101118957/ab3df494-3e2a-40df-82bc-cca59d2a9e0a)

*Masked Image*
![2010-09-10-home](https://github.com/DaadfroGG/ocr-batch-cleaner/assets/101118957/7b2564f6-b075-4f0c-83a3-fc6f3080fe23)

## Customization

- You can adjust the threshold value used for generating the text mask by modifying the `threshold` parameter in the `generate_text_mask` function.
- If the required directories (`text_masks` and `masked_images`) do not exist, the program will create them automatically.

## Benefits of Using Text Masks

Instead of using the provided masked images, it is recommended to work directly with the generated text masks. This approach allows you to have better control over the text regions in the images. Some potential benefits of using text masks include:

- **Selective masking:** You can apply the text mask to specific parts of the original image, preserving other elements in the scene.
- **Text extraction:** You can extract the text regions from the original image using the text mask and use them for further analysis or processing.
- **Customization:** You can modify the text mask to refine the text region boundaries or combine multiple masks for complex text region selections.


## Limitations

- The program currently supports the following image file formats: JPG, JPEG, PNG, and BMP. Make sure your images have one of these file extensions.
- The program assumes that the image directory (`raws`), text mask directory (`text_masks`), and output directory (`masked_images`) are located in the same directory as the script.
