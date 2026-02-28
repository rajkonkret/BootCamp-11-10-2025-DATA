import xlsxwriter

book = xlsxwriter.Workbook("xlsxwriter_optimized.xlsx",
                           options={"constant_memory": True})
#  options={"constant_memory": True} - stały bufor w pamięci
# zapis częściami

sheet = book.add_worksheet()
for row in range(1000):
    sheet.write_row(row, 0, list(range(2000)))

book.close()
