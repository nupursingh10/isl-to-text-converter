import tensorflow as tf
import cv2
import numpy as np

# Load model
model = tf.keras.models.load_model("isl_model.h5")

# Class labels (IMPORTANT — update if needed)
import os

# Load class names automatically
classes = sorted(os.listdir("data/train"))
print("Classes:", classes)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    h, w, _ = frame.shape

# Define center crop box
    size = 300
    x1 = w//2 - size//2
    y1 = h//2 - size//2
    x2 = x1 + size
    y2 = y1 + size

    roi = frame[y1:y2, x1:x2]

# Draw rectangle on screen
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

    img = cv2.resize(roi, (64,64))
    img = img / 255.0
    img = np.reshape(img, (1,64,64,3))
    pred = model.predict(img, verbose=0)
    label = classes[np.argmax(pred)]

    cv2.putText(frame, label, (50,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0,255,0), 2)

    cv2.imshow("ISL Prediction", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()