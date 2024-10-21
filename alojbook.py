# %%

import requests
#hago mi rquest
url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"

querystring = {"dest_id":"-117543","search_type":"CITY","arrival_date":"2024-10-25","departure_date":"2024-10-28","adults":"1","room_qty":"1","page_number":"1","units":"metric","temperature_unit":"c","languagecode":"en-us","currency_code":"EUR"}

headers = {
	"x-rapidapi-key": "8bf68f7481msh7aa93c8e8e9a6ffp19eef8jsn33f2cc37fe85",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

datos= response.json()
#tengo mis datos a full
datos
clean = datos['data']
#empiezo a adentrarme en mis diccionarios
#busco mis keys
clean.keys()
#al encontrar la info, paso a seguir buscando
hoteles = clean['hotels']
hoteles[0]['property']
#saco el nombre
hoteles[0]['property']['name']
#saco la cantidad de reviews
hoteles[0]['property']['reviewCount']
#saco el score
hoteles[0]['property']['reviewScore']
# precio por las noches
hoteles[0]['property']['priceBreakdown']['grossPrice']['value']
hoteles[0]['property']['checkin']['fromTime']
hoteles[0]['property']['checkin']['untilTime']
hoteles[0]['property']['checkout']['fromTime']
hoteles[0]['property']['checkout']['untilTime']
#lista vacía para meter cosas
lista_datos_dicc = []
for i in range(0,(len(hoteles))):
     ciudad = hoteles[i]['property']['wishlistName']
     nombre = hoteles[i]['property']['name']
     reviewcount = hoteles[i]['property']['reviewCount']
     reviewscore = hoteles[i]['property']['reviewScore']
     precio = hoteles[i]['property']['priceBreakdown']['grossPrice']['value']
     hora_entrada1 = hoteles[i]['property']['checkin']['fromTime']
     hora_entrada2 = hoteles[i]['property']['checkin']['untilTime']
     hora_salida1 = hoteles[i]['property']['checkout']['fromTime']
     hora_salida2 = hoteles[i]['property']['checkout']['untilTime']
     dicc = {
     'Ciudad': ciudad,
     'Hotel': nombre,
     'Cantidad de reviews':reviewcount,
     'Calificación': reviewscore,
     'Precio': precio,
     'Entrada desde': hora_entrada1,
     'Entrada hasta': hora_entrada2,
     'Salida desde': hora_salida1,
     'Salida hasta': hora_salida2}
     lista_datos_dicc.append(dicc)
df = pd.DataFrame(lista_datos_dicc)
df.dtypes
df.to_csv('datos/alojamientos_florencia.csv', index=False)
import requests

url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"

querystring = {"dest_id":"-2167973","search_type":"CITY","arrival_date":"2024-10-25","departure_date":"2024-10-28","adults":"1","room_qty":"1","page_number":"1","units":"metric","temperature_unit":"c","languagecode":"en-us","currency_code":"EUR"}

headers = {
	"x-rapidapi-key": "8bf68f7481msh7aa93c8e8e9a6ffp19eef8jsn33f2cc37fe85",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

datos_lisboa = response.json()
hoteles_lisboa = datos_lisboa['data']['hotels']
len(hoteles_lisboa)
hoteles_lisboa[0]['property'].keys()
hoteles_lisboa[0]['property']['wishlistName']
hoteles_lisboa[0]['property']['name']
hoteles_lisboa[0]['property']['reviewCount']
hoteles_lisboa[0]['property']['reviewScore']
hoteles_lisboa[0]['property']['priceBreakdown']['grossPrice']['value']
lista_dicc_lisboa = []
for i in range(0,(len(hoteles_lisboa))):
     city = hoteles_lisboa[i]['property']['wishlistName']
     name = hoteles_lisboa[i]['property']['name']
     rc = hoteles_lisboa[i]['property']['reviewCount']
     rsc = hoteles_lisboa[i]['property']['reviewScore']
     price = hoteles_lisboa[i]['property']['priceBreakdown']['grossPrice']['value']
     hora_entradal = hoteles_lisboa[i]['property']['checkin']['fromTime']
     hora_entradal2 = hoteles_lisboa[i]['property']['checkin']['untilTime']
     hora_salidal = hoteles_lisboa[i]['property']['checkout']['fromTime']
     hora_salidal2 = hoteles_lisboa[i]['property']['checkout']['untilTime']
     diccionario = {
     'Ciudad': city,
     'Hotel': name,
     'Cantidad de reviews':rc,
     'Calificación': rsc,
     'Precio': price,
     'Entrada desde': hora_entradal,
     'Entrada hasta': hora_entradal2,
     'Salida desde': hora_salidal,
     'Salida hasta': hora_salidal2}
     lista_dicc_lisboa.append(diccionario)
df_lisboa = pd.DataFrame(lista_dicc_lisboa)
df_lisboa.dtypes
df_lisboa.to_csv('datos/alojamientos_lisboa.csv', index=False)
df_vacio = pd.DataFrame()

df_vacio = pd.concat([df_vacio,df,df_lisboa],ignore_index=True)
df_vacio['Precio'].round
df_vacio.to_csv('datos/alojamientos_combinados.csv', index=False)