#import openpyxl

class HomePageData:

    test_HomePage_data = [{"firstname":"Rahul", "lastname":"shetty", "gender":"Male"}, {"firstname":"Siri", "lastname":"Mali", "gender":"Female"}]

'''
    @staticmethod
    def getTestData(test_case_name):
        Dict = {}
        book = openpyxl.load_workbook("C:\\Users\\syala\\OneDrive\\Documents\\PythonDemo.xlsx")
        sheet = book.active
        for i in range(1, sheet.max_row + 1):
            if sheet.cell(row=i, column=1).value == test_case_name:
                for j in range(2, sheet.max_column + 1):
                    # Dict["lastname"] = 'yalagonda'
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

        return[Dict]
    '''