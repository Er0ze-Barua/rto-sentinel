# RTO Sentinel | AI-Powered Fraud Detection System

**RTO Sentinel** is a full-stack Machine Learning application developed to address the **"Return to Origin" (RTO) Risk Detection** problem statement originally open-sourced by **Razorpay**. 

## 📄 Project Overview
The system is designed to tackle the financial losses incurred by e-commerce merchants when orders are returned before delivery. Using a specialized **Kaggle Dataset** containing historical transaction details and fraud markers, the system analyzes patterns in customer behavior and transaction metadata to predict RTO risk before shipment.

## 🏗️ Architecture & Tech Stack
The project utilizes a **Microservices Architecture** to decouple the machine learning inference from the user interface:

* **The Brain (FastAPI):** A high-performance inference API that validates data via Pydantic and serves model predictions with low latency.
* **The Face (Django):** A custom-designed web dashboard featuring a "Nights and Crimson" dark theme for merchant-side analytics.
* **The Engine (Random Forest):** A Scikit-Learn classifier trained on transaction history, achieving high precision in fraud detection.

## 📊 Key Metrics
* **Accuracy:** 87.2%
* **Precision (Fraud Class):** 0.92
* **Recall (Fraud Class):** 0.85
* **Architecture:** RESTful API with Decoupled Frontend/Backend

## 💡 Highlights
* **Real-time Risk Scoring:** Instant probability assessments for incoming orders.
* **Microservice Decoupling:** The model engine and the web UI are independent services, allowing for easier scalability and model updates.
* **Custom UI/UX:** Built with a cybersecurity-inspired aesthetic using glassmorphism and high-contrast design.
