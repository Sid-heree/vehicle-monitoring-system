import streamlit as st
import cv2
import numpy as np
import time
from services.pipeline import process_image

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Vehicle AI System", layout="wide")

# ================= CUSTOM CSS =================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Title */
.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #00FFD1;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cccccc;
}

/* Card */
.card {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
}

/* Upload box */
.css-1cpxqw2 {
    border: 2px dashed #00FFD1;
    padding: 20px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown('<p class="main-title">🚗 Vehicle Monitoring System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI Detection • Number Plate • Seatbelt • Real-Time Video</p>', unsafe_allow_html=True)

st.divider()

# ================= FILE UPLOAD =================
uploaded_file = st.file_uploader(
    "📤 Upload Image or Video",
    type=["jpg", "png", "jpeg", "mp4"]
)

# ================= PROCESS =================
if uploaded_file:

    file_type = uploaded_file.type

    # ================= IMAGE =================
    if "image" in file_type:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📷 Original Image")
            st.image(image, channels="BGR")

        with st.spinner("🔍 Processing image..."):
            result = process_image(image, use_ocr=True)

        with col2:
            st.markdown("### 🤖 Detection Output")
            st.image(result["image"], channels="BGR")

        st.divider()

        # ================= RESULTS =================
        st.markdown("###  Detection Results")

        if len(result["data"]) == 0:
            st.warning("⚠️ No vehicle detected")
        else:
            for item in result["data"]:
                st.markdown(f"""
                <div class="card">
                    🚘 <b>Vehicle:</b> {item['vehicle_type']} <br>
                    🔢 <b>Plate:</b> {item['plate']} <br>
                     <b>Seatbelt:</b> {item['seatbelt']}
                </div>
                """, unsafe_allow_html=True)

    # ================= VIDEO =================
    elif "video" in file_type:

        tfile = open("temp.mp4", "wb")
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture("temp.mp4")

        st.markdown("### 🎥 Video Processing")
        stframe = st.empty()

        frame_count = 0
        prev_time = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1

            # 🔥 Skip frames for speed
            if frame_count % 3 != 0:
                continue

            frame = cv2.resize(frame, (640, 480))

            # 🔥 FPS calculation
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
            prev_time = curr_time

            result = process_image(frame, use_ocr=False)
            output_frame = result["image"]

            # 🔥 FPS Display
            cv2.putText(
                output_frame,
                f"FPS: {int(fps)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )

            stframe.image(output_frame, channels="BGR")

        cap.release()