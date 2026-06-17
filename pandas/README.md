# 🎓 Student Performance Analysis using Pandas

A beginner-friendly data analysis project built using **Pandas** to analyze student academic performance and attendance records.

## 📌 Project Overview

This project demonstrates how Pandas can be used to organize, filter, and analyze tabular data.

Using a dataset of students from different departments, the program performs performance analysis and generates useful insights.

---

## 📊 Dataset Structure

The dataset contains:

* Student ID
* Name
* Department
* Marks
* Attendance

Example:

| Student ID | Name   | Department | Marks | Attendance |
| ---------- | ------ | ---------- | ----- | ---------- |
| 101        | Shreya | CSE        | 83    | 53.9       |
| 102        | Rahil  | Mech       | 79    | 78         |
| 103        | Sparsh | CSE        | 86    | 97         |

---

## 🚀 Features Implemented

### 1. Top Performing Students

Identifies the top 3 students based on marks using:

```python
df.nlargest()
```

### 2. Bottom Performing Students

Identifies the bottom 3 students based on marks using:

```python
df.nsmallest()
```

### 3. Above Average Students

Calculates the average marks and filters students scoring above the average.

### 4. Department-wise Performance Analysis

Calculates average marks for each department using:

```python
groupby()
```

---

## 🧠 Pandas Concepts Used

* DataFrame Creation
* Data Selection
* Filtering
* Aggregation Functions
* `mean()`
* `groupby()`
* `nlargest()`
* `nsmallest()`
* Boolean Indexing

---

## 🎯 Learning Outcomes

Through this project, I learned:

* How to work with structured datasets using Pandas
* How to filter and analyze data efficiently
* How to generate meaningful insights from tabular data
* The importance of grouping and aggregation in data analysis

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* NumPy

---

## ▶️ How to Run

```bash
pip install pandas numpy

python student_performance_analysis.py
```

---

## 📚 Project Type

Beginner-Friendly Data Analysis Project using Pandas.
