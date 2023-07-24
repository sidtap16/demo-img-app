import cv2
import streamlit as st
import numpy as np
from PIL import Image


def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img

def edge_detection(img):
    edge = cv2.Canny(img, threshold1=100, threshold2=200)
    return edge

def grayscale_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def rotate_90(img):
    rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return rot

def rotate_180(img):
    rot1 = cv2.rotate(img, cv2.ROTATE_180)
    return rot1

def resize_image(img):
    cx = st.sidebar.number_input("Enter custom width", min_value=1)
    cy = st.sidebar.number_input("Enter custom height", min_value=1)
    resized = cv2.resize(img, (cx, cy))
    return resized

def cro_image(img):
    roi = img[50:100, 100:300]
    return roi

def main_loop():
    st.title("Image Processing and Task Automation")
    st.subheader("This app allows you to perform operations on images")
    

    blur_rate = st.sidebar.slider("Blurring", min_value=0.1, max_value=3.0)
    brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
    edges_detection = st.sidebar.checkbox("Detect Edges")
    grayscale_conversion = st.sidebar.checkbox('Convert to Grayscale')
    rotation_90 = st.sidebar.checkbox('Rotate 90 Degrees')
    rotation_180 = st.sidebar.checkbox('Rotate 180 Degrees')
    resize_option = st.sidebar.checkbox('Resize')
    Crop_option = st.sidebar.checkbox('Default Crop')
    
        

    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file: 
        st.info('Upload only jpg,png,jpeg files', icon="⚠️")
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    processed_image = blur_image(original_image, blur_rate)
    processed_image = brighten_image(processed_image, brightness_amount)

    if edges_detection:
        processed_image = edge_detection(processed_image)

    if grayscale_conversion:
        processed_image = grayscale_image(processed_image)

    if rotation_90:
        processed_image = rotate_90(processed_image)

    if rotation_180:
        processed_image = rotate_180(processed_image)

    if resize_option:
        processed_image = resize_image(processed_image)

    if Crop_option:
        processed_image = cro_image(processed_image)

    st.text("Original Image vs Processed Image")
    st.image([original_image, processed_image])

   

if __name__ == '__main__':
    main_loop()

