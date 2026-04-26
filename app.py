import streamlit as st
import cv2
import numpy as np
from face_utils import recognize_face
from email_utils import send_email
from excel_utils import mark_attendance_excel
import sqlite3
from datetime import datetime
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Smart Attendance", layout="wide")

st.title("📸 Smart Attendance System")

 
email = st.text_input("Enter Email")
branch = st.text_input("Enter Branch")

option = st.selectbox("Select Mode", ["Upload Image", "Live Camera"])

def save_attendance(name, email, branch):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance VALUES (?, ?, ?, ?)",
        (name, email, date_str, time_str)
    )

    conn.commit()
    conn.close()

    mark_attendance_excel(name, email, branch, date_str, time_str)
    send_email(email, name)

    st.success("✅ Attendance Marked, Email Sent!")

if option == "Upload Image":
    file = st.file_uploader("Upload Image")

    if file:
        image = Image.open(file)
        image = np.array(image)
        image = cv2.resize(image, (200, 200))

        name = recognize_face(image)

        st.success(f"Detected: {name}")

        if st.button("Mark Attendance"):
            if email == "" or branch == "":
                st.error("Enter email & branch")
            else:
                save_attendance(name, email, branch)

if option == "Live Camera":
    run = st.checkbox("Start Camera")

    if run:
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Camera error")
                break

            face = cv2.resize(frame, (200, 200))
            name = recognize_face(face)

            stframe.image(frame, channels="BGR")
            st.write(f"Detected: {name}")

            if st.button("Mark Attendance"):
                if email == "" or branch == "":
                    st.error("Enter email & branch")
                else:
                    save_attendance(name, email, branch)
                    break

        cap.release()

st.markdown("---")
st.header("📊 Attendance Dashboard")

conn = sqlite3.connect("attendance.db")
df = pd.read_sql_query("SELECT * FROM attendance", conn)
conn.close()

if not df.empty:

    selected_date = st.date_input("Filter by Date", datetime.now().date())

    df["Date"] = pd.to_datetime(df["date"])
    filtered_df = df[df["Date"].dt.date == selected_date]

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(df))
    col2.metric("Today Attendance", len(filtered_df))
    col3.metric("Unique Students", df["name"].nunique())

    st.markdown("---")

    st.subheader("📋 Attendance Table")
    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Attendance Count")
        st.bar_chart(df["name"].value_counts())

    with col2:
        st.subheader("📊 Distribution")
        st.write(df["name"].value_counts().plot.pie(autopct='%1.1f%%'))

    st.markdown("---")
    st.subheader("⬇️ Download Attendance")

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "attendance.csv", "text/csv")

else:
    st.warning("No attendance data available")