# %%
# Importamos las librerías que necesitamos

# Librerías de extracción de datos
# -----------------------------------------------------------------------

# Importaciones:
# Beautifulsoup
from bs4 import BeautifulSoup

# Requests
import requests

import pandas as pd
import numpy as np

from time import sleep

# Importar librerías para automatización de navegadores web con Selenium
# -----------------------------------------------------------------------
from selenium import webdriver  # Selenium es una herramienta para automatizar la interacción con navegadores web.
from webdriver_manager.chrome import ChromeDriverManager  # ChromeDriverManager gestiona la instalación del controlador de Chrome.
from selenium.webdriver.common.keys import Keys  # Keys es útil para simular eventos de teclado en Selenium.
from selenium.webdriver.support.ui import Select  # Select se utiliza para interactuar con elementos <select> en páginas web.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException # Excepciones comunes de selenium que nos podemos encontrar 
### casi todas lo hacen así, puede que otra no porque percibe las cookies como otra capa
driver = webdriver.Chrome()
url_wunder = "https://www.guias.travel/tour/"
driver.get(url_wunder)
# colocar prints
driver.maximize_window()
driver.implicitly_wait(5) ### es como un sleep, pero aquí va a intentar lo siguiente durante el tiempo que le digo
#aceptamos las cookies
### para las cookies
### el tiempo de python puede ser diferente al navegador
try: 
    driver.find_element("css selector", '#search-form-input').click()
except:
    print('No encuentro el botón')

driver.find_element('css selector', '#search-form-input').send_keys('florencia', Keys.ENTER)
for i in range(5):  # Número de veces que deseas hacer scroll
    driver.execute_script("window.scrollBy(0, 1000);")  # Desplazarse 1000 píxeles hacia abajo
    sleep(1)  # Esperar un segundo entre cada scroll
try: 
    driver.find_element("css selector", '#more_tours > span').click()
except:
    print('No encuentro el botón')
for i in range(5):  # Número de veces que deseas hacer scroll
    driver.execute_script("window.scrollBy(0, 1000);")  # Desplazarse 1000 píxeles hacia abajo
    sleep(1)  # Esperar un segundo entre cada scroll
sopa_excursiones = BeautifulSoup(driver.page_source)

lista_paquetes = sopa_excursiones.findAll('div', {'class': 'strip_all_tour_list'})

# div, class: 
# body > div.container.margin_60.tours_archive_container > div > div.col-lg-9.col-md-8 > div.tour-list > a:nth-child(1) > div > div
excursiones = [viaje.find('h2').getText() for viaje in lista_paquetes]
len(excursiones)
tipo_excursion = [excursion.find('h3').getText() for excursion in lista_paquetes]
len(tipo_excursion)
descripcion = [desc.find('p').getText() for desc in lista_paquetes]
len(descripcion)
lista_precios = sopa_excursiones.findAll('div', {'class': 'price_container'})
precios_generales = [precio.getText() for precio in lista_precios]
lista_duration_florencia = sopa_excursiones('div', {'class': "tduration"})
duracion_florencia = [dur.getText().strip() for dur in lista_duration_florencia]
duracion_florencia

#rango desde 0 al tamaño de mi lista
#itero sobre cada indice
#busco solo los indices impares, si es así lo guardo en mi lista nueva
dflorencia_unicas = [duracion_florencia[i] for i in range(len(duracion_florencia)) if i % 2 == 1]
len(dflorencia_unicas)
len(duracion_florencia)
dflorencia_unicas
lista_precios
#creamos lista vacía
precios = []

for precio in lista_precios:
    #buscame el precio, que ya viene con descuento
    precio_normal = precio.find('div', class_='normal_price')

    # si lo encuentra, añade
    if precio_normal:
        precios.append(precio_normal.text.strip())
       
    # de esta forma puedo buscar en los que no tienen una div clara, que no se han tocado
    else:
        sup_precio = precio.find('sup')
        span_precio = precio.find('span')
        
        # busca el precio en sup, y lo limpia
        if span_precio:
            precios.append(span_precio.text.strip())
        # para todo lo demás, gratis
        else:
            precios.append('Gratis')

