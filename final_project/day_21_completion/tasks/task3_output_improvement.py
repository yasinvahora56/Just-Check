# Task 3: Final Output Improvement
# Run this file using the command: python task3_output_improvement.py

# Instructions:
# Make the print statements look more professional.
# Use standard string formatting like centering (`.center()`), borders (`=`), and right-aligning prices (`>`).

# ----------------- Write Your Code Below -----------------

def professional_view(expenses):
    # Print a nice header
    print("\n" + "="*40)
    print("EXPENSE REPORT".center(40))
    print("="*40)
    
    if not expenses:
        print("No expenses recorded yet.".center(40))
    else:
        # Print column headers
        # <20 means left-align with 20 spaces
        # >15 means right-align with 15 spaces
        print(f"{'Category':<20} | {'Amount':>15}")
        print("-" * 40)
        
        for exp in expenses:
            # Format amount with 2 decimal places
            formatted_amount = f"${exp['amount']:.2f}"
            print(f"{exp['category']:<20} | {formatted_amount:>15}")
            
        print("-" * 40)
        total = sum(exp["amount"] for exp in expenses)
        print(f"{'TOTAL':<20} | {f'${total:.2f}':>15}")
        
    print("="*40 + "\n")

# Simulating the feature
if __name__ == "__main__":
    sample_data = [
        {"amount": 50.5, "category": "Food"},
        {"amount": 100, "category": "Travel"},
        {"amount": 12.99, "category": "Coffee"}
    ]
    professional_view(sample_data)
