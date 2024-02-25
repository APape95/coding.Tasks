# Create a list called menu with 4 items on.
# Create 2 dictionaries one for price and stock.
# Each should have the 4 items on with stock levels and pricing.
# Then calculate the total value of all items you have in stock.

# List of what is being sold in the cafe
menu = "Coffee", "Tea", "Toast", "Porriage"

# Dictionary of amount of each iteam we have in stock.
stock = {
    "Coffee": 20,
    "Tea": 30,
    "Toast": 40,
    "Porriage": 10
    }

# Dictionary of how much each item costs.
price = {
    "Coffee": 4.50,
    "Tea": 2.75,
    "Toast": 2.00,
    "Porriage": 3.50
    }


# Stock value of each item by multiplying the amount of stock by the cost.
coffee_value = (stock["Coffee"] * price["Coffee"])
tea_value = (stock["Tea"] * price["Tea"])
toast_value = (stock["Toast"] * price["Toast"])
porriage_value = (stock["Porriage"] * price["Porriage"])

# Add all items together to give us the total stock value.
stock_value = coffee_value + tea_value + toast_value + porriage_value

# Printing the total value to 2 desimal places as it is currency.
print(f"The total value of all stock is £{stock_value:.2f}")