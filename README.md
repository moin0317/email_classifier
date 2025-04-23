# 📧 Email Classifier API

A FastAPI application to classify customer support emails into predefined categories and mask PII entities using regex.

## 🚀 Features
- PII masking: email, phone, card, CVV, names, DOB, Aadhar, etc.
- Multi-class classification via RandomForest
- RESTful API with FastAPI + Docker
- Interactive docs at `/docs`

## 📦 Project Structure
email_classifier_project/ 
├── app.py
├── api.py 
├── models.py 
├── utils.py 
├── train_model.py 
├── requirements.txt 
├── Dockerfile 
└── classifier_model/ 
    └── email_classifier.pkl

 
 The trained model file email_classifier.pkl (≈ 100MB) is excluded from this repository.
It’s deployed directly on Hugging Face Space.

