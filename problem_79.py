# Problem 79: Calculate compound interest
# Find and fix the error

def compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / n) ** (n * time)
    return amount - principal
print(f"Compound Interest: {compound_interest(p, r, t, n)}")
