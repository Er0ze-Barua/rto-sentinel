# RTO Sentinel | AI-Powered Fraud Detection System

**RTO Sentinel** is a full-stack Machine Learning application developed to address the **"Return to Origin" (RTO) Risk Detection** problem statement originally open-sourced by Razorpay.

---

## 📄 Project Overview

The system is designed to tackle the financial losses incurred by e-commerce merchants when orders are returned before delivery. Using a specialized Kaggle dataset containing historical transaction details and fraud markers, the system analyzes patterns in customer behavior and transaction metadata to predict RTO risk before shipment.

---

## 🏗️ Architecture & Tech Stack

The project utilizes a **Microservices Architecture** to decouple the machine learning inference from the user interface:

- **The Brain (FastAPI):** High-performance inference API with validation via Pydantic  
- **The Face (Django):** Web dashboard for merchant-side analytics  
- **The Engine (Random Forest):** Scikit-learn classifier trained on transaction data  

---

## 🐳 Containerized Architecture

The entire system is fully containerized using **Docker and Docker Compose**, enabling seamless multi-service deployment.

Architecture flow:

Django (Frontend) → FastAPI (Backend) → ML Model

---

## 🚀 Running the Project (Docker)

### 1. Clone the repository

git clone https://github.com/Er0ze-Barua/rto-sentinel.git  
cd rto-sentinel

### 2. Run using Docker Compose

docker-compose up --build

---

## 🌐 Access the Application

- Frontend (Django): http://localhost:8001  
- Backend API Docs (FastAPI): http://localhost:8000/docs  

---

## 📊 Key Metrics

- Accuracy: 87.2%  
- Precision (Fraud Class): 0.92  
- Recall (Fraud Class): 0.85  
- Architecture: RESTful API with Decoupled Frontend/Backend  

---

## 💡 Highlights

- Real-time risk scoring for incoming orders  
- Microservice-based architecture (frontend + backend separation)  
- Dockerized deployment using Docker Compose  
- Reproducible environment across systems  
- Clean UI for interaction and analysis  

---

## ⚠️ Notes

- The trained model file (.pkl) is not included due to size constraints  
- You may need to retrain or place the model manually  
