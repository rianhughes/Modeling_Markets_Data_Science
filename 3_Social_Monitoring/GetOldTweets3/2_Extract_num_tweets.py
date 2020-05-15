import csv
import os
import subprocess

query_string="bitcoin"
filename_save="B_Tweet_Data_Processed/B_GetOldTweet_" + query_string + "_GetNum_.csv"


with open(filename_save, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Month", "Day" ,"num_lines"])
    for year in [2020]:
        for month in [1]:
            for day in [1,5,10]:
                num_lines = sum(1 for line in open("A_Tweet_Data/A_GetOldTweet_" + query_string + "-" + str(year) + "-" + str(month) + "-" + str(day) + ".csv"))
                writer.writerow([year, month, day, num_lines])
    


