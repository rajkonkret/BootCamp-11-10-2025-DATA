from openpyxl import Workbook
import openpyxl

wb = Workbook()
ws = wb.active
ws.title = "Dane"

data = [
    ["Data", "Kategoria", "Produkt", "Sprzedaj"],
    ["2024-01-01", "Elektronika", "Telefon", 1500],
    ["2024-01-02", "Elektronika", "Telefon", 1500],
    ["2024-01-02", "Odzież", "Koszula", 1500],
    ["2024-01-03", "Odzież", "Kurtka", 1500],
    ["2024-01-04", "Elektronika", "Laptop", 1500],
]
