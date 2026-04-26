# 📸 Smart Attendance System

A complete **AI-based Smart Attendance System** built using Python, OpenCV, and Streamlit that automates attendance marking using face recognition, along with email notifications and real-time analytics.

---

## 🚀 Overview

The Smart Attendance System replaces traditional manual attendance methods with an intelligent, automated solution. It detects and recognizes faces using computer vision techniques and records attendance in both a database and an Excel sheet.

Additionally, it provides a real-time dashboard with analytics and sends email confirmations upon successful attendance marking.

---

## ✨ Features

* 🎯 Face Recognition using OpenCV (LBPH Algorithm)
* 📤 Upload Image & 📷 Live Camera Detection
* 📧 Email Notification after attendance marking
* 📊 Excel Sheet Storage (attendance.xlsx)
* 🗄️ SQLite Database Storage (attendance.db)
* 📈 Real-time Dashboard with Graphs & Metrics
* 🔍 Filter attendance by date
* 📥 Download attendance as CSV
* 🚫 Duplicate attendance prevention (same day)

---

## 🛠️ Technologies Used

* **Python** – Core programming language
* **OpenCV** – Face detection & recognition
* **Streamlit** – Web-based UI & dashboard
* **SQLite** – Lightweight database
* **Pandas** – Data manipulation & analytics
* **OpenPyXL** – Excel file handling
* **SMTP (Gmail)** – Email notifications

---

## 📁 Project Structure

```
Smart-Attendance/
│
├── dataset/                # Face images dataset
├── model/                  # Trained face recognition model
│
├── app.py                  # Main Streamlit application
├── train_model.py          # Model training script
├── face_utils.py           # Face recognition logic
├── email_utils.py          # Email sending logic
├── excel_utils.py          # Excel handling
├── db_init.py              # Database setup
│
├── attendance.db           # SQLite database (auto-generated)
├── attendance.xlsx         # Excel file (auto-generated)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/PRIMODIALNYXAlpha/Smart-Attendance.git
cd Smart-Attendance
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Prepare Dataset

Create dataset like:

```
dataset/
   ├── Person1/
       ├── img1.jpg
       ├── img2.jpg
   ├── Person2/
```

👉 Each folder = one person
👉 Add 15–30 clear face images

---

### 4️⃣ Train Model

```
python train_model.py
```

---

### 5️⃣ Initialize Database

```
python db_init.py
```

---

### 6️⃣ Run Application

```
streamlit run app.py
```

---

## 📊 Dashboard Features

* Total attendance records
* Daily attendance count
* Unique students count
* Bar chart (attendance per person)
* Pie chart (distribution)
* Filter by date
* Download attendance report

---

## 📧 Email Configuration

To enable email notifications:

1. Enable **2-Step Verification** in your Google Account
2. Generate a **Gmail App Password**
3. Update in `email_utils.py`:

```
sender_email = "your_email@gmail.com"
password = "your_app_password"
```

---

## 🧠 How It Works

1. Face image is captured (upload or camera)
2. Image is processed using OpenCV
3. LBPH algorithm recognizes the face
4. Attendance is marked if match is found
5. Data is stored in:

   * SQLite database
   * Excel file
6. Email notification is sent
7. Dashboard updates in real-time

---

## 📌 Advantages

* Eliminates manual attendance errors
* Fast and automated process
* Real-time analytics and monitoring
* Easy to use interface
* Scalable for classrooms or organizations

---

## 🚀 Future Enhancements

* 🔐 Login system (Admin/Student)
* 🌐 Cloud deployment (web access)
* 📱 Mobile compatibility
* 🎯 Improved face detection accuracy
* 📊 Advanced analytics dashboard

---

## 👨‍💻 Author

**Tarun SR**
Final Year Engineering Student

---

## 📄 License

This project is for educational purposes.
