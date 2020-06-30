import csv
import os
import subprocess
import pandas as pd
import FunctionsSentiment as SF
import FunctionsPrice as PF

filename_save="D_Processed_Price_and_Sentiment/D_Senitment_Price.csv"
query_string="bitcoin"

#Write the data to a csv file
with open(filename_save, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Pos", "Neg", "Neu", "Total", "Price","Year","Month","Day"])
    for year in [2017]:
        for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            for day in [1]: #, 5, 6 ,7, 8, 9, 15, 20]:
                df_row=[] 
                try:
                    # Get Sentiment Data
                    FileName_Tweet="A_Tweet_Data/A_GetOldTweet_" + query_string + "-" + str(year) + "-" + str(month) + "-" + str(day) + ".csv"
                    pos,neg,neu,tot = SF.GetSenti_Data(FileName_Tweet)
                except:
                    # Data point doesn't exist / some error
                    pos,neg,neu,tot = 0,0,0,0
                
                try:
                    #Get Price Data
                    FileName_Price="C_Price_Data/Bitfinex_BTCUSD_d.csv" # "A_Tweet_Data/A_GetOldTweet_" + query_string + "-" + str(year) + "-" + str(month) + "-" + str(day) + ".csv"
                    price= PF.GetPrice_on_Date(FileName_Price, year, month, day)
                except:
                    # Error when getting price data
                    price=-1;
                writer.writerow([pos,neg,neu,tot,price,year,month,day])
    

