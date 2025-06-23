# 🧪 ETL Pipeline using Pandas and Scikit-learn

This repository contains a simple ETL (Extract, Transform, Load) pipeline implemented using Python, Pandas, and Scikit-learn.

---

## 📁 Files Included

- `data.csv` — Sample raw dataset containing missing values and numeric/categorical columns.
- `etl_pipeline.py` — A Python script to run the ETL pipeline.
- `etl_pipeline_notebook.ipynb` — A Jupyter Notebook version of the same ETL process.
- `cleaned_data.csv` — Output file after running the ETL process (created after execution).

---

## 🚀 What This Project Does

This project:
- Extracts data from a CSV file
- Transforms the data by:
  - Dropping missing values
  - Scaling numeric features using `StandardScaler`
- Loads (saves) the cleaned data to a new CSV file

---

## 🔧 Requirements

- Python 3.x
- Pandas
- Scikit-learn

Install them using:

```bash
pip install pandas scikit-learn

📌 How to Run
Option 1: Run the Python Script
bash
Copy
Edit
python etl_pipeline.py
📓 Option 2: Use the Jupyter Notebook
Open etl_pipeline_notebook.ipynb in Jupyter

Run all cells

The cleaned data will be saved as cleaned_data.csv

💡 Example Output
Original Data:

id	age	salary	department
1	25	50000	HR
2	30	60000	IT
…	…	…	…

Transformed Data (after scaling & cleaning):

id	age	salary
…	…	…

📂 Use Case
This project demonstrates a basic data engineering workflow. It is ideal for:

Beginners learning about ETL

Preprocessing before machine learning

Data cleaning steps in data science pipelines










