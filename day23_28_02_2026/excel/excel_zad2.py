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

# tworzy arkusz
sheet = book.add_worksheet("Arkusz1")

sheet.write("A1", "Witaj1")
sheet.write("A2", "Witaj  2")

# formatowanie / kolory
formatting = book.add_format(
    {"font_color": "#FF0000",
     "bg_color": "#FFFF00",
     "bold": True,
     "align": "center",
     "border": 1,
     "border_color": "#FF0000"}
)

sheet.write("A3", "Witaj 3", formatting)

# formatowanie daty
date_format = book.add_format({"num_format": "yyyy/mm/dd"})
sheet.write("A4", dt.date(2016, 10, 13), date_format)

# formatowanie wartości numerycznych
# number_format = book.add_format({"num_format": "0.00"})
number_format = book.add_format({"num_format": "[$-409]0.00"})  # 409 - lokalizacja USA

sheet.write("A5", 3.333333, number_format)

# formuły
sheet.write("A6", "=SUM(A4, 2)")

# dodanie obrazka
sheet.insert_image(0, 5, 'django_komendy.png', {"x_scale": 0.5, "y_scale": 0.5})

# wykresy
categories = ['Styczeń', "Luty"]
values = [100, 150]
sheet.write_row("B20", categories)
sheet.write_row("B21", values)

chart = book.add_chart({"type": "column"})
chart.set_title({"name": "Sprzedaż"})
chart.add_series(
    {
        "name": "=Arkusz1!A30",
        "categories": "=Arkusz1!B20:C20",
        "values": "=Arkusz1!B21:C21"
    }
)

chart.set_x_axis({"name": "OS X"})
chart.set_y_axis({"name": "OS Y"})

sheet.insert_chart("A15", chart)

book.close()  # tworzy plik na dysku
