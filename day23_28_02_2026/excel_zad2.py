# xlsxWriter - do tworzenia plików excel
# pip install xlsxwriter

import xlsxwriter
import datetime as dt

# tworzymy plik, w pamięci
book = xlsxwriter.Workbook('xlsxwriter.xlsx')
book = xlsxwriter.Workbook('xlsxwriter2.xlsx')
book = xlsxwriter.Workbook('xlsxwriter3.xlsx')
book = xlsxwriter.Workbook('xlsxwriter4.xlsx')
book = xlsxwriter.Workbook('xlsxwriter5.xlsx')

book.close()  # tworzy plik na dysku
