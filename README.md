# 🎓 Smart Attendance Analytical Platform

An AI-powered Smart Attendance Analytical Platform developed using **Machine Learning**, **Deep Learning**, **Natural Language Processing (NLP)**, and **Generative AI**. The system helps educational institutions manage attendance, analyze student performance, predict dropout risks, and generate intelligent insights through an interactive Streamlit application.

---

## 📌 Project Overview

The Smart Attendance Analytical Platform provides an intelligent solution for monitoring and analyzing student attendance. It combines traditional attendance management with AI-powered analytics to help faculty identify at-risk students, understand attendance patterns, and improve academic performance.

---

## ✨ Features

### 👤 User Authentication
- Secure Login System
- Role-Based Access Control
- Admin Login
- Faculty Login
- Student Login

### 👨‍🎓 Student Management
- Add Student
- Edit Student
- Delete Student
- Search Student
- Download Student Report

### 📚 Subject Management
- Add Subject
- Edit Subject
- Delete Subject
- Subject-wise Attendance Dashboard

### 📊 Dashboard
- Total Students
- Attendance Statistics
- Safe vs Shortage Students
- Attendance Distribution
- Interactive Charts

### 🤖 Artificial Intelligence
- Decision Tree Classification
- LSTM Attendance Forecasting
- GRU Attendance Forecasting
- BERT Sentiment Analysis
- Gemini AI Chatbot

### 📈 Analytics
- Attendance Analysis
- Student Performance Analysis
- Subject-wise Reports
- Dropout Risk Prediction
- Student Sentiment Analysis

### 📄 Reports
- Student Reports
- PDF Report Generation
- Attendance Summary

---

## 🧠 AI Models Used

| Model | Purpose |
|--------|----------|
| Decision Tree | Attendance Classification |
| LSTM | Attendance Forecasting |
| GRU | Attendance Forecasting |
| BERT | Student Sentiment Analysis |
| Gemini AI | AI Chatbot & Recommendations |

---

## 🛠 Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### Database
- SQLite (Student & Subject Management)
- CSV (Analytics Modules)

### Libraries
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow
- Transformers
- ReportLab
- Google Generative AI

---

## 📁 Project Structure

```text
Smart_Attendance_Project/

├── app.py
├── auth.py
├── login.py
├── navigation.py
├── pages/
├── database/
├── attendance.csv
├── student_report.csv
├── student_feedback_sentiment.csv
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart_Attendance_Project.git
```

### Move into Project

```bash
cd Smart_Attendance_Project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔑 Login Roles

| Role | Access |
|------|---------|
| Admin | Full Access |
| Faculty | Student & Subject Management |
| Student | View Only |

---

## 📊 Project Workflow

```
User Login
      │
      ▼
Role Authentication
      │
      ▼
Dashboard
      │
      ├── Student Management
      ├── Subject Management
      ├── Attendance Analytics
      ├── Reports
      ├── AI Chatbot
      └── Sentiment Analysis
```

---

## 🎯 Future Enhancements

- Complete SQLite Migration
- MySQL Integration
- Face Recognition Attendance
- QR Code Attendance
- Email Notifications
- Parent Portal
- Faculty Portal
- Cloud Deployment
- Mobile Application

---

## 👨‍💻 Developer

**JAI KUMAR**

🎓 Rajalakshmi Engineering College

💻 B.Tech Information Technology

Project developed as part of the **PENTAS HUB Internship Program**.

---

## 📜 License

This project is developed for educational and internship purposes.