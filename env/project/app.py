import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import io

st.set_page_config(layout="wide")
st.title("Image Processing Web App")

# --- Image Source Selection ---
st.sidebar.header("Select Image Source")
source = st.sidebar.radio("Choose source:", ("Upload from Computer", "Webcam"))

img = None

# --- Load Image ---
if source == "Upload from Computer":
    uploaded_file = st.sidebar.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        img = np.array(Image.open(uploaded_file))

elif source == "Webcam":
    picture = st.sidebar.camera_input("Take a picture with your webcam")
    if picture is not None:
        img = np.array(Image.open(picture))

# --- Show Original Image ---
if img is not None:
    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    # --- Image Processing Options ---
    st.sidebar.header("Processing Options")
    apply_gray = st.sidebar.checkbox("Grayscale")
    apply_blur = st.sidebar.checkbox("Gaussian Blur")
    blur_kernel = st.sidebar.slider("Blur Kernel Size", 1, 15, 5)
    apply_canny = st.sidebar.checkbox("Canny Edge Detection")
    canny_min = st.sidebar.slider("Canny Min Threshold", 0, 255, 50)
    canny_max = st.sidebar.slider("Canny Max Threshold", 0, 255, 150)

    # --- Process Image ---
    proc_img = img.copy()

    if apply_gray:
        proc_img = cv2.cvtColor(proc_img, cv2.COLOR_RGB2GRAY)

    if apply_blur:
        k = blur_kernel if blur_kernel % 2 == 1 else blur_kernel + 1
        proc_img = cv2.GaussianBlur(proc_img, (k, k), 0)

    if apply_canny:
        # Canny ต้องเป็น grayscale
        if len(proc_img.shape) == 3:
            proc_img_gray = cv2.cvtColor(proc_img, cv2.COLOR_RGB2GRAY)
        else:
            proc_img_gray = proc_img
        proc_img = cv2.Canny(proc_img_gray, canny_min, canny_max)

    st.subheader("Processed Image")
    st.image(proc_img, use_container_width=True)

    # --- Histogram ---
    st.subheader("Histogram")
    plt.figure(figsize=(8, 4))

    if len(proc_img.shape) == 2:  # Grayscale or binary
        plt.hist(proc_img.ravel(), bins=256, range=(0, 255), color='gray')
    else:  # RGB
        colors = ('r', 'g', 'b')
        for i, col in enumerate(colors):
            plt.hist(proc_img[:, :, i].ravel(), bins=256, range=(0, 255), color=col, alpha=0.5)

    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    st.pyplot(plt)

else:
    st.info("Please select an image source and provide a picture to start processing")
