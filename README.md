# AI-Powered-Attendance-Management-System
### Overview

The AI-Powered Attendance Management System is a smart and automated solution for tracking attendance in classrooms or workplaces using facial recognition technology. This system eliminates manual attendance, reduces errors, and improves efficiency. Built with Python and OpenCV, it provides a simple GUI for admins and seamless face recognition for users.

### Features

1.Face Recognition Attendance: Automatically marks attendance by detecting and recognizing faces.

2.Real-Time Detection: Uses webcam or video feed for live recognition.

3.Secure Database: Attendance data stored in CSV files or a database.

4.User-Friendly GUI: Interactive interface built with Tkinter.

5.Automated Reports: Generate attendance reports for daily, weekly, or monthly tracking.

6.Supports Multiple Users: Recognizes multiple faces in a single session.

### Technologies Used

i.Python 3.12

ii.OpenCV – Computer vision library for face detection and recognition.

iii.Tkinter – GUI interface for user interactions.

iv.Pillow (PIL) – Image processing library.

v.NumPy – Numerical computations.

vi.CSV – Attendance storage (can be replaced with SQL databases for scalability).

vii.Git & GitHub – Version control

### Project Structure

AI-Powered-Attendance-Management-System/
│
├─ college_images/               # Sample images for testing
│    └─ BestFacialRecognition.JPG
├─ haarcascade/                  # Haar cascade files for face detection
│    └─ haarcascade_frontalface_default.xml
├─ main.py                       # Core program handling face recognition
├─ login.py                      # GUI login system
├─ Attendance.csv                # Attendance log file
├─ README.md                     # Project documentation
└─ requirements.txt              # Project dependencies

### How to Use

i.Launch the system by running login.py.

2.Log in as an admin (credentials can be predefined in the system).

3.Add new student images to the college_images folder.

4.Start the face recognition process from the GUI.

5.Attendance is automatically marked in Attendance.csv.

6.Generate reports as needed.

### Contributing

Contributions are welcome! You can:

Improve face recognition accuracy

Add database support (MySQL/PostgreSQL)

Enhance GUI design

Implement email notifications for attendance

### Contact

For questions, suggestions, or collaboration, reach out to:

Manoj Kumar Mandal
Email: manojkumarmandal1111@gmail.com
contact no:- 8404970494
GitHub: https://github.com/manoj333565
