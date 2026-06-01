# Task 5: Ticket Pricing
# Run this file using the command: python task5_ticket_pricing.py

# Instructions:
# Determine the ticket price of a movie based on age:
# - Age < 12 -> Child Ticket ($5 / Rs 100)
# - Age < 60 -> Adult Ticket ($12 / Rs 250)
# - Else -> Senior Citizen Ticket ($8 / Rs 150)

# ----------------- Write Your Code Below -----------------

age = int(input("Enter age: "))

if age < 12:
  print("Ticket Category: Child")
  print("Price: Rs 100")
elif age < 60:
  print("Ticket Category: Adult")
  print("Price: Rs 250")
else:
  print("Ticket Category: Senior")
  print("Price: Rs 150")
