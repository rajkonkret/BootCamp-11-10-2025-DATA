# praca z plikami xls
# xlrd, xlwt
import sys

print(sys.version)  # 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)]
print(sys.version_info)
# sys.version_info(major=3, minor=13, micro=7, releaselevel='final', serial=0)

print(sys.executable)  # srodowisko pythona
# /Users/radoslawjaniak/BootCamp-11-10-2025-DATA/.venv/bin/python

# pip install "xlrd==1.2.0" "xlwt==1.3.0" "xlutils==2.0.0"
import xlrd

person = xlrd.open_workbook('dane_person.xls')
print(person)  # <xlrd.book.Book object at 0x108024830>
print(person.sheet_names())  # ['Arkusz1']

sheet = person.sheet_by_index(0)
print(sheet.name)  # Arkusz1

sheet = person.sheet_by_name("Arkusz1")
print(sheet.name)  # Arkusz1
