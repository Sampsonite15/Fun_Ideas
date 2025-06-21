from datetime import date

baseline_date = date(2024, 4, 1)

# Example baseline prices from April 1st, 2024
baseline_prices = {
    "CocaCola_12pack": 7.99,
    "Gasoline_gallon": 2.73,
    "GitHub_Subscription": 10.0,
    "FastFood_Meal": 8.75,
    "Coffee_kCup20_pack": 17.99
}

# Today’s prices could be fetched or entered manually
today_prices = {
    "CocaCola_12pack": 8.69,
    "Gasoline_gallon": 2.90,
    "GitHub_Subscription": 10.0,
    "FastFood_Meal": 9.25,
    "Coffee_kCup20_pack": 26.99
    
}

today = date.today()
days_since_baseline = (today - baseline_date).days

print(f"Tracking drift from {baseline_date} — {days_since_baseline} days ago")

from datetime import date

# Baseline and current gas prices
baseline_price = 2.73
current_price = 2.90
days_elapsed = 446

# Inflation calculation
price_change = current_price - baseline_price
percent_change = (price_change / baseline_price) * 100

# Output
print(f"⛽ Gasoline has increased by ${price_change:.2f} "
      f"({percent_change:.2f}%) over the past {days_elapsed} days "
      f"since your baseline on April 1, 2024.")

# Coffee prices
coffee_baseline = 17.99
coffee_current = 26.99

coffee_change = coffee_current - coffee_baseline
coffee_percent = (coffee_change / coffee_baseline) * 100

print(f"☕ Coffee pods have increased by ${coffee_change:.2f} "
      f"({coffee_percent:.2f}%) since April 1, 2024.")
