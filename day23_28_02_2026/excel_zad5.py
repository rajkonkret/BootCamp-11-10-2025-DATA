import xlwt
from xlwt.Utils import cell_to_rowcol2
import datetime as dt

book = xlwt.Workbook()

sheet = book.add_sheet("Arkusz1")

sheet.write(*cell_to_rowcol2("A1"), "Radek")
sheet.write(r=1, c=0, label="Kowalski")

formatting = xlwt.easyxf(
    "font: bold on, color red;"
    "align: horiz center;"
    "borders: top_color red, bottom_color red,"
    "right_color red, left_color red,"
    "left thin, right thin,"
    "top thin, bottom thin;"
    "pattern: pattern solid, fore_color yellow;"
)
book.save("dane.xls")
