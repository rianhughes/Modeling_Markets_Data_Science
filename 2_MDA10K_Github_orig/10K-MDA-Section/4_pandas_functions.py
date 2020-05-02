import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load File
df = pd.read_csv('0_3__FUSE_MDA_XLSX_DATA.csv')

print(df.keys())

# Create New DataFrame
data = [ df['TONE'], df['Year'] ]
keys = ["TONE","Year"]
df2 = pd.concat(data, axis=1, keys=keys)

# Plot some stuff
sns.pairplot(df2)
plt.show()


