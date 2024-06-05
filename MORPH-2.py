
import cv2
import os

def perform_closing(input_folder, output_folder, kernel_size):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.JPG', '.png', '.jpeg','.tif')):
            # Read the input image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Define the structuring element (kernel) for closing operation
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))

            # Perform closing operation
            closed_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
            closed_image = cv2.morphologyEx(closed_image, cv2.MORPH_CLOSE, kernel)
            # closed_image = cv2.dilate(closed_image, kernel, iterations=3)
            closed_image = cv2.erode(closed_image, kernel, iterations=1)
            # closed_image = cv2.morphologyEx(closed_image, cv2.MORPH_CLOSE, kernel)

            # Save the closed image
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, closed_image)

            print(f"Closing performed and image saved: {output_path}")

# Example usage:
input_folder = r'H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output\morph'  # Replace with your input folder path
output_folder = r'H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output\morph-2'  # Replace with your output folder path
kernel_size = 21  # Adjust the kernel size as needed

perform_closing(input_folder, output_folder, kernel_size)
