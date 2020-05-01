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
# Need to search for balance sheets only..
ID = 4
SearchFile= 'XLSX_Files/' + str(ID) + '_Financial_Report.xlsx'
SearchString = 'total assets' # needs to be lower case
specific_sheet_name = 'consolidated balance sheets'

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
            print([ID, specific_sheet_name ,int(dd.columns[i][-4:]), dd[dd.columns[0]].values[0], dd[dd.columns[i]].values[0], 'thousands' if 'thousands' in dd.columns[0].lower() else 'millions' ])


for ii in range(1,8):
    SearchFile = 'XLSX_Files/' + str(ii) + '_Financial_Report.xlsx'
    SearchString = 'total assets'
    print(['ID','specific_sheet_name', 'Year', 'SearchString Value'])
    print([ii,ii,ii,ii,ii])
    print([SearchFile, SearchString, specific_sheet_name])
    try:
        get_info_from_xlsx(SearchFile,SearchString, ii)
    except:
        print("------------ get_info_from_xlsx failed")
        pass
