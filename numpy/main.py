#importing libraries

import numpy as np
import matplotlib.pyplot as plt

#Data: [restaurant_id , 2021 ,  2022 , 2023 , 2024]

sales_data = np.array ([
    [1, 150000, 180000, 220000, 250000],
    [2,  120000, 140000, 160000, 190000],
    [3,  200000, 230000, 260000, 300000],
    [4, 180000, 210000, 240000, 270000],
    [5,  160000, 185000, 205000, 230000]

])
print("\n")

#numpy theories in real world scenarios/databases

print("=== Zomato sales report ===")

print("\nSales data shape: " ,sales_data.shape)

print("Sales of first three restaurant:\n",sales_data[0:3])

#total sales
Total_sales = np.sum(sales_data[:,1:], axis=0)
print("Total sales per year: ", Total_sales)

#minimum sale
Min_sales = np.min(sales_data[:,1:], axis=1)
print("Minimum sales per restaurant: ", Min_sales)

#maximum sale
Max_sales = np.max(sales_data[:,1:], axis=0)
print("Maximum sales per year: ", Max_sales)

#average sale
Average_sales = np.average(sales_data[:,1:], axis=1)
print("Average sales per restaurat: ", Average_sales)

#cumulative sales
cumsum = np.cumsum(sales_data[:,1:], axis=1)
print("Cumulative sum: ",cumsum)

#graph for cumulative sales
years = [2021, 2022, 2023, 2024]
plt.figure(figsize=(10, 6))
plt.plot(years ,np.average(cumsum, axis=0), marker ='o')
plt.xticks(years)
plt.title("Average Cumulative sales accross all restaurant")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()