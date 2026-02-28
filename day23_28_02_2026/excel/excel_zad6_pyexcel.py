import pyexcel

# pip install pyexcel pyexcel-xlsx

data = [
    ["Imie", "Wiek"],
    ["Tomek", 45],
    ["Kasia", 34],
]

sheet = pyexcel.Sheet(data)
sheet.save_as('wyniki.xlsx')

sheet = pyexcel.get_sheet(file_name='wyniki.xlsx')
print(sheet)
# pyexcel sheet:
# +-------+------+
# | Imie  | Wiek |
# +-------+------+
# | Tomek | 45   |
# +-------+------+
# | Kasia | 34   |
# +-------+------+
