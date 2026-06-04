# Task 5: Challenge
# Run this file using the command: python task5_prime_check.py

# Instructions:
# Write a function called `is_prime` that checks if a number is a prime number.
# Return True if it is prime, and False otherwise.
# A prime number is a number greater than 1 that is only divisible by 1 and itself.
# Take a number from the user, call the function, and print "Prime" or "Not Prime".

# Concept Explained:
# To check if `n` is prime, loop from 2 to `n-1`.
# If `n % i == 0` for any `i` in that range, it's NOT prime (return False immediately).
# If the loop finishes without finding any divisors, it IS prime (return True).

# ----------------- Write Your Code Below -----------------

def is_prime(number):
    if number <= 1:
        return False
        
    for i in range(2, number):
        if number % i == 0:
            return False # Found a divisor
            
    return True # No divisors found

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

# ---------------------------------------------------------
# Expected Output (for 7):
# Enter a number: 7
# Prime

# Expected Output (for 10):
# Enter a number: 10
# Not Prime
