import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(r"./birthYear.csv")
print(data)

''' 
sns.heatmap(data,annot=True,fmt="d")
-> annot=True : means we want  umbers inside our heatmap
-> fmt="d"  :  format set to decimal ,integer

->the above line of code is going to blow up as it is not in the right format for a heatmap , we need 
to convert it into a matrix first(using pivot) 
'''
for i in range(20):
    print("-",end="")
print()
dataP=data.pivot("month","year","births")   #conversion to matrix
print(dataP)
sns.heatmap(dataP,annot=True,fmt="d")
plt.show()