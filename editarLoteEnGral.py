from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

def editarLote(id_primer_lote, cantidad_lotes ,lista_de_lotes):

    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Administrador\Desktop\Proyectos\autocompletadorConSelenium\chromedriver.exe")
    driver.get("https://www.elrural.com/remates-ofertas/login")
    usuario = driver.find_element_by_id("email")
    usuario.send_keys("xxxxxxxxxxx")#Usuario

    passw = driver.find_element_by_id("password")
    passw.send_keys("xxxx")#Pass
    passw.send_keys(Keys.ENTER)
    i = 0
    for lot in lista_de_lotes:
        print(i)
        time.sleep(2)
        driver.get("https://www.elrural.com/remates-ofertas/admin/lotes/edit/"+str(id_primer_lote+i))

        titulo = driver.find_element_by_id("titulo")
        titulo.send_keys(Keys.LEFT_CONTROL, "a")
        titulo.send_keys(Keys.DELETE)
        titulo.send_keys(lot.tit)

        numeroLote = driver.find_element_by_id("numero")
        numeroLote.send_keys(Keys.LEFT_CONTROL, "a")
        numeroLote.send_keys(Keys.DELETE)
        numeroLote.send_keys(lot.numL)

        precio = driver.find_element_by_id("precio")
        precio.send_keys(Keys.LEFT_CONTROL, "a")
        precio.send_keys(Keys.DELETE)
        precio.send_keys(lot.prec)

        if not (lot.lkVimeo == "None"):
            linkVimeo = driver.find_element_by_id("link_vimeo")
            linkVimeo.send_keys(Keys.LEFT_CONTROL, "a")
            linkVimeo.send_keys(Keys.DELETE)
            linkVimeo.send_keys(lot.lkVimeo)

        if not (lot.lkYou == "None"):
            linkYoutube = driver.find_element_by_id("link_youtube")
            linkYoutube.send_keys(Keys.LEFT_CONTROL, "a")
            linkYoutube.send_keys(Keys.DELETE)
            linkYoutube.send_keys(lot.lkYou)

        razaCate = driver.find_elements_by_id("dodo")
        razaCate[0].send_keys(" ")
        time.sleep(1)
        razaCate[0].send_keys(lot.raza)
        time.sleep(1)
        razaCate[0].send_keys(Keys.ARROW_DOWN)
        razaCate[0].send_keys(Keys.ARROW_DOWN)
        razaCate[0].send_keys(Keys.ARROW_DOWN)
        razaCate[0].send_keys(Keys.ARROW_DOWN)
        razaCate[0].send_keys(Keys.ENTER)

        razaCate[1].send_keys(" ")
        time.sleep(1)
        razaCate[1].send_keys(lot.cate)
        # time.sleep(1)
        # razaCate[1].send_keys(Keys.ARROW_DOWN)
        razaCate[1].send_keys(Keys.ENTER)

        rp = driver.find_element_by_id("rp")
        rp.send_keys(Keys.LEFT_CONTROL, "a")
        rp.send_keys(Keys.DELETE)
        rp.send_keys(lot.rp)

        sba = driver.find_element_by_id("sba")
        sba.send_keys(Keys.LEFT_CONTROL, "a")
        sba.send_keys(Keys.DELETE)
        sba.send_keys(lot.sba)

        fecha = driver.find_element_by_id("fecha_nacimiento")
        fecha.send_keys(Keys.LEFT_CONTROL, "a")
        fecha.send_keys(Keys.DELETE)
        fecha.send_keys(lot.fech)
        fecha.send_keys(Keys.ENTER)
        fecha.send_keys(Keys.ENTER)
        fecha.send_keys(Keys.ENTER)
        fecha.send_keys(Keys.ENTER)

        i+= 1