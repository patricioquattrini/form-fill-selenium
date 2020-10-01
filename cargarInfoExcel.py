from openpyxl import load_workbook
from lote import Lote

def cargarExcel(file, hasta, lista_de_lotes):

    wb = load_workbook(file)
    worksheet = wb.active

    for i in range(2, hasta+1):
        lote = Lote()
        row = worksheet[i]
        lote.tit = str(row[0].value)
        lote.numL = str(row[1].value)
        lote.prec = str(row[2].value)
        lote.lkVimeo = str(row[3].value)
        lote.lkYou = str(row[4].value)
        lote.raza = str(row[5].value)
        lote.cate = str(row[6].value)
        lote.rp = str(row[7].value)
        lote.sba = str(row[8].value)
        lote.fech = str(row[9].value)
        lista_de_lotes.append(lote)

