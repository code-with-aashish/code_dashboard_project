import matplotlib.pyplot as plt

# Sample data
categories = ["Baby Products", "Groceries", "Household Items", "Clothing", "Electronics"]
average_spend = [120, 75, 50, 100, 200]  # Average spend per customer in each category

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(categories, average_spend, color='skyblue', edgecolor='black')

# Adding titles and labels
plt.title("Average Spend per Customer by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Spend (USD)")

# Show grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
