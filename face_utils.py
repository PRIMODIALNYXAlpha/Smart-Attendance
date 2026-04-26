import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("model/face_model.yml")

label_map = np.load("model/labels.npy", allow_pickle=True).item()

def recognize_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (200, 200))

    label, confidence = recognizer.predict(gray)

    if confidence < 100:
        return label_map[label]
    else:
        return "Unknown"