import matplotlib.pyplot as plt

class SmartphoneInventoryAgent:
    def __init__(self, avg_price, critical_stock_level=10, discount_threshold=0.2, order_quantity=15):
        self.avg_price = avg_price
        self.critical_stock_level = critical_stock_level
        self.discount_threshold = discount_threshold
        self.order_quantity = order_quantity

    def price_monitoring(self, current_price):
        """Check if the current price is below the discount threshold."""
        return current_price < (1 - self.discount_threshold) * self.avg_price

    def inventory_monitoring(self, current_stock):
        """Check if the stock is below the critical level."""
        return current_stock < self.critical_stock_level

    def ordering_decision(self, current_price, current_stock):
        """Decide how many units to order based on price and stock levels."""
        if self.inventory_monitoring(current_stock):
            # Stock is critically low
            return 10  # Minimum restock amount
        elif self.price_monitoring(current_price):
            # Price is significantly low, order more units
            return self.order_quantity
        else:
            # No need to order
            return 0


# Simulation Data
prices = [600, 580, 500, 450, 650, 700, 560, 490]  # Example price changes over time
stock_levels = [20, 18, 15, 5, 30, 12, 8, 25]       # Example stock levels over time

# Initialize the Trading Agent
agent = SmartphoneInventoryAgent(avg_price=600)

# Tracking variables for graph
order_quantities = []
timestamps = range(len(prices))

# Simulate the decision process over time
for i in range(len(prices)):
    current_price = prices[i]
    current_stock = stock_levels[i]
    tobuy = agent.ordering_decision(current_price, current_stock)
    order_quantities.append(tobuy)

    print(f"Time {i+1}: Price = {current_price} BDT, Stock = {current_stock} units, Order = {tobuy} units")

# Plotting the Results
plt.figure(figsize=(10, 6))
plt.plot(timestamps, prices, label='Smartphone Price (BDT)', marker='o')
plt.plot(timestamps, stock_levels, label='Stock Level (units)', marker='o')
plt.bar(timestamps, order_quantities, label='Units Ordered', alpha=0.5, color='orange')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Smartphone Inventory Management')
plt.legend()
plt.grid(True)
plt.show()
