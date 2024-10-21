# 🌍 Comparativa de Destinos: Florencia y Lisboa

## 📖 Descripción
Este proyecto está enfocado en la comparación de dos destinos turísticos: **Florencia** y **Lisboa**, con el objetivo de ayudar a una persona interesada en conocer las características clave de ambas ciudades para tomar una decisión informada sobre su próximo viaje.

A través de **2 APIs** y técnicas de **Web Scraping**, se ha recopilado y analizado información sobre tres aspectos fundamentales:
1. 🏨 **Hospedajes** (Precios, distancia al centro, calificaciones).
2. ✈️ **Vuelos** (Duración, precio, escalas).
3. 🚶 **Excursiones disponibles** (Tipos de actividades, precios).

El análisis tiene como fin ofrecer una comparativa detallada entre ambos destinos, centrándose en precios, duraciones y opciones de entretenimiento.

## 🗂️ Estructura del Proyecto

# ✈️ Proyecto de Comparación de Destinos: Lisboa vs Florencia

## 📖 Descripción
Este proyecto se enfoca en la comparación de dos destinos turísticos europeos: Lisboa y Florencia. Utilizando Web Scraping y dos APIs, se ha recopilado información relevante sobre alojamientos, vuelos y excursiones disponibles en ambas ciudades. El objetivo es proporcionar una visión clara y comparativa que pueda ser útil para los viajeros interesados en estos destinos.

Los datos analizados incluyen:
- Información sobre **hospedajes** obtenidos mediante scraping y la API de Booking.
- Detalles de **vuelos** entre los destinos, recogidos a través de una API de vuelos.
- Comparación de **excursiones** disponibles en cada ciudad, recopiladas mediante scraping de sitios web especializados.

Este análisis ofrece una visión clara de los precios, la duración de los vuelos y las principales actividades turísticas en ambas ciudades, ayudando a las personas a tomar decisiones informadas sobre su próximo viaje.

## 🗂️ Estructura del Proyecto
├── datos/             # Datos recopilados para el análisis
│   └── archivos.csv    # Datos de las excursiones obtenidos por scraping/APIs
├── EDA/               # Análisis exploratorio de los datos
│   └── eda.ipynb         # Notebook con análisis exploratorio de datos
├── Notebooks/         # Jupyter Notebooks con el código del proyecto
│   ├── alojamientos.ipynb   # Datos de los hospedajes en Lisboa y Florencia
│   ├── excursiones.ipynb   # Datos de excursiones en Lisboa y Florencia
│   └── viajes.ipynb    # Datos de los vuelos en Lisboa y Florencia
├── src/               # Código fuente del proyecto
├── .env               # Variables de entorno para las API keys
├── .gitignore         # Archivos y carpetas que no serán versionados en Git
└── README.md          # Descripción del proyecto

## 🛠️ Instalación y Requisitos
Este proyecto utiliza **Python 3.8** y las siguientes bibliotecas:

- `requests` (para manejar las APIs)
- `beautifulsoup4` (para Web Scraping)
- `pandas` (para manipulación de datos)
- `matplotlib` (para visualizaciones)

🌟 Información Clave del Análisis

🏨 Comparación de Hospedajes
Se han recopilado 40 alojamientos de cada ciudad. Los resultados muestran que los precios en Florencia son más altos, con un promedio de 727€, mientras que en Lisboa, el precio promedio es de 554€. La distribución de los precios en ambas ciudades indica que Florencia tiene más valores atípicos en los extremos superiores.

Precio promedio en Florencia: 727€
Precio promedio en Lisboa: 554€
Mediana en Florencia: Se concentra en precios más elevados.
Mediana en Lisboa: Mayor concentración en el rango medio-bajo.

✈️ Comparación de Vuelos
Los tiempos y precios de los vuelos varían dependiendo de las escalas y las aerolíneas. Los vuelos a Lisboa son más cortos y económicos comparados con Florencia.

Duración promedio de vuelos a Florencia: 265 minutos (desde Madrid).
Duración promedio de vuelos a Lisboa: 82 minutos.
Precio promedio de vuelos a Florencia: Más elevado en comparación con Lisboa.
Precio promedio de vuelos a Lisboa: 152.42€, destacando Ryanair como la aerolínea más accesible.

🚶 Comparación de Excursiones
Las excursiones en Florencia resultan ser un poco más caras, especialmente en actividades relacionadas con museos y monumentos.

Costo promedio de excursiones en Florencia: 81.10€
Costo promedio de excursiones en Lisboa: 59.13€
Excursiones más comunes: Recorridos de un día en ambas ciudades, con predominio de tours a museos en Florencia.

📊 Resultados y Conclusiones
Este análisis comparativo ha revelado diferencias importantes entre los dos destinos:

Florencia es generalmente más costosa en términos de hospedajes y excursiones.
Lisboa ofrece opciones más económicas y vuelos más cortos.
Ambos destinos tienen una oferta variada de actividades turísticas, con Florencia destacándose por sus museos y Lisboa por sus precios más accesibles.
Este proyecto proporciona una visión clara para quien esté interesado en viajar a estas ciudades, y es útil para planificar un presupuesto y decidir qué destino se ajusta mejor a sus expectativas.

🔄 Próximos Pasos
Explorar más ciudades para ofrecer comparativas adicionales.
Implementar un análisis predictivo para evaluar futuras tendencias en precios de vuelos y hospedajes.
Incluir la integración con más APIs para obtener información en tiempo real.

✒️ Autor
Nelson Carvajal - GitHub Profile
