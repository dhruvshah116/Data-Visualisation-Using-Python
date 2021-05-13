import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15,5))

df=pd.read_json(r"./rain.json")

plt.plot(df["Month"],df["Temperature"],label="Temperature")
#plt.show()

plt.plot(df["Month"],df["Rainfall"],label="Rainfall")
plt.legend()
plt.show()


