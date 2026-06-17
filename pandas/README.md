# 🎓 Student Performance Analysis using Pandas

A beginner-friendly data analysis project built using **Pandas** and **Matplotlib** to analyze student academic performance and attendance records.

## 📌 Project Overview

This project demonstrates how Pandas can be used to organize, filter, analyze, and visualize tabular data.

Using a dataset of students from different departments, the program performs performance analysis, identifies top performers, evaluates attendance records, and generates meaningful insights through data visualization.

---

## 📊 Dataset Structure

The dataset contains the following information:

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

### 5. Attendance Analysis

Identifies students with attendance greater than 85%.

### 6. Department Toppers

Finds the highest-scoring student from each department using:

```python
idxmax()
```

### 7. Best Performing Department

Determines the department with the highest average marks.

### 8. Data Visualization

Generates a bar chart showing average marks scored by each department.

---

## 🧠 Pandas Concepts Used

* DataFrame Creation
* Data Selection
* Filtering
* Boolean Indexing
* Aggregation Functions
* Conditional Selection
* GroupBy Operations
* `mean()`
* `nlargest()`
* `nsmallest()`
* `idxmax()`
* `groupby()`

---

## 📈 Visualization Output

The project generates a bar chart displaying the average marks scored by students in each department.

Example:

```python
dept_avg.plot(kind='bar')
```

You can add the generated graph image below after running the project:

```markdown
![Department Average Marks](avg_marks_analysis.png)
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

* How to work with structured datasets using Pandas
* How to filter and analyze data efficiently
* How to perform grouping and aggregation operations
* How to identify trends and top performers in a dataset
* How to generate meaningful insights from tabular data
* How to visualize data using Matplotlib

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install required libraries:

```bash
pip install pandas numpy matplotlib
```

3. Run the program:

```bash
python student_performance_analysis.py
```

---

## 📂 Project Structure

```text
student_performance_analysis/
│
├── student_performance_analysis.py
├── avg_marks_analysis.png
└── README.md
```

---

## 📚 Project Type

Beginner-Friendly Data Analysis Project using Pandas and Matplotlib.

---

## 🔮 Future Improvements

* Add department-wise attendance analysis
* Export results to CSV files
* Create interactive visualizations
* Build a dashboard using Streamlit
* Analyze larger real-world datasets

---

### ⭐ Key Takeaway

This project demonstrates how Pandas can be used to clean, analyze, and visualize student performance data, making it a strong foundation for future Machine Learning and Data Analysis projects.
