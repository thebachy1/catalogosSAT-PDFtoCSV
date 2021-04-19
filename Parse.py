import tabula
import csv, os, glob
import pandas as pd

tabula.convert_into("test.pdf", "catalogo-bancosPt1.csv", output_format="csv", stream=True, guess=False, pages='48', area=(293.99, 70.66, 686.5, 508.21))
f = open('catalogo-bancosPt1.csv', 'r')
csv_f = csv.reader(f)
rows = list(csv_f)
for i, row in enumerate(rows):
    if row[0] in (None, ""):
        previous_row = rows[i-1]
        previous_row[2] += ' ' + row[2]

        del rows[i]

with open('catalogo-bancosPt1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
        
tabula.convert_into("test.pdf", "catalogo-bancosPt2.csv", output_format="csv", pages='49-50', area=(83.55, 67.85, 714.73, 510.42))
f = open('catalogo-bancosPt2.csv', 'r')
csv_f = csv.reader(f)
rows = list(csv_f)
for i, row in enumerate(rows):
    if row[0] in (None, ""):
        previous_row = rows[i-1]
        previous_row[1] += ' ' + row[1]
        previous_row[2] += ' ' + row[2]

        del rows[i]

with open('catalogo-bancosPt2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

file = pd.read_csv('catalogo-bancosPt2.csv')

headerList = ['Clave', 'Nombre corto', 'Nombre o razón social']

file.to_csv("catalogo-bancosPt2.csv", header=headerList, index=False)


tabula.convert_into("test.pdf", "catalogo-bancosPt3.csv", output_format="csv", pages='51', area=(82.46, 68.02, 630.18, 509.04))
f = open('catalogo-bancosPt3.csv', 'r')
csv_f = csv.reader(f)
rows = list(csv_f)
for i, row in enumerate(rows):
    if not row[0] in (None, ""):
        del row[4], row[3]

    elif row[0] in (None, ""):
        del row[0], row[1]

with open('catalogo-bancosPt3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

file = pd.read_csv('catalogo-bancosPt3.csv')

headerList = ['Clave', 'Nombre corto', 'Nombre o razón social']

file.to_csv("catalogo-bancosPt3.csv", header=headerList, index=False)
    
os.chdir("/Users/thebachy1/Code/Parse-PDF")
all_filenames = ['catalogo-bancosPt1.csv', 'catalogo-bancosPt2.csv', 'catalogo-bancosPt3.csv']
combined_csv = pd.concat([pd.read_csv(f, header = 0) for f in all_filenames ])
combined_csv.to_csv("catalogo-bancos.csv", encoding='utf-8')

tabula.convert_into("test.pdf", "codigo-agrupador-cuentas.csv", output_format="csv", pages='2-37')