import os

import matplotlib.pyplot as plt
import keras_ocr
import cv2
import math
import numpy as np

#    Use a different fill method: The current implementation uses the cv2.fillPoly() function to fill the polygon with white color. You can experiment with different fill methods, such as cv2.drawContours(), to see if this improves the accuracy of the mask.

#    Use a different OCR model or preprocessing method: The accuracy of the mask depends on the accuracy of the OCR model and the quality of the input image. You can experiment with different OCR models or preprocessing methods to see if this improves the accuracy of the mask.

def midpoint(x1, y1, x2, y2):
    x_mid = int((x1 + x2)/2)
    y_mid = int((y1 + y2)/2)
    return (x_mid, y_mid)


def generate_text_mask(img_path, pipeline, threshold=0):
    # read the image 
    img = keras_ocr.tools.read(img_path) 
    
    # Recognize text (and corresponding regions)
    # Each list of predictions in prediction_groups is a list of
    # (word, box) tuples. 
    prediction_groups = pipeline.recognize([img])
    
    # Define the mask for text regions
    mask = np.zeros(img.shape[:2], dtype="uint8")
    for box in prediction_groups[0]:
        x0, y0 = box[1][0]
        x1, y1 = box[1][1] 
        x2, y2 = box[1][2]
        x3, y3 = box[1][3] 
        
        # Draw a filled polygon corresponding to the text region
        pts = np.array([[x0, y0], [x1, y1], [x2, y2], [x3, y3]], dtype=np.int32)
        cv2.fillPoly(mask, [pts], (255,), threshold)
                 
    return(mask)



# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# Define the source directory containing the image files
source_dir = 'raws'

# Define a directory to save the text masks
mask_dir = 'text_masks'

# Create the mask directory if it doesn't exist
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)

# Get a list of image files in the source directory
image_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

# Loop through each image file and generate a text mask
for image_file in image_files:
    # Generate the text mask
    image_path = os.path.join(source_dir, image_file)
    text_mask = generate_text_mask(image_path, pipeline, threshold=100)
    
    # Save the mask image
    mask_path = os.path.join(mask_dir, image_file)
    cv2.imwrite(mask_path, text_mask)

output_dir = 'masked_images'

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
    
    # Replace the text with white color
    img[mask > 0] = 255
    
    # Save the masked image
    output_path = os.path.join(output_dir, image_file)
    cv2.imwrite(output_path, img)