precios
diccionario = {'Excursiones': excursiones, 'Tipo de excursión': tipo_excursion, 'Descripción': descripcion, 'Precio': precios}
df = pd.DataFrame(diccionario)
df['Precio'] = df['Precio'].str.replace('€', '').replace('¡Gratis!', '0.00')
df.to_csv('datos/excursiones_florencia.csv', index=False)
#buscamos un parentesis dentro del cual buscamos el signo negativom seguido de un numero de uno o más digitos acompañado del porcentaje, cierra parentesis  sigue el espacio
df['Precio'] = df['Precio'].str.replace(r'\(-\d+%\)\s*', '', regex=True)

# Convertimos la columna a tipo float después de eliminar los porcentajes
df['Precio'] = df['Precio'].astype(float)

#cambiar formato
df
### casi todas lo hacen así, puede que otra no porque percibe las cookies como otra capa
driver = webdriver.Chrome()
url_wunder = "https://www.guias.travel/tour/"
driver.get(url_wunder)
# colocar prints
driver.maximize_window()
driver.implicitly_wait(5) ### es como un sleep, pero aquí va a intentar lo siguiente durante el tiempo que le digo
#aceptamos las cookies
### para las cookies
### el tiempo de python puede ser diferente al navegador
try: 
    driver.find_element("css selector", '#search-form-input').click()
except:
    print('No encuentro el botón')

driver.find_element('css selector', '#search-form-input').send_keys('lisboa', Keys.ENTER)
for i in range(6):  # Número de veces que deseas hacer scroll
    driver.execute_script("window.scrollBy(0, 1000);")  # Desplazarse 1000 píxeles hacia abajo
    sleep(1)  # Esperar un segundo entre cada scroll
sleep(3)
try: 
    driver.find_element("css selector", '#more_tours > span').click()
except:
    print('No encuentro el botón')
for i in range(2):  # Número de veces que deseas hacer scroll
    driver.execute_script("window.scrollBy(0, 1000);")  # Desplazarse 1000 píxeles hacia abajo
    sleep(1)  # Esperar un segundo entre cada scroll
sopa_lisboa = BeautifulSoup(driver.page_source)

lista_paquetes_lisboa = sopa_lisboa.findAll('div', {'class': 'strip_all_tour_list'})
lista_paquetes_lisboa[0]
# div, class: 
# body > div.container.margin_60.tours_archive_container > div > div.col-lg-9.col-md-8 > div.tour-list > a:nth-child(1) > div > div
excursiones_lisboa = [viaje.find('h2').getText() for viaje in lista_paquetes_lisboa]
len(excursiones_lisboa)
tipo_excursion_lisboa = [excursion.find('h3').getText() for excursion in lista_paquetes_lisboa]
len(tipo_excursion_lisboa)
descripcion_lisboa = [desc.find('p').getText() for desc in lista_paquetes_lisboa]
len(descripcion_lisboa)
lista_precios_lisboa = sopa_lisboa.findAll('div', {'class': 'price_container'})
precios_lisboa = [p.getText().strip().replace( ' \nVer más', '') for p in lista_precios_lisboa]
len(precios_lisboa)
lista_duracion = sopa_lisboa('div', {'class': "tduration"})
duraciones_lisboa = [dur.getText().strip() for dur in lista_duracion]
duraciones_lisboa
#rango desde 0 al tamaño de mi lista
#itero sobre cada indice
#busco solo los indices impares, si es así lo guardo en mi lista nueva. 
duraciones_unicas = [duraciones_lisboa[i] for i in range(len(duraciones_lisboa)) if i % 2 == 1]

print(duraciones_unicas)

len(duraciones_unicas)
diccionario_lisboa = {'Excursiones': excursiones_lisboa, 'Tipo de excursión': tipo_excursion_lisboa, 'Descripción': descripcion_lisboa, 'Precio': precios_lisboa, 'Duración':duraciones_unicas}
df_lisboa = pd.DataFrame(diccionario_lisboa)
df_lisboa['Duración']
df_lisboa['Precio'] = df_lisboa['Precio'].str.replace('€', '').astype(float)
#cambiar el formato
df_lisboa
df_lisboa.to_csv('datos/excursiones_lisboa.csv', index=False)
df_lisboa.dtypes