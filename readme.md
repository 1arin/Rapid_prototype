git push origin main# Image Processing Web App

A simple Streamlit web application for basic image processing.

## Features
- Choose image from **local upload** or **webcam capture**
- Apply image processing filters:
  - Grayscale
  - Gaussian Blur (adjustable kernel size)
  - Canny Edge Detection (adjustable min/max thresholds)
- Display **original image** and **processed image**
- Show **histogram** of processed image

## Installation

1. Clone this repository
2. Create a virtual environment (optional but recommended)
     python -m venv env
3. Activate the environment
     env\Scripts\activate
4. Install dependencies
     pip install -r requirements.txt

**Usage**
- Run the Streamlit app
    streamlit run app.py
- Open the URL shown in your terminal (usually http://localhost:8501) in a web browser

**notes**
- The use_container_width=True parameter ensures the images scale to the container width.
- Canny edge detection requires grayscale images; this is handled automatically in the app.
- Histogram works for grayscale, binary, and RGB images.

  If you have any questions/problem pleasw contact me here **aroundthegreat@gmail.com**
