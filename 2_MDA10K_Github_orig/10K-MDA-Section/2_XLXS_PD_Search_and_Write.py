"""
This file searches through a selection of xslx files (SearchFile), pulls the data you want (SearchString from specific_sheet_name), and saves it into a csv file (csv_filename)
Inputs: 
    SearchFile
    SearchString
    specific_sheet_name
    csv_filename
Outputs:
    CSV file 'csv_filename'
"""
import pandas as pd

# Returns the objects (rows?) which contain the STRING in the colomn
def get_cc_concept(df, STRING):
    qq=df.iloc[:,0].str.lower().iloc[:].str.contains(STRING)
    return df[qq.fillna(False)] # Returns objects which contains 'assets' in the key, case-controlled.

# Returns an array of all sheet names which contain STRING in the first Colomn 
def get_sheet_names(xlsx,STRING,array, specific_sheet_name):
    for sheet in xlsx.sheet_names:
        if specific_sheet_name == sheet.lower():
            found_ntn = get_cc_concept(xlsx.parse(sheet), STRING).empty
            array.append(sheet) if found_ntn==False else -1000
    return array

# Search SearchFile for ass instances where SearchString appears
def get_info_from_xlsx(SearchFile, SearchString, ID):
    xlsx = pd.ExcelFile(SearchFile)
    array=[]
    get_sheet_names(xlsx,SearchString,array, specific_sheet_name)

    # Return the data of SearchString in all sheets found (if found)
    for fd in range(0, len(array)):
        boolob = xlsx.parse(array[fd]).iloc[:,0].str.lower().str.contains(SearchString)
        dd=xlsx.parse(array[fd])[boolob.fillna(False)]
        # Get the values from the cleaned data
        for i in range(1, len(dd.columns)):
            newv = int( str(dd[dd.columns[i]].values[0]) + '000') if 'thousands' in dd.columns[0].lower() else int(dd[dd.columns[i]].values[0])
            return [ID, specific_sheet_name ,int(dd.columns[i][-4:]), dd[dd.columns[0]].values[0], newv, 'thousands' ]
            #return [ID, specific_sheet_name ,int(dd.columns[i][-4:]), dd[dd.columns[0]].values[0], dd[dd.columns[i]].values[0], 'thousands' if 'thousands' in dd.columns[0].lower() else 'millions' ]


# Print some data to terminal for testing
if 0:
    for ii in range(1,8):
        ID = ii
        SearchFile = 'XLSX_Files/' + str(ii) + '_Financial_Report.xlsx'
        SearchString = 'total assets'
        specific_sheet_name = 'consolidated balance sheets'
        print(['ID','specific_sheet_name', 'Year', 'SearchString Value']) 
        print([SearchFile, SearchString, specific_sheet_name])
        try:
            get_info_from_xlsx(SearchFile,SearchString, ii)
        except:
            print("------------ get_info_from_xlsx failed")
            pass


# Main Algorithm
# Write Data to a csv file
import csv
import os

csv_filename="0_2__XLXS_PD_Search_and_Write_DATA.csv"
ID_start=1
ID_end=90000

with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(['ID','specific_sheet_name', 'Year', 'quantity-type', 'quantity-value', 'quantity-units'])
    for ii in range(ID_start, ID_end):
        ID = ii
        SearchFile = 'XLSX_Files_MDATone/' + str(ii) + '_Financial_Report.xlsx'
        SearchString = 'total assets'
        specific_sheet_name = 'consolidated balance sheets'   
        try:
            #print(get_info_from_xlsx(SearchFile,SearchString, ii))
            writer.writerow(get_info_from_xlsx(SearchFile,SearchString, ii))
        except:
            try:
                SearchFile = 'XLSX_Files_MDATone/' + str(ii) + '_Financial_Report.xls'
                writer.writerow(get_info_from_xlsx(SearchFile,SearchString, ii))
                print("------------ get_info_from_xlsx failed ----- failed to write to csv file")
            except:
                pass



