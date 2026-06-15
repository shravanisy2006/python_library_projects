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

#total sales per year
total_sales = np.sum(sales_data[:,1:], axis=0)
#axis=0 → perform operation column-wise (years)
print("Total sales per year: ", total_sales)

#total sales per restaurant
total = np.sum(sales_data[:,1:],axis=1)
#axis=1 → perform operation row-wise (restaurants)
print("Total sales per restaurant: ", total)

#minimum sale
min_sales = np.min(sales_data[:,1:], axis=1)
print("Minimum sales per restaurant: ", min_sales)

#maximum sale
max_sales = np.max(sales_data[:,1:], axis=0)
print("Maximum sales per year: ", max_sales)

#top restaurant
top_restaurant = np.argmax(total)
print("The top restaurant: ",sales_data[top_restaurant, 0])

#growth rate
growth = np.diff(sales_data[:,1:],axis=1)
print("Yearly Growth: ",growth)

#average sale
average_sales = np.average(sales_data[:,1:], axis=1)
print("Average sales per restaurat: ", average_sales)

#cumulative sales
cumsum = np.cumsum(sales_data[:,1:], axis=1)
print("Cumulative sum: ",cumsum)

#graph for cumulative sales
years = [2021, 2022, 2023, 2024]

for i in range(len(sales_data)):
    plt.plot(
        years ,
        sales_data[i,1:], 
        marker ='o',
        label = f"Restaurant{int(sales_data[i,0])}"
        )
plt.xticks(years)
plt.title("Restaurant Sales Trend")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.show()