# Student Performance Analysis 📊

An end-to-end student performance analysis project built using **Python** and **MySQL**.  
The project loads student marks from a CSV file, processes the data, stores it in a SQL database, and generates performance insights.

---

## 🚀 Project Overview

This project demonstrates a simple but professional **data pipeline**:

- Load raw student data from a CSV file  
- Clean and process the data using Python (Pandas)  
- Store and retrieve data from a MySQL database  
- Calculate average marks and performance status (Pass / Average / Fail)  
- Designed with modular and extensible code structure  

---

## ✨ Features

- CSV-based data ingestion  
- Support for multiple subjects per student  
- Average marks calculation  
- Performance status classification  
- MySQL database integration  
- Clean, modular Python code  

---

## 🛠 Tech Stack

- Python 3  
- Pandas  
- MySQL  
- Git & GitHub  

---

## 📁 Project Structure

student-performance-analysis/ │ ├── data/ │   ├── raw/                # Input CSV files │   └── src/                # Core application logic │       ├── data_loader.py │       ├── data_cleaning.py │       ├── analysis.py │       ├── prediction.py │       ├── db_connection.py │       ├── db_writer.py │       └── db_reader.py │ ├── outputs/                # Generated outputs (optional) ├── main.py                 # Entry point of the pipeline ├── requirements.txt └── README.md

---

## ⚙️ Setup & Run

### 1️⃣ Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2️⃣ Configure MySQL
Create a MySQL database
Update database credentials in db_connection.py

3️⃣ Run the project
python main.py
This will:
Load data from CSV
Insert data into MySQL
Fetch processed results
Display student performance summary

📊 Sample Output
<img width="4160" height="782" alt="image" src="https://github.com/user-attachments/assets/5dbab40f-7823-491c-bb04-b59791c054be" />

🔮 Future Improvements
Add data visualizations and dashboards
Introduce automated testing
Enhance performance logic using ML
Add REST API support

🙌 Author
Himanshu Gupta
Building projects to learn data analysis and backend integration 🚀

⭐ If you like this project, consider starring the repository!

---


