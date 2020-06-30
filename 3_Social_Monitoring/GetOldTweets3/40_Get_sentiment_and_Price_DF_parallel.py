import csv
import os
import subprocess
import pandas as pd
import FunctionsSentiment as SF
import FunctionsPrice as PF
import sys

# Year and Month as inputs (to allow for hardcode parallizing)
year_arg = sys.argv[1]
month_arg = sys.argv[2]

filename_save="D_Processed_Price_and_Sentiment/D_Senitment_Price_"+year_arg+"_"+month_arg+".csv"
query_string="bitcoin"

#Write the datato a csv file
with open(filename_save, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Pos", "Neg", "Neu", "Total", "Price","Year","Month","Day"])
    for year in [year_arg]:
        for month in [month_arg]:
            for day in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17 ,18 ,19, 20, 21, 22, 23, 24, 25, 26, 27, 28]: #, 29, 30, 31]:
                df_row=[] 
                #try:
                    # Get Sentiment Data
                #    FileName_Tweet="A_Tweet_Data/A_GetOldTweet_" + query_string + "-" + str(year) + "-" + str(month) + "-" + str(day) + ".csv"
                #    pos,neg,neu,tot = SF.GetSenti_Data(FileName_Tweet)
                #except:
                    # Data point doesn't exist / some error
                #    pos,neg,neu,tot = 0,0,0,0
                
                #try:
                    #Get Price Data
                print([year, month, day])
                FileName_Price="C_Price_Data/Bitfinex_BTCUSD_d.csv" # "A_Tweet_Data/A_GetOldTweet_" + query_string + "-" + str(year) + "-" + str(month) + "-" + str(day) + ".csv"
                price= PF.GetPrice_on_Date(FileName_Price, year, month, day)
                #print([year, month, day])
                #except:
                    # Error when getting price data
                    
                    #price=-1;
                #writer.writerow([pos,neg,neu,tot,price,year,month,day])
    

