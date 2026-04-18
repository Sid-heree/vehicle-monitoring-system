 Vehicle Monitoring System

An AI-powered computer vision system that detects vehicles, recognizes number plates, and analyzes seatbelt usage from images and videos.

Features
🚘 Vehicle Detection (Car, Truck, Bus, Motorcycle)
🔢 Number Plate Detection
🔤 OCR (Extract text from number plates)
 Seatbelt Detection
🎥 Video Processing with FPS display
📷 Image Upload Support
🎨 Clean Streamlit UI


🧠 Tech Stack
Python
OpenCV
Ultralytics YOLOv8
EasyOCR
Streamlit


Project Structure:
<img width="497" height="802" alt="image" src="https://github.com/user-attachments/assets/1ca03746-86d6-4a41-a7f6-be661ff2a23d" />




⚙️ Installation
git clone https://github.com/your-username/vehicle-monitoring-system.git
cd vehicle-monitoring-system

pip install -r requirements.txt

▶️ Run the Application
streamlit run app/app.py

*How It Works

Upload an image or video
System detects:
Vehicle
Number plate
Seatbelt usage
Displays:
Annotated output
Detection results
FPS (for video)


🧩 Pipeline

Input → Vehicle Detection → Plate Detection → OCR → Seatbelt Detection → Output
⚠️ Notes
OCR works best on clear number plates
Seatbelt detection requires visible driver
Video processing may be slower on low-end systems
