# Eye Blink Detection Project

## Overview

This project implements an eye blink detection system using OpenCV, dlib, and NumPy. The system processes real-time video feed, detects faces, extracts eye regions, and determines blink occurrences using eye aspect ratio (EAR).

## Features

- Real-time Eye Blink Detection using a webcam

- Face and Eye Landmark Detection via dlib

- Eye Aspect Ratio (EAR) Calculation for blink classification

- Threshold-based Blink Detection

## Installation

- Ensure you have Python installed. Then, install the required dependencies using:

- pip install opencv-python-headless dlib numpy scipy

## Usage

- Run the script to start real-time eye blink detection:

- python eye_blink_detection.py

## How It Works

- The system loads a pre-trained facial landmark detector from dlib.

- It captures frames from the webcam and detects the facial region.

- Extracts eye landmarks and computes the Eye Aspect Ratio (EAR).

- If EAR falls below a threshold for a certain duration, a blink is detected.

## Dependencies

- Python 3.x

- OpenCV

- dlib

- NumPy

- SciPy

## Acknowledgments

- dlib’s facial landmark detector for feature extraction

- Timmothy Trinkle’s research on EAR for blink detection

## License

This project is open-source and available under the MIT License.

