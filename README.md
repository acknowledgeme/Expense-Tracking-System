# Expense Management System

An Expense Management System built with a **Streamlit frontend** and a **FastAPI backend** that allows users to manage expenses and download reports in CSV format.

---

## Features
- Add, update, and delete expenses
- Category-wise expense tracking
- Monthly expense analytics
- Interactive dashboard using Streamlit
- RESTful APIs using FastAPI
- ✅ Download expense reports as **CSV**
- Test cases for backend and frontend

---

## Tech Stack
- Python
- FastAPI
- Streamlit
- MySQL
- PyTest

---
## 📁 Project Structure
expense-management-system/
│
├── backend/ # FastAPI backend server
├── frontend/ # Streamlit frontend application
├── tests/ # Test cases
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---



## Setup Instructions

### 
1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the FastAPI backend
uvicorn server.server:app --reload

4️⃣ Run the Streamlit frontend
streamlit run frontend/app.py

## CSV Download

Users can download their expense data as a CSV file directly from the application for offline analysis and record keeping.

##Run Tests
pytest

