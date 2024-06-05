import cv2
import os
import csv

def mark_biggest_object_center(thresholded_image):
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables to track the largest contour and its area
    largest_contour = None
    largest_area = 0

    # Iterate through each contour
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # Update the largest contour and its area if the current contour is larger
        if area > largest_area:
            largest_area = area
            largest_contour = contour

    # Calculate the moments of the largest contour to find centroid
    if largest_contour is not None:
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            # Calculate centroid coordinates
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            return (cX, cY)
    else:
        return None

def save_coordinates_to_csv(csv_file, image_filename, coordinates):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([image_filename, coordinates[0], coordinates[1]])  # Writing row in format [filename, x-coordinate, y-coordinate]

# Function to process images in a folder
def process_images(input_folder, output_csv):
    # Write header to CSV file
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image Filename', 'X Coordinate', 'Y Coordinate'])  # Writing header row

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.tif', '.JPG')):
            # Read the input image
            image_path = os.path.join(input_folder, filename)
            thresholded_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Mark the center of the biggest object in the image
            center = mark_biggest_object_center(thresholded_image)

            # Save the coordinates to the CSV file
            if center is not None:
                save_coordinates_to_csv(output_csv, filename, center)
                print(f"Centroid coordinates of the biggest object in image {filename}: ({center[0]}, {center[1]})")
            else:
                print(f"No object found in image {filename}")

# Example usage:
input_folder = 'H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output\AND2'  # Replace with your input folder path
output_csv = 'centroid_coordinates.csv'  # Replace with the desired output CSV file path

process_images(input_folder, output_csv)
