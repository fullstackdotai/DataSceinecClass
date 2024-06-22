import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("starting to import file")
data = pd.read_csv("laptop.csv")
print("Finished import file")
print(data.shape)
print(data.isnull().sum())
print(data.head(10))


#data.drop(columns=['Unnamed:0'],inplace=True)
## remove gb and kg from Ram and weight and convert the cols to numeric
data['Ram'] = data['Ram'].str.replace("GB", "")
data['Weight'] = data['Weight'].str.replace("kg", "")
data['Ram'] = data['Ram'].astype('int32')
data['Weight'] = data['Weight'].astype('float32')

sns.distplot(data['Price'])
plt.show()


#what is avg price of each brand?

sns.barplot(x=data['Company'], y=data['Price'])

plt.xticks(rotation="vertical")

plt.show()