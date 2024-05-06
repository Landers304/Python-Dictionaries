#Task 1:


import copy

# Given sales data
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# Create a deep copy of weekly_sales
copied_sales_data = copy.deepcopy(weekly_sales)

# Update the sales figure for "Electronics" in "Week 2" in the copied data
copied_sales_data["Week 2"]["Electronics"] = 18000

# Display the original and updated sales data
print("Original Sales Data:")
print(weekly_sales)
print("\nCopied and Updated Sales Data:")
print(copied_sales_data)
