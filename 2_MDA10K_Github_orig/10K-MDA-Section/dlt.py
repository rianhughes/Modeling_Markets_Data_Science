import os
import re
import csv
import requests 
import urllib

# edgar/data/98246/0000098246-20-000058
# Want the Financial_Report.xlsx

filepath = "/home/rian/Desktop/1_Work/6_Jobs__Quant_RiskManagmemnt_DS/Modeling_Markets/2_MDA10K_Github_orig/10K-MDA-Section/"

download_xlsx = os.path.join(filepath, "downloadlist_xlsx_MDATone.csv")
download = os.path.join(filepath, "MDA_Tone.csv")
savepath = filepath + "XLSX_Files_MDATone/"
#download = os.path.join(filepath, "downloadlist.txt")

# remove new downloadlist_xlsx.txt file if it exists. Keep it fresh.
if os.path.exists(download_xlsx):
    os.remove(download_xlsx)

# First step : Create file with links
# Create a bunch of links to potential Fiinancial_Report.xlsx files and save in download_xlsx
with open(download_xlsx,"a+") as newfile:
    g = open(download, "r")
    newfile.write("ID,URL\n")
    next(csv.reader(g))
    for line in g:
     substring = re.search("edgar/data/(.*?).txt", line).group(1)
     substring = substring.replace('-','')
     str2 = re.search("(.*?),", line).group(1)
     #print([ str2 ,"edgar/data/" + substring])
     newfile.write(str2 + "," +"edgar/data/" + substring + "/Financial_Report.xlsx" +"\n")
    g.close()


