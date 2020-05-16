import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

filename_k = 'Price_Data/Kraken_BTCUSD_d.csv'  
filename_b = 'Price_Data/Bitfinex_BTCUSD_d.csv'
filename_t = 'B_Tweet_Data_Processed/B_GetOldTweet_bitcoin_GetNum_.csv'

def plot_price(filename_, ID):
    df=pd.read_csv(filename_)
    x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in df['Date']]
    y = df['Open']
    plt.plot(x,y, label=ID)
    plt.gcf().autofmt_xdate()

def plot_tweet_count(filename_, ID, Nrmlse):
    df=pd.read_csv(filename_)
    dates = [ str(df['Year'][i])+'-'+str(df['Month'][i])+'-'+str(df['Day'][i]) for i in range(len(df['Day']))]
    x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
    y = df['num_lines']*Nrmlse
    plt.plot(x,y, label=ID)
    plt.gcf().autofmt_xdate()

def get_nrmlse(filename_price, filename_tweet):
    """
    Normalise the tweet count to the price
    """
    df1=pd.read_csv(filename_price)
    df2=pd.read_csv(filename_tweet)
    ref_date1 = '2017-06-01' 
    ref_price = float(df1[df1['Date']==ref_date1]['Open'])
    ref_tcnt  = float(df2[(df2['Year']==2017)][(df2['Month']==6)][df2['Day']==1]['num_lines'])
    return ref_price/ref_tcnt

Nrmlse=get_nrmlse(filename_k, filename_t)
print(Nrmlse)

plot_price(filename_k, 'BTCUSD-Kraken')
plot_price(filename_b, 'BTCUSD-Bitfinex')
plot_tweet_count(filename_t, 'Tweet Count (Norm)', Nrmlse )

plt.legend()
plt.show()


