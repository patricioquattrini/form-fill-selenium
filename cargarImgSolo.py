from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


def cargadorDeImagenes(idPrimerLote, cantLotes, rutaImg):

    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Administrador\Desktop\Proyectos\autocompletadorConSelenium\chromedriver.exe")
    driver.get("https://www.elrural.com/remates-ofertas/login")
    usuario = driver.find_element_by_id("email")
    usuario.send_keys("xxxxxx")

    passw = driver.find_element_by_id("password")
    passw.send_keys("xxxx")
    passw.send_keys(Keys.ENTER)

    for i in range(cantLotes):
        time.sleep(23)
        driver.get("https://www.elrural.com/remates-ofertas/admin/images/addto/"+str(idPrimerLote+i))
        driver.find_element_by_name("image[]").send_keys(os.getcwd() + rutaImg)
        subir_img = driver.find_elements_by_tag_name("button")
        subir_img[1].send_keys(Keys.ENTER)
