<h1 align="center">🚗 Vehicle Monitoring System</h1>
<p align="center">AI Detection • Number Plate • Seatbelt • Real-Time Video</p>

An AI-powered computer vision system that detects vehicles, recognizes number plates, and analyzes seatbelt usage from images and videos.



<h2>Features</h2>

🚘 Vehicle Detection (Car, Truck, Bus, Motorcycle)
🔢 Number Plate Detection
🔤 OCR (Extract text from number plates)
 Seatbelt Detection
🎥 Video Processing with FPS display
📷 Image Upload Support
🎨 Clean Streamlit UI

<h2>🧠 Tech Stack</h2>

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

<h3>▶️ Run the Application</h3>
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



Output:
<img width="1982" height="1056" alt="image" src="https://github.com/user-attachments/assets/2c71207b-d22f-44e8-a50e-973fb78a93b6" />
<img width="2100" height="1055" alt="image" src="https://github.com/user-attachments/assets/464c2122-1d99-4e5f-93fb-323777995c50" />

