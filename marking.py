import cv2
import os
import numpy as np
import csv

def find_max_intensity(image):
    max_intensity = np.max(image)
    max_intensity_coordinate = np.unravel_index(np.argmax(image), image.shape)
    return max_intensity, max_intensity_coordinate

def save_coordinates_to_csv(csv_file, image_filename, coordinates):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([image_filename, coordinates[1], coordinates[0]])  # Writing row in format [filename, y-coordinate, x-coordinate]

# Function to process images in a folder
def process_images(input_folder, output_csv):
    # Write header to CSV file
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image Filename', 'Y Coordinate', 'X Coordinate'])  # Writing header row

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.tif','JPG')):
            # Read the input image
            image_path = os.path.join(input_folder, filename)
            bgr_image = cv2.imread(image_path)

            # Convert the image to grayscale
            grayscale_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

            # Find the maximum intensity value and its coordinate in the image
            max_intensity, max_intensity_coordinate = find_max_intensity(grayscale_image)

            # Save the coordinates to the CSV file
            save_coordinates_to_csv(output_csv, filename, max_intensity_coordinate)

# Example usage:
input_folder = 'H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output\AND2'  # Replace with your input folder path
output_csv = 'max_intensity_coordinates.csv'  # Replace with the desired output CSV file path

process_images(input_folder, output_csv)
