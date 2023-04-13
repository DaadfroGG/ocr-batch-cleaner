import os
import cv2
import numpy as np
def apply_mask(raw_dir, mask_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of image files in the raw directory
    image_files = [f for f in os.listdir(raw_dir) if os.path.isfile(os.path.join(raw_dir, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    # Loop through each image file and apply the text mask
    for image_file in image_files:
        # Load the original image and the text mask
        image_path = os.path.join(raw_dir, image_file)
        mask_path = os.path.join(mask_dir, image_file)
        img = cv2.imread(image_path)
        mask = cv2.imread(mask_path, 0)
        
        # Replace the text with white color
        img[mask > 0] = 255
        
        # Save the masked image
        output_path = os.path.join(output_dir, image_file)
        cv2.imwrite(output_path, img)

raw_dir = 'raws'
mask_dir = 'text_masks'
output_dir = 'masked_images'

apply_mask(raw_dir, mask_dir, output_dir)

