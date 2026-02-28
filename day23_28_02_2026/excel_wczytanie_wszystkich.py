import glob
from pprint import pprint

from openpyxl import load_workbook

file_list = glob.glob("*.xlsx") # pokazuje liste plikow o rozszerzeniu .xlsx
print(file_list)
pprint(file_list)
# ['wyniki.xlsx',
#  'xlsxwriter_optimized.xlsx',
#  'edited.xlsx',
#  'dane_zaktualziowane.xlsx',
#  'openpyxl_optimized.xlsx',
#  'tabela_przestawna.xlsx',
#  'tabela_przestawna2.xlsx',
#  'vgsales_formated.xlsx',
#  'xlsxwriter.xlsx',
#  'xlsxwriter5.xlsx']

