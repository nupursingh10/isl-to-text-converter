# 🔤 Indian Sign Language (ISL) to Text Converter

🚀 A real-time Indian Sign Language (ISL) recognition system using CNN and OpenCV for gesture-to-text conversion.

---

## 📌 Project Overview

This project detects Indian Sign Language hand gestures in real time using computer vision and deep learning.  
The system captures webcam input, processes the hand region, and predicts the corresponding ISL alphabet.

The goal is to help bridge communication between hearing-impaired individuals and non-sign language users.

---

## ✨ Features

- Real-time webcam prediction  
- CNN-based gesture classification  
- Automatic train-test dataset split  
- ROI-based hand cropping for better accuracy  
- Lightweight and beginner-friendly pipeline  

---

## 🧠 Tech Stack

- Python  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Matplotlib  

---

## ⚙️ Prerequisites

Before running this project, ensure you have:

- Python 3.8 or above  
- Working webcam  
- Windows/Linux/Mac supported  
- pip installed  

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/nupursingh10/isl-to-text-converter.git
cd isl-to-text-converter
```

Install dependencies:

```bash
pip install tensorflow opencv-python numpy matplotlib
```

---

## 📊 Dataset Details

- Dataset sourced from Mendeley and manually preprocessed  
- Images organized class-wise (A–Z, digits optional)  
- Automatic 80/20 train-test split implemented  
- Images resized to **64×64** during training  

### Expected Dataset Structure

```
dataset/
   A/
   B/
   C/
   ...
```

---

## 🏋️‍♀️ Train the Model

Run:

```bash
python train_model.py
```

This will:

- Load dataset  
- Train CNN model  
- Save model as `isl_model.h5`  

---

## 🎥 Run Real-Time Prediction

Run:

```bash
python predict.py
```

### What happens:

- Webcam opens  
- Green box shows Region of Interest  
- Place hand inside the box  
- Predicted letter appears on screen  
- Press **q** to exit  

---

## 📊 Model Performance

- Training Accuracy: ~100%  
- Validation Accuracy: ~100%  

---

## 📁 Project Structure

```
isl-to-text-converter/
│
├── train_model.py
├── predict.py
├── split_dataset.py
├── images/
├── README.md
└── requirements.txt (recommended)
```

---

## 📷 Demo

![Demo](images/demo1.png)

---

## 🚧 Future Improvements

- MediaPipe hand detection  
- Word and sentence formation  
- Web deployment (Streamlit/Flask)  
- Mobile application integration  
- Support for full ISL vocabulary  

---

## 🛠️ Troubleshooting

**Issue:** Webcam not opening  
- Ensure camera permissions are enabled  

**Issue:** Wrong predictions  
- Keep hand inside green box  
- Use plain background  
- Ensure good lighting  

**Issue:** Module not found  
- Run `pip install -r requirements.txt`

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the repository and submit pull requests.

---

## 📄 License

This project is for educational purposes.

---

## 👩‍💻 Author

**Nupur Singh**  
B.Tech Final Year Student  
Interested in AI, Computer Vision & Web Development

---

⭐ If you found this helpful, consider giving the repo a star!
