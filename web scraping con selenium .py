# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:46:59 2020

@author: 20rd1
"""

# Se importan las librerias 
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd 

# Ruta para indicar la ubicación del driver necesario para la biblioteca webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Le decimos al driver de chrome de que url sacar la información
driver.get('https://www.olx.com.ec/autos_c378')



# Buscamos el boton de cargar más 
# Vamos a darle al boton 3 veces

boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        boton.click()
        time.sleep(random.uniform(15.0, 20.0))
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

# Marcamos donde estan todos los anuncios de una lista
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

precio = list()
descripcion = list ()               #creamos las listas para almacenar los datos

for auto in autos:                  #creamos un for para meter cada dato en su lista
    precio.append(auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text)
   
    
    descripcion.append(auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text)
    
    
#con la libreria pandas creamos la tabla. 
    
dict = {'Coches': descripcion,'Precio':precio}

df = pd.DataFrame(dict)

print(df)













