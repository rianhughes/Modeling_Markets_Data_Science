import pandas as pd

# Returns the objects (rows?) which contain the STRING in the colomn
def get_cc_concept(df, STRING):
    qq=df.iloc[:,0].str.lower().iloc[:].str.contains(STRING)
    return df[qq.fillna(False)] # Returns objects which contains 'assets' in the key, case-controlled.

# Returns an array of all sheet names which contain STRING in the first Colomn 
def get_sheet_names(xlsx,STRING,array):
    for sheet in xlsx.sheet_names:
     found_ntn = get_cc_concept(xlsx.parse(sheet), STRING).empty
     array.append(sheet) if found_ntn==False else -1000
    return array

# Search SearchFile for ass instances where SearchString appears
SearchFile= 'XLSX_Files/4_Financial_Report.xlsx'
SearchString = 'total assets' # needs to be lower case
xlsx = pd.ExcelFile(SearchFile)
array=[]
get_sheet_names(xlsx,SearchString,array)

#Note array needs to be non-empty

# Return the data of SearchString in all sheets found (if found)
print(len(array))

for fd in range(0, len(array)):
    boolob = xlsx.parse(array[fd]).iloc[:,0].str.lower().str.contains(SearchString)
    print(xlsx.parse(array[fd])[boolob.fillna(False)])



