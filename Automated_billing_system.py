# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 22:32:39 2025

@author: 91944
"""
import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO

# Load your YOLOv8 model
model = YOLO(r"D:\Studies\Bangalore\T3\Capstone\best.pt")

# Price list
price_list = {
    "beans": 20, "cake": 60, "candy": 5, "cereal": 30, "chips": 10, "chocolate": 10, "coffee": 25, "corn": 20,
    "flour": 40, "honey": 70, "jam": 50, "juice": 30, "milk": 20, "nuts": 80, "oil": 65, "pasta": 40, "rice": 30,
    "soda": 25, "spices": 75, "sugar": 50, "tea": 20, "tomato sauce": 15, "fish": 50, "vinegar": 40, "water": 10
}

st.title("🛒 Automated Grocery Billing System")

uploaded_file = st.file_uploader("Upload Grocery Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to array
    img_array = np.array(image)

    # Run detection
    results = model(img_array)[0]

    # Draw bounding boxes on image
    boxed_image = results.plot()  # returns a NumPy array with boxes

    st.image(boxed_image, caption="Detected Items with Bounding Boxes", use_container_width=True)

    # Get class names
    detected_classes = [model.names[int(cls)] for cls in results.boxes.cls]

    st.subheader("📦 Detected Items")
    st.write(detected_classes)

    st.subheader("🧾 Billing Details")
    bill = {}
    total = 0
    for item in detected_classes:
        if item in price_list:
            bill[item] = bill.get(item, 0) + price_list[item]
            total += price_list[item]
        else:
            st.warning(f"'{item}' not found in price list!")

    for item, price in bill.items():
        st.write(f"{item}: ₹{price}")

    st.markdown(f"### 💰 Total Amount: ₹{total}")
