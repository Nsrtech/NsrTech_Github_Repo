import openpyxl

def Read_Excel_Data(file_path,sheet_name):
    #Code to load the data from excel file
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook[sheet_name]
    data_list = []

    for row in sheet.iter_rows(min_row=2,values_only=True):
        data_list.append(row)
    return data_list
