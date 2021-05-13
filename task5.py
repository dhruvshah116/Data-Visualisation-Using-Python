import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'./tempYearly.csv')

sns.jointplot("Year","Rainfall",data=df,kind="reg")
plt.show()