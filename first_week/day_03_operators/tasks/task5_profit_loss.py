# Task 5: Profit or Loss Calculator
# Run this file using the command: python task5_profit_loss.py

# 📝 Instructions:
# Accept Cost Price (CP) and Selling Price (SP) from user.
# Calculate and print if it's a Profit or Loss, along with the respective amount.

# ----------------- Write Your Code Below -----------------

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit = {int(profit)}")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"Loss = {int(loss)}")
else:
    print("No Profit, No Loss")

# ---------------------------------------------------------
# Expected Output (e.g. SP=1000, CP=800):
# Enter Cost Price: 800
# Enter Selling Price: 1000
# Profit = 200
