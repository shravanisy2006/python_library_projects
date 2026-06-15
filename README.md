# 🍽️ Zomato Restaurant Sales Analysis using NumPy & Matplotlib

Part of my Python Libraries Learning Series, where I build small projects to understand NumPy, Matplotlib, Pandas, and Machine Learning concepts through practical examples.

## 📌 Project Overview

This project demonstrates how **NumPy** and **Matplotlib** can be used to analyze restaurant sales data in a real-world business scenario.

Using sales records of multiple restaurants from **2021 to 2024**, the program performs data analysis operations and visualizes sales trends.

---

## 📊 Dataset Structure

The dataset is stored as a NumPy array in the following format:

```
[restaurant_id, 2021_sales, 2022_sales, 2023_sales, 2024_sales]
```

Example:

```python
[
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 140000, 160000, 190000],
    [3, 200000, 230000, 260000, 300000],
    [4, 180000, 210000, 240000, 270000],
    [5, 160000, 185000, 205000, 230000]
]
```

---

## 🚀 Features Implemented

### 1. Dataset Information

* Display dataset shape using `.shape`
* Access specific records using array slicing

### 2. Sales Analysis

* Total sales per year
* Total sales per restaurant
* Minimum sales per restaurant
* Maximum sales per year
* Average sales per restaurant

### 3. Performance Analysis

* Identify the top-performing restaurant using `np.argmax()`
* Calculate yearly sales growth using `np.diff()`
* Compute cumulative sales using `np.cumsum()`

### 4. Data Visualization

* Plot yearly sales trends for each restaurant
* Add titles, labels, legends, and grids for better readability

---

## 🧠 NumPy Concepts Used

| Concept                               | Function Used      |
| ------------------------------------- | ------------------ |
| Creating Arrays                       | `np.array()`       |
| Array Shape                           | `.shape`           |
| Array Slicing                         | `[:, 1:]`, `[0:3]` |
| Sum Operations                        | `np.sum()`         |
| Minimum Values                        | `np.min()`         |
| Maximum Values                        | `np.max()`         |
| Average Calculation                   | `np.average()`     |
| Finding Maximum Index                 | `np.argmax()`      |
| Difference Between Consecutive Values | `np.diff()`        |
| Cumulative Sum                        | `np.cumsum()`      |
| Axis Operations                       | `axis=0`, `axis=1` |

---

## 📈 Matplotlib Concepts Used

| Concept              | Function Used  |
| -------------------- | -------------- |
| Create Figure        | `plt.figure()` |
| Line Plot            | `plt.plot()`   |
| Markers              | `marker='o'`   |
| Custom X-axis Labels | `plt.xticks()` |
| Graph Title          | `plt.title()`  |
| X-axis Label         | `plt.xlabel()` |
| Y-axis Label         | `plt.ylabel()` |
| Grid                 | `plt.grid()`   |
| Legend               | `plt.legend()` |
| Display Plot         | `plt.show()`   |

---

## 📊 Visualization Output

The program generates a line chart showing the **sales trend of each restaurant from 2021 to 2024**, helping identify growth patterns and top performers.

---

## 🎯 Learning Outcomes

By completing this project, I learned:

* How to manipulate multidimensional arrays using NumPy
* The importance of `axis=0` (column-wise operations) and `axis=1` (row-wise operations)
* Techniques for performing business data analysis
* How to visualize data effectively using Matplotlib
* Applying Python libraries to real-world scenarios

---

## 🛠️ Technologies Used

* Python 3.x
* NumPy
* Matplotlib

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install dependencies:

```bash
pip install numpy matplotlib
```

3. Run the program:

```bash
python main.py
```

---

## 📚 Project Type

Beginner-friendly Data Analysis Project using NumPy and Matplotlib.
