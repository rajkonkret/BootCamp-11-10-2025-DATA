import xlrd

with xlrd.open_workbook('xlwt.xls', on_demand=True) as book:
    sheet = book.sheet_by_index(0)

# on_demand=True - wczytuje tylko potrzebne arkusze

print(sheet)  # <xlrd.sheet.Sheet object at 0x107397620>
print(sheet.name)  # Arkusz1
print(sheet.nrows)  # 6
