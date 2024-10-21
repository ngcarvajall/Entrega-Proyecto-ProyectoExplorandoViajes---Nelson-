# %%

import requests

url = "https://sky-scrapper.p.rapidapi.com/api/v2/flights/searchFlights"

querystring = {"originSkyId":"MAD","destinationSkyId":"LIS","originEntityId":"95565077","destinationEntityId":"95565055","date":"2024-10-25","returnDate":"2024-10-28","cabinClass":"economy","adults":"1","sortBy":"best","limit":"25","currency":"EUR"}

headers = {
	"x-rapidapi-key": "8bf68f7481msh7aa93c8e8e9a6ffp19eef8jsn33f2cc37fe85",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

viajes = response.json()


with open('vuelos.json', 'w') as archivo_json:
    json.dump(viajes, archivo_json, indent=4)
viajes['data'].keys()
info_vuelo = len(viajes['data']['itineraries'])
precios = viajes['data']['itineraries'][0]['price']['raw']
id_inicio = viajes['data']['itineraries'][0]['legs'][0]['origin']['id']
inicio_ciudad = viajes['data']['itineraries'][0]['legs'][0]['origin']['name']
id_regreso = viajes['data']['itineraries'][0]['legs'][0]['destination']['id']
id_regreso
regreso_ciudad = viajes['data']['itineraries'][0]['legs'][0]['destination']['name']
regreso_ciudad
tiempo = viajes['data']['itineraries'][0]['legs'][0]['durationInMinutes']
tiempo
paradas = viajes['data']['itineraries'][0]['legs'][0]['stopCount']
paradas
linea_aerea = viajes['data']['itineraries'][1]['legs'][1]['carriers']['marketing'][0]['name']
linea_aerea
hora_salida = viajes['data']['itineraries'][0]['legs'][0]['departure']
hora_salida
hora_llegada = viajes['data']['itineraries'][0]['legs'][0]['arrival']
hora_llegada
len(viajes['data']['itineraries'])
viajes
lista_de_diccionarios = []
# creo mi lista de diccionarios
for i in range(0,info_vuelo):
    #aquí itero sobre la cantidad de vuelos, 20 en total pero en pares de solo 10
    precios = viajes['data']['itineraries'][i]['price']['raw']
    for j in range(0,2):
        #itero sobre los elementos de ida y vuelta
        id_inicio = viajes['data']['itineraries'][i]['legs'][j]['origin']['id']
        inicio_ciudad = viajes['data']['itineraries'][i]['legs'][j]['origin']['name']
        id_regreso = viajes['data']['itineraries'][i]['legs'][j]['destination']['id']
        regreso_ciudad = viajes['data']['itineraries'][i]['legs'][j]['destination']['name']
        tiempo = viajes['data']['itineraries'][i]['legs'][j]['durationInMinutes']
        paradas = viajes['data']['itineraries'][i]['legs'][j]['stopCount']
        linea_aerea = viajes['data']['itineraries'][i]['legs'][j]['carriers']['marketing'][0]['name']
        hora_salida = viajes['data']['itineraries'][i]['legs'][j]['departure']
        hora_llegada = viajes['data']['itineraries'][i]['legs'][j]['arrival']
        diccionario = {'Costo': precios,
                'ID Salida': id_inicio,
                'Salida': inicio_ciudad,
                'ID Llegada': id_regreso,
                'Llegada': regreso_ciudad,
                'Tiempo': tiempo,
                'Paradas': paradas,
                'Aerolínea': linea_aerea,
                'Hora de Salida': hora_salida,
                'Hora de Llegada': hora_llegada}
        lista_de_diccionarios.append(diccionario)

#creo mi diccionario y le apendeo las listas cada vez que itero
df = pd.DataFrame(lista_de_diccionarios)
df
df.to_csv('datos/vuelos_lisboa_itinerario.csv', index=False)
import requests

url = "https://sky-scrapper.p.rapidapi.com/api/v2/flights/searchFlights"

querystring = {"originSkyId":"MAD","destinationSkyId":"FLR","originEntityId":"95565077","destinationEntityId":"95673830","date":"2024-10-25","returnDate":"2024-10-28","cabinClass":"economy","adults":"1","sortBy":"best","currency":"EUR"}

headers = {
	"x-rapidapi-key": "8bf68f7481msh7aa93c8e8e9a6ffp19eef8jsn33f2cc37fe85",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

viaje_florencia = response.json()
viaje_florencia.keys()
info_cantidad = len(viaje_florencia['data']['itineraries'])
precio_fl = viaje_florencia['data']['itineraries'][0]['price']['raw']
id_fl = viaje_florencia['data']['itineraries'][0]['legs'][0]['origin']['id']
salida_fl = viaje_florencia['data']['itineraries'][0]['legs'][0]['origin']['name']
id_vuelta = viaje_florencia['data']['itineraries'][0]['legs'][0]['destination']['id']
regreso_fl = viaje_florencia['data']['itineraries'][0]['legs'][0]['destination']['name']
tiempo_fl = viaje_florencia['data']['itineraries'][0]['legs'][0]['durationInMinutes']
tiempo_fl
stops = viaje_florencia['data']['itineraries'][0]['legs'][0]['stopCount']
linea_devuelo = viaje_florencia['data']['itineraries'][0]['legs'][0]['carriers']['marketing'][0]['name']
linea_devuelo
salida = viaje_florencia['data']['itineraries'][0]['legs'][0]['departure']
salida
llegada = viaje_florencia['data']['itineraries'][0]['legs'][0]['arrival']
llegada
list_dict = []
for i in range(0,info_cantidad):
    precio_fl = viaje_florencia['data']['itineraries'][i]['price']['raw']    
    for j in range(0,2):
        id_fl = viaje_florencia['data']['itineraries'][i]['legs'][j]['origin']['id']
        salida_fl = viaje_florencia['data']['itineraries'][i]['legs'][j]['origin']['name']
        id_vuelta = viaje_florencia['data']['itineraries'][i]['legs'][j]['destination']['id']
        regreso_fl = viaje_florencia['data']['itineraries'][i]['legs'][j]['destination']['name']
        tiempo_fl = viaje_florencia['data']['itineraries'][i]['legs'][j]['durationInMinutes']
        stops = viaje_florencia['data']['itineraries'][i]['legs'][j]['stopCount']
        linea_devuelo = viaje_florencia['data']['itineraries'][i]['legs'][j]['carriers']['marketing'][0]['name']
        salida = viaje_florencia['data']['itineraries'][i]['legs'][j]['departure']
        llegada = viaje_florencia['data']['itineraries'][i]['legs'][j]['arrival']
        dicty = {'Costo': precio_fl,
                'ID Salida': id_fl,
                'Salida': salida_fl,
                'ID Llegada': id_vuelta,
                'Llegada': regreso_fl,
                'Tiempo': tiempo_fl,
                'Paradas': stops,
                'Aerolínea': linea_devuelo,
                'Hora de Salida': salida,
                'Hora de Llegada': llegada}
        list_dict.append(dicty)
df_florence = pd.DataFrame(list_dict)
df_florence.head()
df_florence.to_csv('datos/vuelos_florencia_itinerario.csv', index=False)
df_florence