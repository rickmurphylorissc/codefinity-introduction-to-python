prices = [29.99, 45.50, 12.75, 38.20]
discount_factors = [0.10, 0.20, 0.15, 0.05]

for i in range(len(prices)):
    prices[i] -= prices[i] * discount_factors[i]
    print(f"Updated price for item {i}: ${prices[i]:.2f}")