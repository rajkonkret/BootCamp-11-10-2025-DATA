import openpyxl

import lxml  # przyspieszenie procesu zapisu

book = openpyxl.Workbook(write_only=True)
# write_only=True - optymalizacja zużycia pamięci
# przy tej fladze nie działą book.active

sheet = book.create_sheet()

# 1000 x 2000
for row in range(1000):
    sheet.append(list(range(2000)))

book.save("openpyxl_optimized.xlsx")
