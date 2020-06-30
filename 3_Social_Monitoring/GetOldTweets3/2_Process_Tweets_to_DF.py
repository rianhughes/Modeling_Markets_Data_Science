import csv
import os
import subprocess
import pandas as pd

query_string="bitcoin"
filename_save="B_Tweet_Data_Processed/B_GetOldTweet_" + query_string + "_GetNum_.csv"


with open(filename_save, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Month", "Day" ,"num_lines", "num_retweets"])
    for year in [2017]:
        for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            for day in [1, 5, 6 ,7, 8, 9, 15, 20]:
                filename = "A_Tweet_Data/A_GetOldTweet_" + query_string + "-" + str(year) + "-" + str(month) + "-" + str(day) + ".csv"
                num_lines = sum(1 for line in open(filename))
                df=pd.read_csv(filename)
                num_retweets = sum(df[df['retweets']>0]['retweets'])
                writer.writerow([year, month, day, num_lines, num_retweets])
    
    for year in [2018]:
        for month in [1, 6, 11, 20]:
            for day in [1]:
                num_lines = sum(1 for line in open("A_Tweet_Data/A_GetOldTweet_" + query_string + "-" + str(year) + "-" + str(month) + "-" + str(day) + ".csv"))
                writer.writerow([year, month, day, num_lines])


