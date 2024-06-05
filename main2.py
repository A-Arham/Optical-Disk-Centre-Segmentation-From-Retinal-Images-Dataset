import cv2
import os
import pandas as pd


def place_markers_and_threshold(input_folder, output_folder, csv_file):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load CSV file
    df = pd.read_csv(csv_file)

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.JPG', '.png', '.jpeg','.tif')):
            # Read the image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Get corresponding coordinates from CSV file
            image_info = df[df['image'] == filename]
            if not image_info.empty:
                x = int(image_info['x'])
                y = int(image_info['y'])
                print(f"Processing image {filename}, coordinates: ({x}, {y})")

                # Calculate the mean intensity around the specified coordinates using a kernel
                # intensity = calculate_mean_intensity(image, x, y, kernel_size)
                # print(f"Mean intensity around coordinates ({x}, {y}): {intensity}")

                # Threshold the image based on the mean intensity value
                _, thresholded_image = cv2.threshold(image, 245, 255, cv2.THRESH_BINARY)

                # Save the thresholded image
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, thresholded_image)

                print(f"Thresholded image saved: {output_path}")




# Example usage:
input_folder = "H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output/t_adaptive"
output_folder = "H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output/thresholded"
csv_file = "optic_disc_centres.csv"

place_markers_and_threshold(input_folder, output_folder, csv_file)
