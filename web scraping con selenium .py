# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:46:59 2020

@author: 20rd1
"""
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd 

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.olx.com.ec/autos_c378')



#Vamos a darle al boton 3 veces

boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        boton.click()
        time.sleep(random.uniform(15.0, 20.0))
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

#todos los anuncios de una lista
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

precio = list()
descripcion = list ()

for auto in autos:
    precio.append(auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text)
   
    
    descripcion.append(auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text)
    
    
    
dict = {'Coches': descripcion,'Precio':precio}

df = pd.DataFrame(dict)

print(df)













