import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [100, 150, 200, 170, 220]
}

df = pd.DataFrame(data)

# Plot
plt.plot(df["Day"], df["Sales"])
plt.title("Sales Data")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()
