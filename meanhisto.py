import cv2
import os

def enhance_images_with_histogram_equalization(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.JPG', '.png', '.jpeg','.tif')):
            # Read the image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Apply histogram equalization
            enhanced_image = cv2.equalizeHist(image)

            # Save the enhanced image
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, enhanced_image)

            print(f"Histogram equalization applied and image saved: {output_path}")

# Example usage:
input_folder = "H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output\green"
output_folder = "H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output/t_adaptive"

enhance_images_with_histogram_equalization(input_folder, output_folder)
