import xlrd
import csv
from xlsxwriter.utility import xl_rowcol_to_cell
import pandas as pd
import matplotlib.pyplot as plt

# As a test, look for Total Asset
# Note that some are n Thousands, and others Millions


# ----- Use Pandas
SearchFile= 'XLSX_Files/4_Financial_Report.xlsx'
SearchString = 'Pensions'

dff = pd.read_excel(SearchFile ,sheet_name=1, index_col=0)
dff.loc[SearchString]

dff.describe()
[dff.mean(), dff.std()]

dff.iloc[:,0] # Gets the first colomn, which are the concepts (?)
dff.iloc[:,0].str.contains('Assets') # Returns bool of which item has 

def get_cc_concept(df, STRING):
    qq=df.iloc[:,0].str.lower().iloc[:].str.contains(STRING) 
    return df[qq.fillna(False)] # Returns objects which contains 'assets' in the key, case-controlled.



# Create a single df object with all sheets
SearchFile= 'XLSX_Files/4_Financial_Report.xlsx'
xlsx = pd.ExcelFile(SearchFile)

array=[]
def get_sheet_names(xlsx,STRING,array):
    for sheet in xlsx.sheet_names:
     found_ntn = get_cc_concept(xlsx.parse(sheet), STRING).empty
     array.append(sheet) if found_ntn==False else -1000
    return array
    
# EXAMPLE
import pandas as pd
SearchFile= 'XLSX_Files/4_Financial_Report.xlsx'
SearchString = 'pensions' # needs to be lower case
xlsx = pd.ExcelFile(SearchFile)
array=[]
get_sheet_names(xlsx,SearchString,array)

#Note array needs to be non-empty
boolob = xlsx.parse(array[0]).iloc[:,0].str.lower().str.contains(SearchString)
xlsx.parse(array[0])[boolob.fillna(False)]

# --------------


def findCell(sh, searchedValue):
    for row in range(sh.nrows):
        for col in range(sh.ncols):
            myCell = sh.cell(row, col)
            if myCell.value == searchedValue:
                return row
                #return xl_rowcol_to_cell(row, col)
    return -1


#myPath = 'XLSX_Files/4_Financial_Report.xlsx'

#searchedValue = 'Entity Common Stock, Shares Outstanding'
#for sh in xlrd.open_workbook(myPath).sheets():
#    print(sh.row(findCell(sh, searchedValue))) if findCell(sh, searchedValue) != -1 else 1

#input('Press ENTER to exit')



#----------------------------

def csv_from_excel():
    wb = xlrd.open_workbook('XLSX_FILES/20761_Financial_Report.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('your_csv_file.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
#csv_from_excel()
