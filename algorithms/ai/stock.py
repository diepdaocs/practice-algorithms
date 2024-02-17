# Write a simple program to predict stock prices using simple MCDA algorithm.
# What is MCDA?

def predict_next_day_price(prices_yesterday, prices_two_days_ago):
    prices = prices_yesterday + prices_two_days_ago
    return sum(prices) / len(prices)

print("Predicted price:", predict_next_day_price([10, 20, 30], [5, 4, 6]))
print("Expected output: [12.5]")
