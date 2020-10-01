from cargadorLote import cargadorLote
from cargarInfoExcel import cargarExcel
from cargarImgSolo import cargadorDeImagenes
from editarLoteEnGral import editarLote
lista_de_lotes = list()

#########################--ESTOS PROGRMAS TIENEN QUE FUNCIONAR UNO A LA VEZ--#########################
######################### PREPARACION #########################
##### Acomodar el Excel con estos titulos, seguir el de prueba, ojo los formatos
##### Titulo    Num_Lote	Precio	link_Vimeo	link_Yaoutube	Raza	Categoria	RP	HBA/SBA	Fecha

######################### CARGADOR DE EXCEL  #########################
file = ".\Remate200720.xlsx" ##### Poner el nombre del EXCEL
#Mirar cuantas filas tiene el Excel del remate y agregarlo en HASTA
hasta = 97
#cargarExcel(file, hasta, lista_de_lotes)
######################### CARGADOR DE EXCEL  #########################

######################### CARGADOR DE LOTES  #########################
id_Remate = "87" ##### Poner el ID del REMATE
#cargadorLote(id_Remate, lista_de_lotes)
#print(str(len(lista_de_lotes))+" Lotes")
######################### CARGADOR DE LOTES NUEVO #########################

######################### EDITOR DE LOTES ##########################
##### Esto sirve para agregar informacion a lotes ya cargados
#cantidad_lotes = 4
#id_primer_lote = 1774
#cargarExcel(file, hasta, lista_de_lotes)
#editarLote(id_primer_lote, cantidad_lotes ,lista_de_lotes)
######################### EDITOR DE LOTES ##########################

######################### CARGADOR DE IMAGENES #########################
######################### ESTO SOLO SE PUEDE USAR SI ESTAN CARGADOS LOS LOTES Y TIENEN QUE SER CONSECUTIVOS #########################
nombreImg = "\logo.PNG"
cantLotes = 95
id_primer_lote = 2496
cargadorDeImagenes(id_primer_lote, cantLotes, nombreImg)
######################### CARGADOR DE IMAGENES #########################
