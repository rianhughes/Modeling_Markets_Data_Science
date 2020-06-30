import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt
import numpy

#File='A_Tweet_Data/A_GetOldTweet_bitcoin-2017-6-1.csv'

#Load File
#df=pd.read_csv(File)
#df_tb = pd.DataFrame({'Tweets' : df['text']})

# Making sure those pesky 'Nans' don't show up.. They aren't strings!
#a=[isinstance(i, str) for i in df_tb['Tweets']]
#df_tb=df_tb[a]

# Create a function to clean the tweets
def cleanTxt(text):
 if type(text)!=str:
    print(type(text))
 text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
 text = re.sub('#', '', text) # Removing '#' hash tag
 text = re.sub('RT[\s]+', '', text) # Removing RT
 text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
 text = re.sub('Bitcoin', '', text) # Removing hyperlink
 text = re.sub('bitcoin', '', text) # Removing hyperlink
 text = re.sub('BTC', '', text) # Removing hyperlink
 text = re.sub('blockchain', '', text) # Removing hyperlink
 return text
# Clean the tweets
#df_tb['Tweets']=df_tb['Tweets'].apply(cleanTxt)

# Create a function to get the subjectivity (fact=0, opinion=1)
def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity (neg = -1, pos = +1)
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity

# Create two new columns 'Subjectivity' & 'Polarity'
#df_tb['Subjectivity'] = df_tb['Tweets'].apply(getSubjectivity)
#df_tb['Polarity'] = df_tb['Tweets'].apply(getPolarity)

# Create a function to compute negative (-1), neutral (0) and positive (+1) analysis
def getAnalysis(score):
    if score < 0:
      return 'Negative'
    elif score == 0:
      return 'Neutral'
    else:
      return 'Positive'
# Add 'Analysis' to the df
#df_tb['Analysis'] = df_tb['Polarity'].apply(getAnalysis)# Show the dataframe


def senti_count(dff):
    neu=0
    pos=0
    neg=0
    #print(dff)
    for i in range(0,dff.shape[0]):
        #print({i,type(i)})
        #print(dff)
        if dff['Analysis'].iloc[i] == 'Neutral':
            neu+=1
        if dff['Analysis'].iloc[i] == 'Positive':
            pos+=1
        if dff['Analysis'].iloc[i] == 'Negative':
            neg+=1
    return [pos,neg,neu, pos+neg+neu]

#senti_count(df_tb)

def GetSenti_Data(FileName):
    #File='A_Tweet_Data/A_GetOldTweet_bitcoin-2017-6-1.csv'

    #Load File
    df=pd.read_csv(FileName)
    df_tb = pd.DataFrame({'Tweets' : df['text']})

    # Making sure those pesky 'Nans' don't show up.. They aren't strings!
    a=[isinstance(i, str) for i in df_tb['Tweets']]
    df_tb=df_tb[a]

    # Clean the tweets
    df_tb['Tweets']=df_tb['Tweets'].apply(cleanTxt)

    # Create two new columns 'Subjectivity' & 'Polarity'
    df_tb['Subjectivity'] = df_tb['Tweets'].apply(getSubjectivity)
    df_tb['Polarity'] = df_tb['Tweets'].apply(getPolarity)

    # Add 'Analysis' to the df
    df_tb['Analysis'] = df_tb['Polarity'].apply(getAnalysis)# Show the dataframe

    # Get Sentiment Data.
    return senti_count(df_tb)


