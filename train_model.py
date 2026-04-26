import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
labels = []
label_map = {}
current_label = 0

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    label_map[current_label] = person

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        img = cv2.imread(img_path)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (200, 200))

        faces.append(gray)
        labels.append(current_label)

    current_label += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))

os.makedirs("model", exist_ok=True)

recognizer.save("model/face_model.yml")
np.save("model/labels.npy", label_map)

print("✅ Training Complete!")