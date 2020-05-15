import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load File
df = pd.read_csv('0_3__FUSE_MDA_XLSX_DATA.csv')

print(df)
print(df.keys())

# Create New DataFrame
data = [ df['TONE'], df['quantity-value'], df['ACQ'],  df['NEG'], df['POS']]
keys = ["TONE","Value", "ACQ", "NEG", "POS"]
df2 = pd.concat(data, axis=1, keys=keys)
df2 = df2[df2['Value']<1000000]

#Plot some stuff
# hue..
sns.pairplot(df2, kind='reg')
plt.show()


