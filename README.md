# Finger Counter

This project is a **computer vision application** that detects and counts the number of fingers shown to a webcam in real-time. It uses **OpenCV** and **MediaPipe** to track hand landmarks, determine which fingers are up, and display the total count on the screen.

---

## 📂 Project Files

- **`main.py`**  
  The main script. Captures webcam video, uses the `HandTrackingModule` to count fingers, and displays the result.  

- **`HandTrackingModule.py`**  
  A reusable module containing all core logic: hand detection, landmark position extraction, determining which fingers are raised, and measuring distances between points.  

---

## 🚀 Features

- Real-time hand and finger tracking  
- Right/left hand detection  
- Determines which fingers are raised or closed  
- Displays total finger count on screen  
- FPS calculation and display  

---

## 🛠 Requirements

You need Python 3 and the following dependencies:  

```bash
pip install opencv-python mediapipe
```

---

## ▶️ How to Run

1. Clone the repository or download the files:
```bash
git clone https://github.com/Brkberber/Finger-Counter.git
cd Finger-Counter
```

2. Start the application:
```bash
python main.py
```

3. A webcam window will open. Raise or lower your fingers — the counter in the top-left corner (**"Finger: X"**) will update live.  
4. Press **`q`** to exit.  

---

## 📌 Notes

- The `fingersUp()` function checks the thumb direction based on the detected hand type (right/left) and evaluates each finger individually.  
- The `findDistance()` method can measure distances between landmarks for gesture control.  
