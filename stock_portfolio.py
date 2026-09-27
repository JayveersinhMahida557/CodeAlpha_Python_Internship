print("====================================")
print("     STOCK PORTFOLIO TRACKER")
print("====================================")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("\nAvailable Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        stock_total = stock_prices[stock_name] * quantity
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        total_investment += stock_total

        print(f"Added {quantity} shares of {stock_name}.")
        print(f"Investment for this stock: ${stock_total}")

    except ValueError:
        print("Please enter a valid whole number for quantity.")

print("\n====================================")
print("          PORTFOLIO SUMMARY")
print("====================================")

if not portfolio:
    print("No stocks were added.")
else:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        print(f"{stock}: {quantity} shares x ${price} = ${value}")

    print("------------------------------------")
    print(f"Total Investment: ${total_investment}")

print("Thank you for using Stock Portfolio Tracker!")
