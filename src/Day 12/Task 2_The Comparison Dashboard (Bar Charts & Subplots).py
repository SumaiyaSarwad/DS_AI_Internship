#Task 2: The Comparison Dashboard (Bar Charts & Subplots)

import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Categories")
plt.ylabel("Sales")
plt.xticks(rotation=20)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [200, 250, 300, 280, 350]

plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
