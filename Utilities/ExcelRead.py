import openpyxl
class ExcelReadClass:
    def read_excel_cell(self, row_no, col_no):
        book = openpyxl.load_workbook('//Users//vipinvijayan//Desktop//Testing Data.xlsx')
        sheet = book["Sheet1"]
        return sheet.cell(row=row_no, column=col_no).value




