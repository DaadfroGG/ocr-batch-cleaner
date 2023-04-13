import os
import cv2
import numpy as np

# Define the source directory containing the image files
source_dir = 'raws'

# Define the mask directory
mask_dir = 'text_masks'

# Define the output directory for masked images
output_dir = 'text_files'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of image files in the source directory
image_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

# Loop through each image file and apply the text mask
for image_file in image_files:
    # Load the original image and the text mask
    image_path = os.path.join(source_dir, image_file)
    mask_path = os.path.join(mask_dir, image_file)
    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path, 0)

    # Invert the mask
    mask = cv2.bitwise_not(mask)

    # Set the pixels outside the text regions to white
    img[mask > 0] = 255

    # Save the masked image
    output_path = os.path.join(output_dir, image_file)
    cv2.imwrite(output_path, img)

