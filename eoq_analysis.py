import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Monthly demand data
demand = [120, 150, 130, 170, 160, 180, 200, 210, 190, 175, 165, 155]

months = list(range(1, 13))

df = pd.DataFrame({
    "Month": months,
    "Demand": demand
})

# Parameters
ordering_cost = 500
holding_cost = 2
annual_demand = sum(demand)

# EOQ calculation
EOQ = np.sqrt((2 * annual_demand * ordering_cost) / holding_cost)

# Reorder Point
lead_time = 1
avg_demand = np.mean(demand)
ROP = avg_demand * lead_time

print(f"EOQ: {EOQ:.2f}")
print(f"ROP: {ROP:.2f}")

# Plot
plt.plot(df["Month"], df["Demand"], marker='o')
plt.title("Monthly Demand Analysis")
plt.xlabel("Month")
plt.ylabel("Demand")
plt.grid()
plt.show()