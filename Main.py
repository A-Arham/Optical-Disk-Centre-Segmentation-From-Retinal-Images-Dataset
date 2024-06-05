import cv2
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_and_save_histogram(image, output_folder, image_name, channel):
    # Calculate histogram for the channel
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Normalize histogram
    hist /= hist.sum()

    # Plot histogram
    plt.plot(hist, color=channel)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title(f'{channel.capitalize()} Channel Histogram')
    plt.xlim([0, 256])

    # Save histogram plot
    plt.savefig(os.path.join(output_folder, f'{channel}-plot', image_name.replace('.jpg', f'_{channel}_histogram.png')))
    plt.close()

def save_channels(image, output_folder, image_name):
    # Split the image into its color channels
    b, g, r = cv2.split(image)

    # Save each channel to separate folders
    cv2.imwrite(os.path.join(output_folder, "blue", image_name), b)
    cv2.imwrite(os.path.join(output_folder, "green", image_name), g)
    cv2.imwrite(os.path.join(output_folder, "red", image_name), r)

    # Calculate and save histogram for each channel
    calculate_and_save_histogram(b, output_folder, image_name, 'blue')
    calculate_and_save_histogram(g, output_folder, image_name, 'green')
    calculate_and_save_histogram(r, output_folder, image_name, 'red')

def enhance_contrast(image):
    # Convert image to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split the LAB image into channels
    l, a, b = cv2.split(lab)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the L channel
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_l = clahe.apply(a)

    # Merge the enhanced L channel with the original A and B channels
    enhanced_lab = cv2.merge([enhanced_l, a, b])

    # Convert LAB image back to BGR color space
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

    return enhanced_image

def place_markers_and_save_channels(input_folder, output_folder, csv_file):
    # Load CSV file
    df = pd.read_csv(csv_file)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create subfolders for each color channel
    for color in ["blue", "green", "red"]:
        channel_folder = os.path.join(output_folder, color)
        if not os.path.exists(channel_folder):
            os.makedirs(channel_folder)

    # Create subfolders for histogram plots
    for channel in ['blue', 'green', 'red']:
        plot_folder = os.path.join(output_folder, f'{channel}-plot')
        if not os.path.exists(plot_folder):
            os.makedirs(plot_folder)

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        # Get image name and coordinates
        image_name = row["image"]

        # Read the image
        image_path = os.path.join(input_folder, image_name)
        image = cv2.imread(image_path)

        # Apply average filtering to decrease noise
        filtered_image = cv2.blur(image, (7, 7))

        # Enhance contrast for green channel images
        # if 'green' in image_name:
        if 'green' in image_name:
            filtered_image = enhance_contrast(filtered_image)

        # Draw cross-shaped marker on the filtered image
        marker_color = (0, 0, 255)  # Red color for marker
        x = int(row["x"])
        y = int(row["y"])
        # marker_size = 20
        # cv2.drawMarker(filtered_image, (x, y), marker_color, markerType=cv2.MARKER_CROSS, markerSize=marker_size, thickness=2)
        #
        # # Draw circular region around the marker
        # radius = 20
        # cv2.circle(filtered_image, (x, y), radius, marker_color, thickness=2)

        # Save each channel to separate folders and calculate histograms
        save_channels(filtered_image, output_folder, image_name)

# Example usage:
input_folder = "H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\Assignment-2\Fundus image"
output_folder = "H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output"
csv_file = "optic_disc_centres.csv"

place_markers_and_save_channels(input_folder, output_folder, csv_file)
