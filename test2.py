import os
import cv2

def and_images(folder1, folder2, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the folders
    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)

    # Iterate over the files in the folders
    for file1, file2 in zip(files1, files2):
        # Read images
        img1 = cv2.imread(os.path.join(folder1, file1))
        img2 = cv2.imread(os.path.join(folder2, file2))

        # Check if images are successfully loaded
        if img1 is not None and img2 is not None:
            # Resize images to a common size
            img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

            # Perform logical AND operation
            result = cv2.bitwise_and(img1, img2)

            # Save the output image
            output_path = os.path.join(output_folder, file1.split('.')[0] + '_AND_' + file2)
            cv2.imwrite(output_path, result)
            print(f"Saved {output_path}")
        else:
            print(f"Error: Could not read {file1} or {file2}")

# Example usage
folder1 = 'H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\Assignment-2\Fundus image'
folder2 = 'H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output\AND'
output_folder = 'H:\SEM 6\DIP\THEORY\ASSIGNMENT-2\Assignment-2-20240424T142035Z-001\output\AND2'

and_images(folder1, folder2, output_folder)
