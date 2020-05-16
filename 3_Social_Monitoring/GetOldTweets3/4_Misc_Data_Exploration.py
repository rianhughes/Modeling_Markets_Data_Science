import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

filename_t = 'A_Tweet_Data/A_GetOldTweet_bitcoin-2017-6-1.csv'  

df=pd.read_csv(filename_t)

# Histogram of favorites
hist_data1 = df[(df['favorites']<100) & (df['favorites']>0)]['favorites']
plt.hist( hist_data1, bins=1000, label='Favs')
#plt.xlabel('Favorites'); plt.ylabel('Count');plt.show()

# Histogram of retweets
hist_data2 = df[(df['retweets']<100) & (df['retweets']>0)]['retweets']
plt.hist( hist_data2, bins=1000, label='Retweets')
plt.xlabel('Retweets'); plt.ylabel('Count');plt.legend();plt.show()


