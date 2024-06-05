# Optic Disc Extraction from Fundus Images

This project explores spatial enhancement and segmentation techniques in digital image processing, specifically for extracting the optic disc from fundus images. These methods are crucial in medical imaging applications for diagnosing various retinal diseases.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Features](#features)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Spatial enhancement and segmentation are fundamental techniques in image processing, particularly in medical imaging applications. This project aims to accurately extract the optic disc from a dataset of 50 fundus images. The optic disc, along with vessels and the fovea, serves as a key landmark in these images.



Ensure you have the following software installed:

- Python 3.x
- OpenCV
- NumPy
- Pandas
- Matplotlib

### Clone the Repository

```sh
git clone https://github.com/your_username/project_name.git
cd project_name
```


## Methodology
The project utilizes a combination of transformation and image filtering techniques for spatial enhancement. Methods such as histogram equalization and contrast stretching improve image quality. Image filtering, including Gaussian blur and morphological operations, refines the images for better segmentation. Segmentation is performed using thresholding techniques and refined with region-growing algorithms and edge detection methods.

## Features
Spatial enhancement using histogram equalization and contrast stretching.
Image filtering techniques like Gaussian blur.
Segmentation using thresholding, region-growing, and edge detection.
Extraction of the optic disc from fundus images.
Configuration
Configure the paths and parameters in the respective Python scripts according to your environment and dataset.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## Fork the Project.
Create your Feature Branch (git checkout -b feature/AmazingFeature).
Commit your Changes (git commit -m 'Add some AmazingFeature').
Push to the Branch (git push origin feature/AmazingFeature).
Open a Pull Request.
License
Distributed under the MIT License. See LICENSE for more information.


## View Images
To view the input fundus images and the marked output images, please visit the following Google Drive link:
https://drive.google.com/drive/folders/12HuSF0yq9lbpziSn1ek1I0beBs1ZGJhR?usp=sharing

Google Drive Link

## Acknowledgements
Dr. Usman Akram - Project Supervisor
Arham-368967 - Project Contributor
College of E&ME, NUST, Rawalpindi