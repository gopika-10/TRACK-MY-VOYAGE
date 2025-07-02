import streamlit as st
import tempfile
import cv2
import numpy as np
import os
from detect import detect_ships
from datetime import datetime

st.set_page_config(page_title="Ship Detection", layout="wide")

st.title("🛰️ Ship Detection")

uploaded_file = st.file_uploader("📤 Upload Satellite Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Run detection
    image, detections = detect_ships(tmp_path)

    # Sidebar stats
    st.sidebar.header("📊 Detection Stats")
    st.sidebar.success(f"✅ Ships Detected: **{len(detections)}**")
    for idx, det in enumerate(detections):
        st.sidebar.write(f"Ship {idx + 1}: Confidence {det['confidence']:.2f}")

    # Draw bounding boxes on image
    for det in detections:
        x1, y1, x2, y2 = map(int, det['box'])
        conf = det['confidence']
        label = f"{det['label']} {conf:.2f}"
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    st.image(image, channels="BGR", caption="Detected Image", use_column_width=True)

    # Save the output image and provide download button
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
    cv2.imwrite(output_path, image)

    with open(output_path, "rb") as file:
        st.download_button("⬇️ Download Result Image", file, file_name=os.path.basename(output_path), mime="image/jpeg")
