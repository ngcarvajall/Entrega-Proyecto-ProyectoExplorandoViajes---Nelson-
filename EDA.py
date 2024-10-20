{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "import time\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "EDA - Alojamientos Fecha: 25-10-2024 al 28-10-2024\n",
    "Pasos a seguir.\n",
    "* El alojamiento lo he obtenido usando la API de Booking. A través de esta pude extraer los datos con los que estaré trabajando a continuación. En cuanto a los alojamientos, estos ya se han unido en un solo Data Frame. De esta manera, podré comparar en el mismo las cosas directamente. \n",
    "He hecho cierta limpieza a medida que iba dando forma al Data Frame, pero aquí se evaluará mejor formato y descripción de los datos.\n",
    "\n",
    "No tengo nulos ni duplicados.\n",
    "\n",
    "Tengo 40 filas y 9 columnas.\n",
    "\n",
    "El precio medio de hospedaje para estas fechas en Lisboa es de 554€ mientras que en Florencia es de 727€. A esto se suma que el mínimo de hospedaje en Lisboa empieza en 81€ mientras que en Florencia es 145€. También pude observar que la mediana en ambos lugares no es tan distante entre ellos, Florencia: 604.96€ y Lisboa: 514.71€. Sin embargo, tenemos un precio máximo de 1842€ en Florencia y 1001€ en Lisboa. En cuanto a la mediana, en Florencia la mediana es menor que le media debido a que la concentración de precios está más cerca de los precios bajo pero hay valores atípicos que elevan la media ya que son bastante altos (1800€). Con respecto a la mediana de Lisboa, es menor que la media esto porque la concentración de los precios es menor que la media pero al presentarse valores atípicos esta ultima se ve ligeramente elevada que la mediana. \n",
    "\n",
    "Debo señalar que el mínimo de hospedaje en Lisboa empieza en 81€ mientras que en Florencia es 145€.\n",
    "\n",
    "Recalco que la riqueza cultural e histórica de Florencia juega un papel importante ya que algunos alojamientos están bastante cerca de lugares memorables de la ciudad.\n",
    "\n",
    "En cuanto a la calificación promedio, en base a 10, encontré que Florencia tiene una media de 8.77 mientras que Lisboa tiene una de 8.53.\n",
    "En cuanto a la cantidad de reviews, Florencia tiene una media de 1650 que se queda muy distante de la media de Lisboa que se presenta en 3044.\n",
    "* Considerando que los precios son más asequibles para Lisboa, puede que la carga histórica y cultural de Florencia eleve más los precios y que por ende más personas decidan asistir en viajes low-cost a Lisboa.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_florencia_lisboa = pd.read_csv('../datos/alojamientos_combinados.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 40 entries, 0 to 39\n",
      "Data columns (total 9 columns):\n",
      " #   Column               Non-Null Count  Dtype  \n",
      "---  ------               --------------  -----  \n",
      " 0   Ciudad               40 non-null     object \n",
      " 1   Hotel                40 non-null     object \n",
      " 2   Cantidad de reviews  40 non-null     int64  \n",
      " 3   Calificación         40 non-null     float64\n",
      " 4   Precio               40 non-null     float64\n",
      " 5   Entrada desde        40 non-null     object \n",
      " 6   Entrada hasta        40 non-null     object \n",
      " 7   Salida desde         40 non-null     object \n",
      " 8   Salida hasta         40 non-null     object \n",
      "dtypes: float64(2), int64(1), object(6)\n",
      "memory usage: 2.9+ KB\n"
     ]
    }
   ],
   "source": [
    "df_florencia_lisboa.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tengo que convertir las horas en formato datetime. Puedo ver que no tengo nulos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ciudad</th>\n",
       "      <th>Hotel</th>\n",
       "      <th>Cantidad de reviews</th>\n",
       "      <th>Calificación</th>\n",
       "      <th>Precio</th>\n",
       "      <th>Entrada desde</th>\n",
       "      <th>Entrada hasta</th>\n",
       "      <th>Salida desde</th>\n",
       "      <th>Salida hasta</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Florence</td>\n",
       "      <td>Florence Heart Uffizi - Renovated and central</td>\n",
       "      <td>70</td>\n",
       "      <td>9.1</td>\n",
       "      <td>585.000000</td>\n",
       "      <td>15:00</td>\n",
       "      <td>20:00</td>\n",
       "      <td>08:00</td>\n",
       "      <td>10:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Florence</td>\n",
       "      <td>Appartamento la Ninfea</td>\n",
       "      <td>195</td>\n",
       "      <td>8.9</td>\n",
       "      <td>1842.380000</td>\n",
       "      <td>14:00</td>\n",
       "      <td>19:00</td>\n",
       "      <td>07:00</td>\n",
       "      <td>10:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Florence</td>\n",
       "      <td>BorgoDeGreci Apartments</td>\n",
       "      <td>468</td>\n",
       "      <td>8.7</td>\n",
       "      <td>590.630000</td>\n",
       "      <td>14:00</td>\n",
       "      <td>00:00</td>\n",
       "      <td>06:00</td>\n",
       "      <td>10:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Florence</td>\n",
       "      <td>B&amp;B Le Stanze del Duomo</td>\n",
       "      <td>6580</td>\n",
       "      <td>8.5</td>\n",
       "      <td>619.304625</td>\n",
       "      <td>14:00</td>\n",
       "      <td>21:00</td>\n",
       "      <td>08:00</td>\n",
       "      <td>11:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Florence</td>\n",
       "      <td>Adler Cavalieri Hotel-Private Spa &amp; Gym</td>\n",
       "      <td>3628</td>\n",
       "      <td>8.5</td>\n",
       "      <td>722.000000</td>\n",
       "      <td>15:00</td>\n",
       "      <td>00:00</td>\n",
       "      <td>00:00</td>\n",
       "      <td>12:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Ciudad                                          Hotel  \\\n",
       "0  Florence  Florence Heart Uffizi - Renovated and central   \n",
       "1  Florence                         Appartamento la Ninfea   \n",
       "2  Florence                        BorgoDeGreci Apartments   \n",
       "3  Florence                        B&B Le Stanze del Duomo   \n",
       "4  Florence        Adler Cavalieri Hotel-Private Spa & Gym   \n",
       "\n",
       "   Cantidad de reviews  Calificación       Precio Entrada desde Entrada hasta  \\\n",
       "0                   70           9.1   585.000000         15:00         20:00   \n",
       "1                  195           8.9  1842.380000         14:00         19:00   \n",
       "2                  468           8.7   590.630000         14:00         00:00   \n",
       "3                 6580           8.5   619.304625         14:00         21:00   \n",
       "4                 3628           8.5   722.000000         15:00         00:00   \n",
       "\n",
       "  Salida desde Salida hasta  \n",
       "0        08:00        10:00  \n",
       "1        07:00        10:00  \n",
       "2        06:00        10:00  \n",
       "3        08:00        11:00  \n",
       "4        00:00        12:00  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_florencia_lisboa['Precio'] = df_florencia_lisboa['Precio'].round(2)\n",
    "# quitamos el exceso de ceros en el precio\n",
    "#  redondeo los precios a dos decimales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ciudad</th>\n",
       "      <th>Hotel</th>\n",
       "      <th>Cantidad de reviews</th>\n",
       "      <th>Calificación</th>\n",
       "      <th>Precio</th>\n",
       "      <th>Entrada desde</th>\n",
       "      <th>Entrada hasta</th>\n",
       "      <th>Salida desde</th>\n",
       "      <th>Salida hasta</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Florence</td>\n",
       "      <td>Florence Heart Uffizi - Renovated and central</td>\n",
       "      <td>70</td>\n",
       "      <td>9.1</td>\n",
       "      <td>585.0</td>\n",
       "      <td>15:00</td>\n",
       "      <td>20:00</td>\n",
       "      <td>08:00</td>\n",
       "      <td>10:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Ciudad                                          Hotel  \\\n",
       "0  Florence  Florence Heart Uffizi - Renovated and central   \n",
       "\n",
       "   Cantidad de reviews  Calificación  Precio Entrada desde Entrada hasta  \\\n",
       "0                   70           9.1   585.0         15:00         20:00   \n",
       "\n",
       "  Salida desde Salida hasta  \n",
       "0        08:00        10:00  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(40, 9)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Ciudad', 'Hotel', 'Cantidad de reviews', 'Calificación', 'Precio',\n",
       "       'Entrada desde', 'Entrada hasta', 'Salida desde', 'Salida hasta'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Cantidad de reviews</th>\n",
       "      <th>Calificación</th>\n",
       "      <th>Precio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>40.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2347.700000</td>\n",
       "      <td>8.652500</td>\n",
       "      <td>641.281500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1961.433244</td>\n",
       "      <td>0.479309</td>\n",
       "      <td>341.147894</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>7.200000</td>\n",
       "      <td>81.870000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>821.750000</td>\n",
       "      <td>8.400000</td>\n",
       "      <td>484.857500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1557.000000</td>\n",
       "      <td>8.700000</td>\n",
       "      <td>587.815000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3835.750000</td>\n",
       "      <td>8.925000</td>\n",
       "      <td>704.172500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>6580.000000</td>\n",
       "      <td>9.500000</td>\n",
       "      <td>1842.380000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Cantidad de reviews  Calificación       Precio\n",
       "count            40.000000     40.000000    40.000000\n",
       "mean           2347.700000      8.652500   641.281500\n",
       "std            1961.433244      0.479309   341.147894\n",
       "min               5.000000      7.200000    81.870000\n",
       "25%             821.750000      8.400000   484.857500\n",
       "50%            1557.000000      8.700000   587.815000\n",
       "75%            3835.750000      8.925000   704.172500\n",
       "max            6580.000000      9.500000  1842.380000"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ciudad</th>\n",
       "      <th>Hotel</th>\n",
       "      <th>Entrada desde</th>\n",
       "      <th>Entrada hasta</th>\n",
       "      <th>Salida desde</th>\n",
       "      <th>Salida hasta</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>40</td>\n",
       "      <td>40</td>\n",
       "      <td>40</td>\n",
       "      <td>40</td>\n",
       "      <td>40</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>2</td>\n",
       "      <td>40</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>Florence</td>\n",
       "      <td>Florence Heart Uffizi - Renovated and central</td>\n",
       "      <td>14:00</td>\n",
       "      <td>00:00</td>\n",
       "      <td>00:00</td>\n",
       "      <td>12:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>19</td>\n",
       "      <td>27</td>\n",
       "      <td>24</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Ciudad                                          Hotel Entrada desde  \\\n",
       "count         40                                             40            40   \n",
       "unique         2                                             40             7   \n",
       "top     Florence  Florence Heart Uffizi - Renovated and central         14:00   \n",
       "freq          20                                              1            19   \n",
       "\n",
       "       Entrada hasta Salida desde Salida hasta  \n",
       "count             40           40           40  \n",
       "unique             7            7            5  \n",
       "top            00:00        00:00        12:00  \n",
       "freq              27           24           16  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.describe(include='O')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Ciudad\n",
       "Florence    727.991\n",
       "Lisbon      554.572\n",
       "Name: Precio, dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.groupby('Ciudad')['Precio'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Ciudad\n",
       "Florence    604.965\n",
       "Lisbon      514.710\n",
       "Name: Precio, dtype: float64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.groupby('Ciudad')['Precio'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Ciudad\n",
       "Florence    8.775\n",
       "Lisbon      8.530\n",
       "Name: Calificación, dtype: float64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.groupby('Ciudad')['Calificación'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El precio medio de hospedaje para estas fechas en Lisboa es de 554€ mientras que en Florencia es de 727€."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ciudad</th>\n",
       "      <th>Florence</th>\n",
       "      <th>Lisbon</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"8\" valign=\"top\">Cantidad de reviews</th>\n",
       "      <th>count</th>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1650.750000</td>\n",
       "      <td>3044.650000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1678.261942</td>\n",
       "      <td>2014.386710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>70.000000</td>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>448.750000</td>\n",
       "      <td>1107.250000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1253.500000</td>\n",
       "      <td>3312.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2116.750000</td>\n",
       "      <td>4820.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>6580.000000</td>\n",
       "      <td>5874.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"8\" valign=\"top\">Calificación</th>\n",
       "      <th>count</th>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>8.775000</td>\n",
       "      <td>8.530000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.378188</td>\n",
       "      <td>0.544929</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>7.800000</td>\n",
       "      <td>7.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>8.500000</td>\n",
       "      <td>8.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>8.800000</td>\n",
       "      <td>8.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>9.025000</td>\n",
       "      <td>8.825000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.400000</td>\n",
       "      <td>9.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"8\" valign=\"top\">Precio</th>\n",
       "      <th>count</th>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>727.991000</td>\n",
       "      <td>554.572000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>412.611753</td>\n",
       "      <td>229.808998</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>145.000000</td>\n",
       "      <td>81.870000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>555.922500</td>\n",
       "      <td>454.050000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>604.965000</td>\n",
       "      <td>514.710000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>704.172500</td>\n",
       "      <td>672.975000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1842.380000</td>\n",
       "      <td>1001.710000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Ciudad                        Florence       Lisbon\n",
       "Cantidad de reviews count    20.000000    20.000000\n",
       "                    mean   1650.750000  3044.650000\n",
       "                    std    1678.261942  2014.386710\n",
       "                    min      70.000000     5.000000\n",
       "                    25%     448.750000  1107.250000\n",
       "                    50%    1253.500000  3312.000000\n",
       "                    75%    2116.750000  4820.500000\n",
       "                    max    6580.000000  5874.000000\n",
       "Calificación        count    20.000000    20.000000\n",
       "                    mean      8.775000     8.530000\n",
       "                    std       0.378188     0.544929\n",
       "                    min       7.800000     7.200000\n",
       "                    25%       8.500000     8.200000\n",
       "                    50%       8.800000     8.600000\n",
       "                    75%       9.025000     8.825000\n",
       "                    max       9.400000     9.500000\n",
       "Precio              count    20.000000    20.000000\n",
       "                    mean    727.991000   554.572000\n",
       "                    std     412.611753   229.808998\n",
       "                    min     145.000000    81.870000\n",
       "                    25%     555.922500   454.050000\n",
       "                    50%     604.965000   514.710000\n",
       "                    75%     704.172500   672.975000\n",
       "                    max    1842.380000  1001.710000"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_florencia_lisboa.groupby('Ciudad').describe().T"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "* Vuelos a Florencia*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A continuación, busco la información sobre los vuelos de MAD-FLR y FLR-MAD durante las fechas del 25-10-2024 al 28-10-2024.\n",
    "\n",
    "En este caso, para Florencia tengo varios horarios duplicados pero destaco el tema de jugar con las combinaciones. Aunque el vuelo de ida pueda repetirse, este tiene una combinación con el vuelo de regreso distinto en todos los caso. Pasa lo mismo con los vuelos duplicados de regreso. \n",
    "\n",
    "Se puede observar claramente con los precios, como cada variación en el horario genera un cambio en los precios. A la vez, aquellos paquetes que hacen escalas, lo que significa una mayor duración del vuelo, tienen un costo menor que aquellos que tienen una trayectoria directa. Esta ruta MAD-FLR tiene una media distinta desde cada ciudad.\n",
    "\n",
    "El precio promedio por ida y vuelta es de 357€ sin considerar aerolíneas. Con una duración de 214 minutos.\n",
    "\n",
    "Podemos ver que los vuelos FLR-MAD tienen un promedio de duración de 163 minutos, mientras que MAD-FLR ascienden a 265 minutos. Esto es visiblemente claro cuando vemos que la duración máxima desde Florencia llega a 284 mientras que saliendo de Madrid puede llegar a 450 minutos. Todo debido a las escalas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_vuelos_florencia = pd.read_csv('../datos/vuelos_florencia_itinerario.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20 entries, 0 to 19\n",
      "Data columns (total 10 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   Costo            20 non-null     float64\n",
      " 1   ID Salida        20 non-null     object \n",
      " 2   Salida           20 non-null     object \n",
      " 3   ID Llegada       20 non-null     object \n",
      " 4   Llegada          20 non-null     object \n",
      " 5   Tiempo           20 non-null     int64  \n",
      " 6   Paradas          20 non-null     int64  \n",
      " 7   Aerolínea        20 non-null     object \n",
      " 8   Hora de Salida   20 non-null     object \n",
      " 9   Hora de Llegada  20 non-null     object \n",
      "dtypes: float64(1), int64(2), object(7)\n",
      "memory usage: 1.7+ KB\n"
     ]
    }
   ],
   "source": [
    "df_vuelos_florencia.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID Salida</th>\n",
       "      <th>Salida</th>\n",
       "      <th>ID Llegada</th>\n",
       "      <th>Llegada</th>\n",
       "      <th>Aerolínea</th>\n",
       "      <th>Hora de Salida</th>\n",
       "      <th>Hora de Llegada</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>10</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>14</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       ID Salida  Salida ID Llegada   Llegada         Aerolínea  \\\n",
       "count         20      20         20        20                20   \n",
       "unique         2       2          2         2                 3   \n",
       "top          MAD  Madrid        FLR  Florence  Vueling Airlines   \n",
       "freq          10      10         10        10                14   \n",
       "\n",
       "             Hora de Salida      Hora de Llegada  \n",
       "count                    20                   20  \n",
       "unique                   10                    9  \n",
       "top     2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "freq                      7                    7  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.describe(include='O')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(10)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia['Hora de Salida'].duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(11)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia['Hora de Llegada'].duplicated().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En este caso, para Florencia tengo varios horarios duplicados pero destaco el tema de jugar con las combinaciones. Aunque el vuelo de ida pueda repetirse, este tiene una combinación con el vuelo de regreso distinto en todos los caso. Pasa lo mismo con los vuelos duplicados de regreso. \n",
    "\n",
    "Se puede observar claramente con los precios, como cada variación en el horario genera un cambio en los precios. A la vez, aquellos paquetes que hacen escalas, lo que significa una mayor duración del vuelo, tienen un costo menor que aquellos que tienen una trayectoria directa."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Costo</th>\n",
       "      <th>ID Salida</th>\n",
       "      <th>Salida</th>\n",
       "      <th>ID Llegada</th>\n",
       "      <th>Llegada</th>\n",
       "      <th>Tiempo</th>\n",
       "      <th>Paradas</th>\n",
       "      <th>Aerolínea</th>\n",
       "      <th>Hora de Salida</th>\n",
       "      <th>Hora de Llegada</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>428.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T09:55:00</td>\n",
       "      <td>2024-10-25T12:15:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>428.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>429.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T15:35:00</td>\n",
       "      <td>2024-10-25T17:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>429.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>290.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>250</td>\n",
       "      <td>1</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T17:20:00</td>\n",
       "      <td>2024-10-25T21:30:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>290.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>281.68</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>300</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T05:50:00</td>\n",
       "      <td>2024-10-25T10:50:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>281.68</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>284</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-28T19:15:00</td>\n",
       "      <td>2024-10-28T23:59:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>451.98</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T09:55:00</td>\n",
       "      <td>2024-10-25T12:15:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>451.98</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T06:15:00</td>\n",
       "      <td>2024-10-28T08:45:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>438.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T15:35:00</td>\n",
       "      <td>2024-10-25T17:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>438.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T06:15:00</td>\n",
       "      <td>2024-10-28T08:45:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>295.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>380</td>\n",
       "      <td>1</td>\n",
       "      <td>Air Europa</td>\n",
       "      <td>2024-10-25T15:10:00</td>\n",
       "      <td>2024-10-25T21:30:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>295.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>308.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>450</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T07:05:00</td>\n",
       "      <td>2024-10-25T14:35:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>308.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>316.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>300</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T05:50:00</td>\n",
       "      <td>2024-10-25T10:50:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>316.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>340.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>415</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T11:35:00</td>\n",
       "      <td>2024-10-25T18:30:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>340.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Costo ID Salida    Salida ID Llegada   Llegada  Tiempo  Paradas  \\\n",
       "0   428.00       MAD    Madrid        FLR  Florence     140        0   \n",
       "1   428.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "2   429.00       MAD    Madrid        FLR  Florence     140        0   \n",
       "3   429.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "4   290.00       MAD    Madrid        FLR  Florence     250        1   \n",
       "5   290.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "6   281.68       MAD    Madrid        FLR  Florence     300        1   \n",
       "7   281.68       FLR  Florence        MAD    Madrid     284        1   \n",
       "8   451.98       MAD    Madrid        FLR  Florence     140        0   \n",
       "9   451.98       FLR  Florence        MAD    Madrid     150        0   \n",
       "10  438.00       MAD    Madrid        FLR  Florence     140        0   \n",
       "11  438.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "12  295.00       MAD    Madrid        FLR  Florence     380        1   \n",
       "13  295.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "14  308.00       MAD    Madrid        FLR  Florence     450        1   \n",
       "15  308.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "16  316.00       MAD    Madrid        FLR  Florence     300        1   \n",
       "17  316.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "18  340.00       MAD    Madrid        FLR  Florence     415        1   \n",
       "19  340.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "\n",
       "           Aerolínea       Hora de Salida      Hora de Llegada  \n",
       "0   Vueling Airlines  2024-10-25T09:55:00  2024-10-25T12:15:00  \n",
       "1   Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "2   Vueling Airlines  2024-10-25T15:35:00  2024-10-25T17:55:00  \n",
       "3   Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "4   Vueling Airlines  2024-10-25T17:20:00  2024-10-25T21:30:00  \n",
       "5   Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "6        ITA Airways  2024-10-25T05:50:00  2024-10-25T10:50:00  \n",
       "7        ITA Airways  2024-10-28T19:15:00  2024-10-28T23:59:00  \n",
       "8   Vueling Airlines  2024-10-25T09:55:00  2024-10-25T12:15:00  \n",
       "9   Vueling Airlines  2024-10-28T06:15:00  2024-10-28T08:45:00  \n",
       "10  Vueling Airlines  2024-10-25T15:35:00  2024-10-25T17:55:00  \n",
       "11  Vueling Airlines  2024-10-28T06:15:00  2024-10-28T08:45:00  \n",
       "12        Air Europa  2024-10-25T15:10:00  2024-10-25T21:30:00  \n",
       "13  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "14       ITA Airways  2024-10-25T07:05:00  2024-10-25T14:35:00  \n",
       "15  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "16       ITA Airways  2024-10-25T05:50:00  2024-10-25T10:50:00  \n",
       "17  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "18       ITA Airways  2024-10-25T11:35:00  2024-10-25T18:30:00  \n",
       "19  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Aerolínea\n",
       "Air Europa          295.000000\n",
       "ITA Airways         305.472000\n",
       "Vueling Airlines    380.925714\n",
       "Name: Costo, dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.groupby('Aerolínea')['Costo'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Salida</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Florence</th>\n",
       "      <td>10.0</td>\n",
       "      <td>163.4</td>\n",
       "      <td>42.374521</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>284.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Madrid</th>\n",
       "      <td>10.0</td>\n",
       "      <td>265.5</td>\n",
       "      <td>122.530042</td>\n",
       "      <td>140.0</td>\n",
       "      <td>140.0</td>\n",
       "      <td>275.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>450.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          count   mean         std    min    25%    50%    75%    max\n",
       "Salida                                                               \n",
       "Florence   10.0  163.4   42.374521  150.0  150.0  150.0  150.0  284.0\n",
       "Madrid     10.0  265.5  122.530042  140.0  140.0  275.0  360.0  450.0"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.groupby('Salida')['Tiempo'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20, 10)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Costo', 'ID Salida', 'Salida', 'ID Llegada', 'Llegada', 'Tiempo',\n",
       "       'Paradas', 'Aerolínea', 'Hora de Salida', 'Hora de Llegada'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Aerolínea\n",
       "Vueling Airlines    70.0\n",
       "ITA Airways         25.0\n",
       "Air Europa           5.0\n",
       "Name: proportion, dtype: float64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia['Aerolínea'].value_counts(normalize=True) * 100"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Puedo observar que de las tres aerolíneas, Vueling tiene el 70% de los vuelos que se ofrecen en estas fechas de ida y vuelta. Seguidos de ITA Airways."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Salida</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Florence</th>\n",
       "      <td>10.0</td>\n",
       "      <td>163.4</td>\n",
       "      <td>42.374521</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>284.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Madrid</th>\n",
       "      <td>10.0</td>\n",
       "      <td>265.5</td>\n",
       "      <td>122.530042</td>\n",
       "      <td>140.0</td>\n",
       "      <td>140.0</td>\n",
       "      <td>275.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>450.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          count   mean         std    min    25%    50%    75%    max\n",
       "Salida                                                               \n",
       "Florence   10.0  163.4   42.374521  150.0  150.0  150.0  150.0  284.0\n",
       "Madrid     10.0  265.5  122.530042  140.0  140.0  275.0  360.0  450.0"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.groupby('Salida')['Tiempo'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Costo</th>\n",
       "      <th>Tiempo</th>\n",
       "      <th>Paradas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>20.00000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.00000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>357.76600</td>\n",
       "      <td>214.450000</td>\n",
       "      <td>0.35000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>68.19356</td>\n",
       "      <td>103.467501</td>\n",
       "      <td>0.48936</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>281.68000</td>\n",
       "      <td>140.000000</td>\n",
       "      <td>0.00000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>295.00000</td>\n",
       "      <td>150.000000</td>\n",
       "      <td>0.00000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>328.00000</td>\n",
       "      <td>150.000000</td>\n",
       "      <td>0.00000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>429.00000</td>\n",
       "      <td>288.000000</td>\n",
       "      <td>1.00000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>451.98000</td>\n",
       "      <td>450.000000</td>\n",
       "      <td>1.00000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Costo      Tiempo   Paradas\n",
       "count   20.00000   20.000000  20.00000\n",
       "mean   357.76600  214.450000   0.35000\n",
       "std     68.19356  103.467501   0.48936\n",
       "min    281.68000  140.000000   0.00000\n",
       "25%    295.00000  150.000000   0.00000\n",
       "50%    328.00000  150.000000   0.00000\n",
       "75%    429.00000  288.000000   1.00000\n",
       "max    451.98000  450.000000   1.00000"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Podemos ver que los vuelos FLR-MAD tienen un promedio de duración de 163 minutos, mientras que MAD-FLR ascienden a 265 minutos. Esto es visiblemente claro cuando vemos que la duración máxima desde Florencia llega a 284 mientras que saliendo de Madrid puede llegar a 450 minutos. Todo debido a las escalas."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "A partir de aquí, empiezo a ver los datos para los vuelos a Lisboa.\n",
    "\n",
    "*No hay nulos, aunque sí duplicados. Ocurre lo mismo que para la otra ruta, existen vuelos duplicados pero que se mantienen al venderse dentro de un paquete que varía las horas de regreso.\n",
    "\n",
    "En relación a los vuelos, cuento con 3 opciones de aerolíneas: easyJet (50%), Ryanair (30%) e Iberia (20%). Esto significa que easyJet tiene la mitad de los vuelos de esta ruta MAD-LIS/LIS-MAD.\n",
    "\n",
    "El costo promedio de un vuelo a Lisboa se encuentra en 152.42, cabe resaltar que la mediana de esta ruta es incluso menor (149.17€). Esto muestra que esta es una ruta más accesible y cuenta con menos disturbios, ya que no cuenta con escalas en ninguna de las rutas propuestas.\n",
    "El tiempo es bastante uniforme por la razón de que no tiene escalas, el timpo promedio es de 82.75 que se traduce a 1h 23 min.\n",
    "\n",
    "El costo promedio de un vuelo a Lisboa se encuentra en 152.42, cabe resaltar que la mediana de esta ruta es incluso menor (149.17€). Esto muestra que esta es una ruta más accesible y cuenta con menos disturbios, ya que no cuenta con escalas en ninguna de las rutas propuestas.\n",
    "El tiempo es bastante uniforme por la razón de que no tiene escalas, el timpo promedio es de 82.75 que se traduce a 1h 23 min.\n",
    "\n",
    "Con respecto a las aerolíneas, la que cuenta con un promedio más bajo es Ryanair con 145€.\n",
    "\n",
    "Se puede observar que existe un duplicado, que se repite 4 veces. Este es el caso que muestro arriba: vuelo MAD-LIS, con easyJet, en horario de 22:35 a 22:55. Esto sucede porque este mismo vuelo de ida, cuenta con 4 opciones de vuelo de regreso LIS-MAD. Por lo que, a pesar de estar duplicado, tiene sentido que se mantenga. Además, al ser una combinación de vuelos, la vuelta tiene horarios distintos por lo que se refleja también en su precio. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_vuelos_lisboa = pd.read_csv('../datos/vuelos_lisboa_itinerario.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Costo</th>\n",
       "      <th>ID Salida</th>\n",
       "      <th>Salida</th>\n",
       "      <th>ID Llegada</th>\n",
       "      <th>Llegada</th>\n",
       "      <th>Tiempo</th>\n",
       "      <th>Paradas</th>\n",
       "      <th>Aerolínea</th>\n",
       "      <th>Hora de Salida</th>\n",
       "      <th>Hora de Llegada</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>154.36</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-25T22:35:00</td>\n",
       "      <td>2024-10-25T22:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>154.36</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "      <td>2024-10-28T17:25:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>160.41</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>Iberia</td>\n",
       "      <td>2024-10-25T23:00:00</td>\n",
       "      <td>2024-10-25T23:25:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>160.41</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>Iberia</td>\n",
       "      <td>2024-10-28T12:30:00</td>\n",
       "      <td>2024-10-28T14:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>130.80</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>Ryanair</td>\n",
       "      <td>2024-10-25T21:35:00</td>\n",
       "      <td>2024-10-25T22:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>130.80</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>Ryanair</td>\n",
       "      <td>2024-10-28T22:00:00</td>\n",
       "      <td>2024-10-29T00:20:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>146.36</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-25T22:35:00</td>\n",
       "      <td>2024-10-25T22:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>146.36</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-28T20:00:00</td>\n",
       "      <td>2024-10-28T22:25:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>146.36</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-25T22:35:00</td>\n",
       "      <td>2024-10-25T22:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>146.36</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-28T07:15:00</td>\n",
       "      <td>2024-10-28T09:40:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>187.30</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-25T09:55:00</td>\n",
       "      <td>2024-10-25T10:20:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>187.30</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>Ryanair</td>\n",
       "      <td>2024-10-28T22:00:00</td>\n",
       "      <td>2024-10-29T00:20:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>173.41</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>Iberia</td>\n",
       "      <td>2024-10-25T23:00:00</td>\n",
       "      <td>2024-10-25T23:25:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>173.41</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>Iberia</td>\n",
       "      <td>2024-10-28T18:45:00</td>\n",
       "      <td>2024-10-28T21:10:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>151.98</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>Ryanair</td>\n",
       "      <td>2024-10-25T21:35:00</td>\n",
       "      <td>2024-10-25T22:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>151.98</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "      <td>2024-10-28T17:25:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>143.98</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>Ryanair</td>\n",
       "      <td>2024-10-25T21:35:00</td>\n",
       "      <td>2024-10-25T22:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>143.98</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-28T20:00:00</td>\n",
       "      <td>2024-10-28T22:25:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>129.30</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-25T22:35:00</td>\n",
       "      <td>2024-10-25T22:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>129.30</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>Ryanair</td>\n",
       "      <td>2024-10-28T22:00:00</td>\n",
       "      <td>2024-10-29T00:20:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Costo ID Salida  Salida ID Llegada Llegada  Tiempo  Paradas Aerolínea  \\\n",
       "0   154.36       MAD  Madrid        LIS  Lisbon      80        0   easyJet   \n",
       "1   154.36       LIS  Lisbon        MAD  Madrid      80        0   easyJet   \n",
       "2   160.41       MAD  Madrid        LIS  Lisbon      85        0    Iberia   \n",
       "3   160.41       LIS  Lisbon        MAD  Madrid      85        0    Iberia   \n",
       "4   130.80       MAD  Madrid        LIS  Lisbon      85        0   Ryanair   \n",
       "5   130.80       LIS  Lisbon        MAD  Madrid      80        0   Ryanair   \n",
       "6   146.36       MAD  Madrid        LIS  Lisbon      80        0   easyJet   \n",
       "7   146.36       LIS  Lisbon        MAD  Madrid      85        0   easyJet   \n",
       "8   146.36       MAD  Madrid        LIS  Lisbon      80        0   easyJet   \n",
       "9   146.36       LIS  Lisbon        MAD  Madrid      85        0   easyJet   \n",
       "10  187.30       MAD  Madrid        LIS  Lisbon      85        0   easyJet   \n",
       "11  187.30       LIS  Lisbon        MAD  Madrid      80        0   Ryanair   \n",
       "12  173.41       MAD  Madrid        LIS  Lisbon      85        0    Iberia   \n",
       "13  173.41       LIS  Lisbon        MAD  Madrid      85        0    Iberia   \n",
       "14  151.98       MAD  Madrid        LIS  Lisbon      85        0   Ryanair   \n",
       "15  151.98       LIS  Lisbon        MAD  Madrid      80        0   easyJet   \n",
       "16  143.98       MAD  Madrid        LIS  Lisbon      85        0   Ryanair   \n",
       "17  143.98       LIS  Lisbon        MAD  Madrid      85        0   easyJet   \n",
       "18  129.30       MAD  Madrid        LIS  Lisbon      80        0   easyJet   \n",
       "19  129.30       LIS  Lisbon        MAD  Madrid      80        0   Ryanair   \n",
       "\n",
       "         Hora de Salida      Hora de Llegada  \n",
       "0   2024-10-25T22:35:00  2024-10-25T22:55:00  \n",
       "1   2024-10-28T15:05:00  2024-10-28T17:25:00  \n",
       "2   2024-10-25T23:00:00  2024-10-25T23:25:00  \n",
       "3   2024-10-28T12:30:00  2024-10-28T14:55:00  \n",
       "4   2024-10-25T21:35:00  2024-10-25T22:00:00  \n",
       "5   2024-10-28T22:00:00  2024-10-29T00:20:00  \n",
       "6   2024-10-25T22:35:00  2024-10-25T22:55:00  \n",
       "7   2024-10-28T20:00:00  2024-10-28T22:25:00  \n",
       "8   2024-10-25T22:35:00  2024-10-25T22:55:00  \n",
       "9   2024-10-28T07:15:00  2024-10-28T09:40:00  \n",
       "10  2024-10-25T09:55:00  2024-10-25T10:20:00  \n",
       "11  2024-10-28T22:00:00  2024-10-29T00:20:00  \n",
       "12  2024-10-25T23:00:00  2024-10-25T23:25:00  \n",
       "13  2024-10-28T18:45:00  2024-10-28T21:10:00  \n",
       "14  2024-10-25T21:35:00  2024-10-25T22:00:00  \n",
       "15  2024-10-28T15:05:00  2024-10-28T17:25:00  \n",
       "16  2024-10-25T21:35:00  2024-10-25T22:00:00  \n",
       "17  2024-10-28T20:00:00  2024-10-28T22:25:00  \n",
       "18  2024-10-25T22:35:00  2024-10-25T22:55:00  \n",
       "19  2024-10-28T22:00:00  2024-10-29T00:20:00  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_lisboa "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20 entries, 0 to 19\n",
      "Data columns (total 10 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   Costo            20 non-null     float64\n",
      " 1   ID Salida        20 non-null     object \n",
      " 2   Salida           20 non-null     object \n",
      " 3   ID Llegada       20 non-null     object \n",
      " 4   Llegada          20 non-null     object \n",
      " 5   Tiempo           20 non-null     int64  \n",
      " 6   Paradas          20 non-null     int64  \n",
      " 7   Aerolínea        20 non-null     object \n",
      " 8   Hora de Salida   20 non-null     object \n",
      " 9   Hora de Llegada  20 non-null     object \n",
      "dtypes: float64(1), int64(2), object(7)\n",
      "memory usage: 1.7+ KB\n"
     ]
    }
   ],
   "source": [
    "df_vuelos_lisboa.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Aerolínea\n",
       "easyJet    50.0\n",
       "Ryanair    30.0\n",
       "Iberia     20.0\n",
       "Name: proportion, dtype: float64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_lisboa['Aerolínea'].value_counts(normalize=True) * 100"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En relación a los vuelos, cuento con 3 opciones de aerolíneas: easyJet (50%), Ryanair (30%) e Iberia (20%). Esto significa que easyJet tiene la mitad de los vuelos de esta ruta MAD-LIS/LIS-MAD."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_vuelos_lisboa['Costo'] = df_vuelos_lisboa['Costo'].round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Costo</th>\n",
       "      <th>Tiempo</th>\n",
       "      <th>Paradas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>20.00</td>\n",
       "      <td>20.00</td>\n",
       "      <td>20.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>152.43</td>\n",
       "      <td>82.75</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>17.39</td>\n",
       "      <td>2.55</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>129.30</td>\n",
       "      <td>80.00</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>143.98</td>\n",
       "      <td>80.00</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>149.17</td>\n",
       "      <td>85.00</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>160.41</td>\n",
       "      <td>85.00</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>187.30</td>\n",
       "      <td>85.00</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Costo  Tiempo  Paradas\n",
       "count   20.00   20.00     20.0\n",
       "mean   152.43   82.75      0.0\n",
       "std     17.39    2.55      0.0\n",
       "min    129.30   80.00      0.0\n",
       "25%    143.98   80.00      0.0\n",
       "50%    149.17   85.00      0.0\n",
       "75%    160.41   85.00      0.0\n",
       "max    187.30   85.00      0.0"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_lisboa.describe().round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Aerolínea</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Iberia</th>\n",
       "      <td>4.0</td>\n",
       "      <td>166.910000</td>\n",
       "      <td>7.505553</td>\n",
       "      <td>160.41</td>\n",
       "      <td>160.41</td>\n",
       "      <td>166.91</td>\n",
       "      <td>173.410</td>\n",
       "      <td>173.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ryanair</th>\n",
       "      <td>6.0</td>\n",
       "      <td>145.693333</td>\n",
       "      <td>22.297697</td>\n",
       "      <td>129.30</td>\n",
       "      <td>130.80</td>\n",
       "      <td>137.39</td>\n",
       "      <td>149.980</td>\n",
       "      <td>187.30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>easyJet</th>\n",
       "      <td>10.0</td>\n",
       "      <td>150.672000</td>\n",
       "      <td>14.706169</td>\n",
       "      <td>129.30</td>\n",
       "      <td>146.36</td>\n",
       "      <td>146.36</td>\n",
       "      <td>153.765</td>\n",
       "      <td>187.30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           count        mean        std     min     25%     50%      75%  \\\n",
       "Aerolínea                                                                  \n",
       "Iberia       4.0  166.910000   7.505553  160.41  160.41  166.91  173.410   \n",
       "Ryanair      6.0  145.693333  22.297697  129.30  130.80  137.39  149.980   \n",
       "easyJet     10.0  150.672000  14.706169  129.30  146.36  146.36  153.765   \n",
       "\n",
       "              max  \n",
       "Aerolínea          \n",
       "Iberia     173.41  \n",
       "Ryanair    187.30  \n",
       "easyJet    187.30  "
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_lisboa.groupby('Aerolínea')['Costo'].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El costo promedio de un vuelo a Lisboa se encuentra en 152.42, cabe resaltar que la mediana de esta ruta es incluso menor (149.17€). Esto muestra que esta es una ruta más accesible y cuenta con menos disturbios, ya que no cuenta con escalas en ninguna de las rutas propuestas.\n",
    "El tiempo es bastante uniforme por la razón de que no tiene escalas, el timpo promedio es de 82.75 que se traduce a 1h 23 min.\n",
    "\n",
    "Con respecto a las aerolíneas, la que cuenta con un promedio más bajo es Ryanair con 145€."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID Salida</th>\n",
       "      <th>Salida</th>\n",
       "      <th>ID Llegada</th>\n",
       "      <th>Llegada</th>\n",
       "      <th>Aerolínea</th>\n",
       "      <th>Hora de Salida</th>\n",
       "      <th>Hora de Llegada</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-25T22:35:00</td>\n",
       "      <td>2024-10-25T22:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       ID Salida  Salida ID Llegada Llegada Aerolínea       Hora de Salida  \\\n",
       "count         20      20         20      20        20                   20   \n",
       "unique         2       2          2       2         3                   10   \n",
       "top          MAD  Madrid        LIS  Lisbon   easyJet  2024-10-25T22:35:00   \n",
       "freq          10      10         10      10        10                    4   \n",
       "\n",
       "            Hora de Llegada  \n",
       "count                    20  \n",
       "unique                   10  \n",
       "top     2024-10-25T22:55:00  \n",
       "freq                      4  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_lisboa.describe(include='O')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Costo</th>\n",
       "      <th>ID Salida</th>\n",
       "      <th>Salida</th>\n",
       "      <th>ID Llegada</th>\n",
       "      <th>Llegada</th>\n",
       "      <th>Tiempo</th>\n",
       "      <th>Paradas</th>\n",
       "      <th>Aerolínea</th>\n",
       "      <th>Hora de Salida</th>\n",
       "      <th>Hora de Llegada</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>146.36</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>LIS</td>\n",
       "      <td>Lisbon</td>\n",
       "      <td>80</td>\n",
       "      <td>0</td>\n",
       "      <td>easyJet</td>\n",
       "      <td>2024-10-25T22:35:00</td>\n",
       "      <td>2024-10-25T22:55:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Costo ID Salida  Salida ID Llegada Llegada  Tiempo  Paradas Aerolínea  \\\n",
       "8  146.36       MAD  Madrid        LIS  Lisbon      80        0   easyJet   \n",
       "\n",
       "        Hora de Salida      Hora de Llegada  \n",
       "8  2024-10-25T22:35:00  2024-10-25T22:55:00  "
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_lisboa[df_vuelos_lisboa.duplicated()]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se puede observar que existe un duplicado, que se repite 4 veces. Este es el caso que muestro arriba: vuelo MAD-LIS, con easyJet, en horario de 22:35 a 22:55. Esto sucede porque este mismo vuelo de ida, cuenta con 4 opciones de vuelo de regreso LIS-MAD. Por lo que, a pesar de estar duplicado, tiene sentido que se mantenga. Además, al ser una combinación de vuelos, la vuelta tiene horarios distintos por lo que se refleja también en su precio. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "--- \n",
    "Excursiones a Florencia:\n",
    "* Pude observar que la media de las actividades se establece en 81.10€, un poco más alta que la mediana (76.18€). Lo que significa que tengo un poco más de concentración en los valores por debajo de la mediana y cuento con datos atípicos altos que elevan la media. Esto se visualiza en los precios, tenemos un par de actividades que son gratuitas pero también cuento con actividades cercanas a los 200€.\n",
    "\n",
    "Las excursiones con mayor cantidad de participación son las que pertenecen a las Excursiones de un día. Las excursiones con un promedio de costo mayor son los museos y monumentos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "excursiones_florencia = pd.read_csv('../datos/excursiones_florencia.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 32 entries, 0 to 31\n",
      "Data columns (total 4 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Excursiones        32 non-null     object \n",
      " 1   Tipo de excursión  32 non-null     object \n",
      " 2   Descripción        32 non-null     object \n",
      " 3   Precio             32 non-null     float64\n",
      "dtypes: float64(1), object(3)\n",
      "memory usage: 1.1+ KB\n"
     ]
    }
   ],
   "source": [
    "excursiones_florencia.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Precio</th>\n",
       "      <td>32.0</td>\n",
       "      <td>81.1</td>\n",
       "      <td>46.91</td>\n",
       "      <td>0.0</td>\n",
       "      <td>53.12</td>\n",
       "      <td>76.18</td>\n",
       "      <td>114.12</td>\n",
       "      <td>181.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        count  mean    std  min    25%    50%     75%    max\n",
       "Precio   32.0  81.1  46.91  0.0  53.12  76.18  114.12  181.0"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_florencia.describe().round(2).T"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Pude observar que la media de las actividades se establece en 81.10€, un poco más alta que la mediana (76.18€). Lo que significa que tengo un poco más de concentración en los valores por debajo de la mediana y cuento con datos atípicos altos que elevan la media. Esto se visualiza en los precios, tenemos un par de actividades que son gratuitas pero también cuento con actividades cercanas a los 200€."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Tipo de excursión\n",
       "Excursiones de un día         37.500\n",
       "Museos y Monumentos           18.750\n",
       "Experiencias Gastronómicas    12.500\n",
       "Visitas Guiadas                9.375\n",
       "Tours a pie                    6.250\n",
       "Free Tours                     3.125\n",
       "Tours en Bus turístico         3.125\n",
       "Tours en Bicicleta             3.125\n",
       "Espectáculos                   3.125\n",
       "Traslados Aeropuertos          3.125\n",
       "Name: proportion, dtype: float64"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_florencia['Tipo de excursión'].value_counts(normalize=True) * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Tipo de excursión\n",
       "Museos y Monumentos           111.733333\n",
       "Experiencias Gastronómicas     96.887500\n",
       "Excursiones de un día          93.195833\n",
       "Visitas Guiadas                69.083333\n",
       "Traslados Aeropuertos          62.000000\n",
       "Tours en Bicicleta             55.000000\n",
       "Tours en Bus turístico         28.750000\n",
       "Espectáculos                   25.000000\n",
       "Tours a pie                    20.500000\n",
       "Free Tours                      0.000000\n",
       "Name: Precio, dtype: float64"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_florencia.groupby('Tipo de excursión')['Precio'].mean().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "* Excursión hacia Lisboa:\n",
    "- No tengo nulos ni duplicados\n",
    "- En este caso, las excursiones de Lisboa tienen una media de costo en 59.13€, ligeramente más baja que la mediana (61.45€). Lo que quiere decir que tengo valores atípicos bajos pero una concentración de valores por encima de los 61€ euros. Esto se traduce a una mayor cantidad de excursiones a menor costo.\n",
    "- Las excursiones de un día toman la mayor cantidad de proporción de las actividades disponibles. A la vez estas tienen un promedio de costo mayor que las demás.\n",
    "- "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "excursiones_lisboa = pd.read_csv('../datos/excursiones_lisboa.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Excursiones', 'Tipo de excursión', 'Descripción', 'Precio',\n",
       "       'Duración'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_lisboa.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 27 entries, 0 to 26\n",
      "Data columns (total 5 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Excursiones        27 non-null     object \n",
      " 1   Tipo de excursión  27 non-null     object \n",
      " 2   Descripción        27 non-null     object \n",
      " 3   Precio             27 non-null     float64\n",
      " 4   Duración           27 non-null     object \n",
      "dtypes: float64(1), object(4)\n",
      "memory usage: 1.2+ KB\n"
     ]
    }
   ],
   "source": [
    "excursiones_lisboa.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Precio</th>\n",
       "      <td>27.0</td>\n",
       "      <td>59.13</td>\n",
       "      <td>27.54</td>\n",
       "      <td>20.0</td>\n",
       "      <td>31.85</td>\n",
       "      <td>61.45</td>\n",
       "      <td>83.5</td>\n",
       "      <td>104.6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        count   mean    std   min    25%    50%   75%    max\n",
       "Precio   27.0  59.13  27.54  20.0  31.85  61.45  83.5  104.6"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_lisboa.describe().round(2).T"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En este caso, las excursiones de Lisboa tienen una media de costo en 59.13€, ligeramente más baja que la mediana (61.45€). Lo que quiere decir que tengo valores atípicos bajos pero una concentración de valores por encima de los 61€ euros. Esto se traduce a una mayor cantidad de excursiones a menor costo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Tipo de excursión\n",
       "Excursiones de un día         29.63\n",
       "Visitas Guiadas               18.52\n",
       "Paseos en barco               11.11\n",
       "Experiencias Gastronómicas     7.41\n",
       "Espectáculos                   7.41\n",
       "Tours en Bus turístico         7.41\n",
       "Pases turísticos               3.70\n",
       "Traslados Aeropuertos          3.70\n",
       "Tours a pie                    3.70\n",
       "Tours en Bicicleta             3.70\n",
       "Alquiler de Vehículos          3.70\n",
       "Name: proportion, dtype: float64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_lisboa['Tipo de excursión'].value_counts(normalize=True).mul(100).round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Tipo de excursión\n",
       "Excursiones de un día         82.90625\n",
       "Paseos en barco               62.40000\n",
       "Visitas Guiadas               61.34000\n",
       "Espectáculos                  55.00000\n",
       "Experiencias Gastronómicas    54.60000\n",
       "Tours a pie                   52.30000\n",
       "Traslados Aeropuertos         34.00000\n",
       "Tours en Bicicleta            33.70000\n",
       "Tours en Bus turístico        28.87500\n",
       "Alquiler de Vehículos         22.50000\n",
       "Pases turísticos              20.00000\n",
       "Name: Precio, dtype: float64"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_lisboa.groupby('Tipo de excursión')['Precio'].mean().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Excursiones</th>\n",
       "      <th>Tipo de excursión</th>\n",
       "      <th>Descripción</th>\n",
       "      <th>Precio</th>\n",
       "      <th>Duración</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Visita guiada por Lisboa con entradas</td>\n",
       "      <td>Visitas Guiadas</td>\n",
       "      <td>Recorrido guiado por Lisboa con entradas y tra...</td>\n",
       "      <td>39.95</td>\n",
       "      <td>4 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Recorrido de un día a  Óbidos y Fátima</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Excursión de un día a Fátima y a las ciudades ...</td>\n",
       "      <td>73.20</td>\n",
       "      <td>10 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Excursión a Sintra, Cascais + Quinta da Regaleira</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Explore Sintra  y descubra Palacios espectacul...</td>\n",
       "      <td>94.15</td>\n",
       "      <td>9 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Lisbon City Card</td>\n",
       "      <td>Pases turísticos</td>\n",
       "      <td>Esta tarjeta ofrece pases y entradas de 24, 4...</td>\n",
       "      <td>20.00</td>\n",
       "      <td>De 1 a 3 días</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Tour por Sintra, Cabo da Roca, Cascais y Estoril</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Excursión a Sintra en Portugal... Más información</td>\n",
       "      <td>61.45</td>\n",
       "      <td>5 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Lisboa por la noche con cena y show de fado in...</td>\n",
       "      <td>Espectáculos</td>\n",
       "      <td>Después de cenar una cena tipica portuguesa en...</td>\n",
       "      <td>89.20</td>\n",
       "      <td>3 horas 30 minutos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Tour a pie por los barrios de Alfama, Chiado y...</td>\n",
       "      <td>Visitas Guiadas</td>\n",
       "      <td>Un tour a pie que le permitirá conocer las his...</td>\n",
       "      <td>58.00</td>\n",
       "      <td>3 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Recorrido en autobús con paradas libres por Li...</td>\n",
       "      <td>Tours en Bus turístico</td>\n",
       "      <td>Explore Lisboa  a su ritmo en este recorrido t...</td>\n",
       "      <td>27.75</td>\n",
       "      <td>flexible</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Tour de medio día a Fatima</td>\n",
       "      <td>Tours a pie</td>\n",
       "      <td>Este tour a Fatima de medio dia le lleva a con...</td>\n",
       "      <td>52.30</td>\n",
       "      <td>5 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Excursión por el Sendero Templario  y Tomar</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Esta excursión le lleva por  los lugares en lo...</td>\n",
       "      <td>85.00</td>\n",
       "      <td>9 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Recorrido guiado por Sintra, Cascais y el Pala...</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Visite Sintra y su Palacio da Pena de cuento d...</td>\n",
       "      <td>80.90</td>\n",
       "      <td>9 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Traslados privados desde el Aeropuerto a Lisboa</td>\n",
       "      <td>Traslados Aeropuertos</td>\n",
       "      <td>Traslados desde el Aeropuerto al centro o vice...</td>\n",
       "      <td>34.00</td>\n",
       "      <td>15 minutos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Espectáculo de fado en Lisboa: ‘Fado in Chiado’</td>\n",
       "      <td>Espectáculos</td>\n",
       "      <td>Fado en Chiado es un espectáculo de fado en di...</td>\n",
       "      <td>20.80</td>\n",
       "      <td>60 minutos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Excursión de un día a Évora</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Excursión guiada en minibús a una de las princ...</td>\n",
       "      <td>78.95</td>\n",
       "      <td>9 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Paseo turístico en barco con paradas libres po...</td>\n",
       "      <td>Paseos en barco</td>\n",
       "      <td>Paseo turístico en barco con paradas libres po...</td>\n",
       "      <td>27.75</td>\n",
       "      <td>flexible</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Paseo en barco por Lisboa con avistamiento de ...</td>\n",
       "      <td>Paseos en barco</td>\n",
       "      <td>Embarque en Lisboa en un RIB (Barco semirrígid...</td>\n",
       "      <td>64.45</td>\n",
       "      <td>3 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Tour en Tuk Tuk por Lisboa</td>\n",
       "      <td>Visitas Guiadas</td>\n",
       "      <td>Disfrute de lo mejor de dos grandes colinas de...</td>\n",
       "      <td>76.95</td>\n",
       "      <td>Flexible</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Tour guiado por Belém en segway</td>\n",
       "      <td>Visitas Guiadas</td>\n",
       "      <td>Únase a nosotros en un paseo impresionante en ...</td>\n",
       "      <td>88.20</td>\n",
       "      <td>2 horas 30 minutos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Hard Rock Cafe Lisboa</td>\n",
       "      <td>Experiencias Gastronómicas</td>\n",
       "      <td>Hard Rock Cafe  es el mejor descubrimiento de ...</td>\n",
       "      <td>27.20</td>\n",
       "      <td>2 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Excursión en bicicleta eléctrica a las colinas...</td>\n",
       "      <td>Tours en Bicicleta</td>\n",
       "      <td>Dice la leyenda que Lisboa fue construida sobr...</td>\n",
       "      <td>33.70</td>\n",
       "      <td>2 horas 30 minutos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Tour por Lisboa en Segway</td>\n",
       "      <td>Visitas Guiadas</td>\n",
       "      <td>Los segways son vehículos futuristas de auto-e...</td>\n",
       "      <td>43.60</td>\n",
       "      <td>1 hora 30 minutos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Arrabida  y Sesimbra Tour enológico para grupo...</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Disfrute de una escapada de un día para grupos...</td>\n",
       "      <td>85.00</td>\n",
       "      <td>8 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Tour privado de vinos y tapas por Lisboa</td>\n",
       "      <td>Experiencias Gastronómicas</td>\n",
       "      <td>En este tour privado de 2 horas, hemos combina...</td>\n",
       "      <td>82.00</td>\n",
       "      <td>2 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Excursión de GoCar guiado por GPS por Lisboa</td>\n",
       "      <td>Alquiler de Vehículos</td>\n",
       "      <td>El GoCar, es muy  fácil y divertido de conduci...</td>\n",
       "      <td>22.50</td>\n",
       "      <td>De 1 a 7 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Visita turística de 1’5 horas en el Bús anfibi...</td>\n",
       "      <td>Tours en Bus turístico</td>\n",
       "      <td>A bordo de nuestro vehículo anfibio, podra adm...</td>\n",
       "      <td>30.00</td>\n",
       "      <td>1 hora 30 minutos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Arrábida Dolphins y Jeep Safari</td>\n",
       "      <td>Paseos en barco</td>\n",
       "      <td>Impresionante safari en jeep por las montañas ...</td>\n",
       "      <td>95.00</td>\n",
       "      <td>8 horas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Tres ciudades en un día: Oporto, Nazaré y Óbid...</td>\n",
       "      <td>Excursiones de un día</td>\n",
       "      <td>Tres ciudades en un día: Oporto, Nazaré y Óbid...</td>\n",
       "      <td>104.60</td>\n",
       "      <td>12 horas</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                          Excursiones  \\\n",
       "0               Visita guiada por Lisboa con entradas   \n",
       "1              Recorrido de un día a  Óbidos y Fátima   \n",
       "2   Excursión a Sintra, Cascais + Quinta da Regaleira   \n",
       "3                                    Lisbon City Card   \n",
       "4    Tour por Sintra, Cabo da Roca, Cascais y Estoril   \n",
       "5   Lisboa por la noche con cena y show de fado in...   \n",
       "6   Tour a pie por los barrios de Alfama, Chiado y...   \n",
       "7   Recorrido en autobús con paradas libres por Li...   \n",
       "8                          Tour de medio día a Fatima   \n",
       "9         Excursión por el Sendero Templario  y Tomar   \n",
       "10  Recorrido guiado por Sintra, Cascais y el Pala...   \n",
       "11    Traslados privados desde el Aeropuerto a Lisboa   \n",
       "12    Espectáculo de fado en Lisboa: ‘Fado in Chiado’   \n",
       "13                        Excursión de un día a Évora   \n",
       "14  Paseo turístico en barco con paradas libres po...   \n",
       "15  Paseo en barco por Lisboa con avistamiento de ...   \n",
       "16                         Tour en Tuk Tuk por Lisboa   \n",
       "17                    Tour guiado por Belém en segway   \n",
       "18                              Hard Rock Cafe Lisboa   \n",
       "19  Excursión en bicicleta eléctrica a las colinas...   \n",
       "20                          Tour por Lisboa en Segway   \n",
       "21  Arrabida  y Sesimbra Tour enológico para grupo...   \n",
       "22           Tour privado de vinos y tapas por Lisboa   \n",
       "23       Excursión de GoCar guiado por GPS por Lisboa   \n",
       "24  Visita turística de 1’5 horas en el Bús anfibi...   \n",
       "25                    Arrábida Dolphins y Jeep Safari   \n",
       "26  Tres ciudades en un día: Oporto, Nazaré y Óbid...   \n",
       "\n",
       "             Tipo de excursión  \\\n",
       "0              Visitas Guiadas   \n",
       "1        Excursiones de un día   \n",
       "2        Excursiones de un día   \n",
       "3             Pases turísticos   \n",
       "4        Excursiones de un día   \n",
       "5                 Espectáculos   \n",
       "6              Visitas Guiadas   \n",
       "7       Tours en Bus turístico   \n",
       "8                  Tours a pie   \n",
       "9        Excursiones de un día   \n",
       "10       Excursiones de un día   \n",
       "11       Traslados Aeropuertos   \n",
       "12                Espectáculos   \n",
       "13       Excursiones de un día   \n",
       "14             Paseos en barco   \n",
       "15             Paseos en barco   \n",
       "16             Visitas Guiadas   \n",
       "17             Visitas Guiadas   \n",
       "18  Experiencias Gastronómicas   \n",
       "19          Tours en Bicicleta   \n",
       "20             Visitas Guiadas   \n",
       "21       Excursiones de un día   \n",
       "22  Experiencias Gastronómicas   \n",
       "23       Alquiler de Vehículos   \n",
       "24      Tours en Bus turístico   \n",
       "25             Paseos en barco   \n",
       "26       Excursiones de un día   \n",
       "\n",
       "                                          Descripción  Precio  \\\n",
       "0   Recorrido guiado por Lisboa con entradas y tra...   39.95   \n",
       "1   Excursión de un día a Fátima y a las ciudades ...   73.20   \n",
       "2   Explore Sintra  y descubra Palacios espectacul...   94.15   \n",
       "3    Esta tarjeta ofrece pases y entradas de 24, 4...   20.00   \n",
       "4   Excursión a Sintra en Portugal... Más información   61.45   \n",
       "5   Después de cenar una cena tipica portuguesa en...   89.20   \n",
       "6   Un tour a pie que le permitirá conocer las his...   58.00   \n",
       "7   Explore Lisboa  a su ritmo en este recorrido t...   27.75   \n",
       "8   Este tour a Fatima de medio dia le lleva a con...   52.30   \n",
       "9   Esta excursión le lleva por  los lugares en lo...   85.00   \n",
       "10  Visite Sintra y su Palacio da Pena de cuento d...   80.90   \n",
       "11  Traslados desde el Aeropuerto al centro o vice...   34.00   \n",
       "12  Fado en Chiado es un espectáculo de fado en di...   20.80   \n",
       "13  Excursión guiada en minibús a una de las princ...   78.95   \n",
       "14  Paseo turístico en barco con paradas libres po...   27.75   \n",
       "15  Embarque en Lisboa en un RIB (Barco semirrígid...   64.45   \n",
       "16  Disfrute de lo mejor de dos grandes colinas de...   76.95   \n",
       "17  Únase a nosotros en un paseo impresionante en ...   88.20   \n",
       "18  Hard Rock Cafe  es el mejor descubrimiento de ...   27.20   \n",
       "19  Dice la leyenda que Lisboa fue construida sobr...   33.70   \n",
       "20  Los segways son vehículos futuristas de auto-e...   43.60   \n",
       "21  Disfrute de una escapada de un día para grupos...   85.00   \n",
       "22  En este tour privado de 2 horas, hemos combina...   82.00   \n",
       "23  El GoCar, es muy  fácil y divertido de conduci...   22.50   \n",
       "24  A bordo de nuestro vehículo anfibio, podra adm...   30.00   \n",
       "25  Impresionante safari en jeep por las montañas ...   95.00   \n",
       "26  Tres ciudades en un día: Oporto, Nazaré y Óbid...  104.60   \n",
       "\n",
       "              Duración  \n",
       "0              4 horas  \n",
       "1             10 horas  \n",
       "2              9 horas  \n",
       "3        De 1 a 3 días  \n",
       "4              5 horas  \n",
       "5   3 horas 30 minutos  \n",
       "6              3 horas  \n",
       "7             flexible  \n",
       "8              5 horas  \n",
       "9              9 horas  \n",
       "10             9 horas  \n",
       "11          15 minutos  \n",
       "12          60 minutos  \n",
       "13             9 horas  \n",
       "14            flexible  \n",
       "15             3 horas  \n",
       "16            Flexible  \n",
       "17  2 horas 30 minutos  \n",
       "18             2 horas  \n",
       "19  2 horas 30 minutos  \n",
       "20   1 hora 30 minutos  \n",
       "21             8 horas  \n",
       "22             2 horas  \n",
       "23      De 1 a 7 horas  \n",
       "24   1 hora 30 minutos  \n",
       "25             8 horas  \n",
       "26            12 horas  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_lisboa"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "--- \n",
    "*Visualización"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Vuelos para Florencia y Lisboa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "cantidad_vuelos = df_vuelos_florencia['Aerolínea'].value_counts()\n",
    "aerolineas = df_vuelos_florencia['Aerolínea'].unique()\n",
    "colores1 = [\"c\", \"cadetblue\", \"mediumseagreen\"]\n",
    "colores2 = [\"darkorange\", \"g\", 'teal']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Proporción de aerolíneas ruta MAD-FLR')"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAccAAAGcCAYAAACstWuGAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABYWElEQVR4nO3dd3gU1f4G8Hd3k03vPSEklJBQQk0QEAw9gOBV4Ee/gDSviIANsYEFrg1sKIqXUIQAAiKiAgoKKEiRqrQA6Y30XrfM74+Qld0kZBOSzJb38zx5IDOzs99Zln33nDlzRiIIggAiIiLSkIpdABERkaFhOBIREelgOBIREelgOBIREelgOBIREelgOBIREelgOBIREelgOBIREelgOJqRPXv2YNWqVVCpVGKXYvLWr1+PdevWiV0GETUSw9FEzJw5E4GBgXWu/+OPPzB16lR06tQJMpms2es5evQoJBIJjh492uzPJZaEhARIJBJs2rRJa/nPP/+M//znPwgODhanMCK6byYVjps2bYJEItH8WFtbo0OHDliwYAEyMjLELk80OTk5mDRpEj755BOMGjVK7HJMWklJCebNm4c33ngDAwcOFLscUW3btg0fffRRk+934MCBkEgkCAoKqnX9oUOHNJ8Bu3fvrnWbtWvXQiKR4IEHHqjzee7+LLGwsICrqyt69eqFRYsW4erVq3rXW/1FsbafSZMmaR1Xly5d7rmv119/XevxlpaWCAwMxMKFC5Gfn693TVQ/C7ELaA5vvvkm2rRpg/Lychw/fhyff/459u/fj8uXL8PW1lbs8prF//73P6jV6lrXXbhwAStWrMD06dNbuCrz8/LLL6Njx454+eWXxS5FdNu2bcPly5exePHiJt+3tbU1bt26hTNnzqB3795a66Kjo2FtbY3y8vI6Hx8dHY3AwECcOXMGt27dQvv27WvdbtiwYZg+fToEQUBBQQEuXbqEzZs3Y+3atXj33Xfx7LPP6l3zwoULER4errXsXr099/L555/D3t4eJSUl+OWXX7BmzRqcP38ex48fb9T+qBaCCdm4caMAQPjzzz+1lj/77LMCAGHbtm11Pra4uLi5y2swQ6xJX0eOHBEACEeOHBG7FL2p1WqhtLRU7+3j4+MFAMLGjRubrygDoVAohIqKigY95uGHHxYCAgKavJaIiAihc+fOQnBwsLB48WKt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+OILdOrUSStsIyIi8MQTT+Dtt9/GxYsXMXz4cFhaWuLmzZvYtWsXPv74Y63BQ7VZunQptm/fjpEjR2LhwoVwdXXF5s2bER8fj2+++abZuq3eeecdHDlyBA888ADmzp2LTp06ITc3F+fPn8fhw4eRm5vboNdizpw5yM3NxeDBg9GqVSskJiZizZo16N69u+b8aUN17twZffr0wUsvvYTc3Fy4urpix44dUCqVNbbt1asXvv76azz77LMIDw+Hvb09xowZo3f9+nJycsLrr79+z2327duHoqIiPPLII7Wu79OnDzw8PBAdHY2JEydqlt+4cQNbt26FIAgoLCzEpUuXsGvXLhQXF+ODDz7Q+/ytvrKysrBixYoay9u0aaO5Frs2lpaWWLRoEV544QUcPHiwyesyS+IMkm0edc2Qo2vGjBmCnZ1dreuKioqEZ555RvD19RUsLS2FoKAg4f3339e6/EAQ/hnmvXXrViEoKEiwsrISevToUeuMMOfPnxciIyMFe3t7wdbWVhg0aJDwxx9/NKj2ffv2Cf369RNsbGwER0dHoXfv3sL27du1jkl32HxDj0VXQECAMGPGjFrruVtiYqLwyCOPCLa2toK7u7uwaNEizaUTuq/HhQsXhLFjxwpubm6ClZWVEBAQIEyYMEH45Zdf7vkcarVa+O9//ysEBARoXusffvih1uMWBEH48ssvhV69egk2NjaCg4ODEBoaKixZskRIS0vTOr6HH3641ueLjY0Vxo8fLzg7OwvW1tZC7969hR9++EFrm4ZcyqHv65uRkSE89dRTgr+/v2BpaSl4e3sLQ4YMEb788ssGvxa7d+8Whg8fLnh6egpyuVxo3bq18MQTTwjp6em1HrPucb3//vt1vjZDhw4VrKysBC8vL+Hll18WDh06VOPfu7i4WJgyZYrg7OwsANDU1tB/S136XPKgeynHmDFjBGtr63te6jBz5kzB0tJScykN7rrkQiqVCs7OzkKPHj2ERYsWCVeuXKm3zrpquddxoY5LPoYMGSIIQt0z5AiCIBQUFAhOTk5CRESE3rVR3SSC0EQjLsyMRCLBU089VaPbkoiIjB/PORIREelgOBIREelgOBIREengaNVG4qlaIiLTxZYjERGRDoYjERGRDoYjERGRDoYjERGRDoYjERGRDoYjERGRDoYjERGRDoYjERGRDoYjERGRDoYj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gKVhw4YhODgYI0aMwOjRozF8+PBGvXbUcAxHMlkudnYIt7NDeGDVN26VWo3ckhLklJQgp7gEOcXF//z9zvJKAxn0I7ewgLu93T8B6OICf1cXuN8592Zurl69ilOnTuHMmTNag3BUKhV27NiBuXPn1vq4n376CampqTUG4KhUKvzyyy8YNmxYnc9pZ2en9XtoaChcXV1x7NgxHDt2DCtXroS3tzfeffdd/Pnnn1AoFOjXrx+AqvOWo0ePxpNPPomVK1fC1dUVx48fx+zZs1FZWanpep0zZw4+++wzLF26FBs3bsTjjz+u6f7u2bMn4uPjceDAARw+fBgTJkzA0KFDa5ynpObBcCSzIZNK4eHgAI86WhkAUFRergnL3JISZN8J0KKycqjUaqgENZRqddXf1cKdP7V/lELVuuqrpGQSCWzkctjW8mNvbQVnGxs42djA2bbqTydbW7NoCTZEVFQUHnroIXz22Wdayzdu3IioqKg6wzEqKgqTJk3CK6+8orV85cqViIqKumc46pJIJBgwYAC+++47XLlyBf3794etrS0qKiqwbt06hIWFaQL13LlzUKvVWL16taZ1unPnzhr7nDZtGpYsWYJPPvkEV69exYwZM7TWOzo6YuLEiZg4cSLGjx+PESNGIDc3F66urnrXTY3DcCS6i4O1NRysrZvkAni1IECtVsNCJmuCysyXQqHAli1b8Oabb6JLly5a6+bMmYMPPvgAV65c0ZyLrJaVlYXvv/8e+/btq/G46dOn47HHHmtw0AwcOBDPPfccwsLCNCNoH3roIURHR+OFF17QbNe+fXsoFAqsWbMGY8aMwYkTJ/DFF1/U2J+LiwvGjh2LF154AcOHD0erVq006z744AP4+PigR48ekEql2LVrF7y9veHs7Kx3vdR44o/hJjJRUomEwdgE9u3bh5ycHDz22GM11nXs2BEdO3as9fKMr776CnZ2dhgyZEiNdUOGDIGNjQ22bt3aoFoiIiKgUqkwcOBAzbKBAwfWWNatWzd88MEHePfdd9GlSxdER0fXeRlGdVfrrFmztJY7ODjgvffeQ1hYGMLDw5GQkID9+/cbxKU35oAz5BARiWjLli145plnkJaWBjnnsDUY7FYlIhJBaWkp0tPT8c477+CJJ55gMBoYts+JiETw3nvvISQkBN7e3njppZfELod0sFuViIhIB1uOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOhiOREREOv4fSG0z/4jtsz4AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie(cantidad_vuelos, labels=aerolineas, data=df_vuelos_florencia, autopct='%1.1f%%', colors=colores1)\n",
    "plt.title('Proporción de aerolíneas ruta MAD-FLR')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En esta visualización se puede observa la distribución de los vuelos en la RUTA MAD-FLR. Alto dominio de Vueling Airlines."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "cantidad_vuelos_lis = df_vuelos_lisboa['Aerolínea'].value_counts()\n",
    "aerolineas_lis = df_vuelos_lisboa['Aerolínea'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Proporción de vuelos MAD-LIS')"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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5a7BWVlZzJgxw+pxcXFx+Pv78/rrrxc733+tPIVvyh988IHV7e+99x4AvXr1AuDMmTNF/o0KR0k3OoU0YMAAXnzxRaZNm1bivvvnz5/nxx9/pHfv3gwYMKDI19ixY8nMzGTevHnXXd/p06cZNGgQ+fn5vPDCC5bbu3TpYvV19cjhRq1bt46srKwit69fv55Tp04VO/UqLpORgo316dOHjh078sILL3D48GGaNGnC4sWL+fnnnxk/frzVhljQ5/nj4uJ47LHH8PDwYNq0aQBW+9O/+uqrLFmyhLZt2zJmzBhcXV359NNPuXDhAm+99dZ1M/n7+/P+++8zatQomjdvzuDBg6lQoQLbtm0jOzu7yJvdzb6WmzV69Gg++ugjhg0bxqZNmwgPD2fmzJlFjhx3cXHhiy++oEePHjRo0ICRI0dSpUoV/vnnH5YtW4a/vz/z58+/7vruvfdehg4dyrRp04iLi7MaDYBeohERETzwwAM8/fTTmM1mvvrqK0JCQkhKSrI8zt/fn48//pj77ruP22+/nYEDB1oe8+uvv9KmTZsihVqoSZMmDB8+nM8++4z09HRiY2NZv349M2bMID4+3rKBt/Co4L59+1KrVi0yMzP5/PPP8ff3v+GDwQICAnjppZeu+Zh58+aRmZnJnXfeWez9LVu2JCQkhISEBKuN8/v27eObb75B0zQyMjLYtm0b3333HefOneO9996je/fupc75ww8/WEajVxo+fHixo+KZM2eSkJBA3759adasGe7u7vz111989dVXeHp68vzzz5d63U5J3Y5PjqFwt8Pr7QI4fPhwzcfHp9j7MjMztccff1yrXLmy5ubmpkVFRWlvv/221W6UmnZ517pvvvlGi4qK0jw8PLSmTZtadsG80ubNm7W4uDjN19dX8/b21jp27KitXr36hrLPmzdPa926tebl5aX5+/trMTEx2rfffmv1mq7cJfVmXsvVIiMjteHDhxeb50pHjhzR7rzzTs3b21sLDg7Wxo0bpy1cuNBql9RCW7Zs0fr166cFBQVpHh4eWmRkpHbPPfdoS5cuve56NE3TMjIyNC8vLw3Qvvnmm2Ifs2nTJq1Fixaau7u7FhERob333ntFdkkttGzZMi0uLk4LCAjQPD09tVq1amkjRoyw2tW4uN1cc3NztZdfflmrUaOG5ubmplWrVk177rnntJycHMtj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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie(cantidad_vuelos_lis, labels=aerolineas_lis, data=df_vuelos_lisboa, autopct='%1.1f%%', colors=colores2)\n",
    "plt.title('Proporción de vuelos MAD-LIS')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Aquí se puede visualizar la distribución de las aerolíneas para la ruta MAD-LIS."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\3879771835.py:1: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x = \"Aerolínea\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Costo promedio por aerolínea MAD-FLR')"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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z0WLFi2EUqkUtWrVEu3atROBgYFajzkDEP7+/sVuryzHqjyPnhf3CHZx36P4+HgxcuRIoVarhaGhoahfv77o3bu32L59e4WORXHK8oj2s+eps7OzaNiwYanLeHh4CCsrK5Gbmyvtd+FgYGAgLC0thaurqwgICCjyc1ieWkrbL5TwiLqfn58Q4v8/el6c+Ph4oa+vL3x9fctcG1U+hRClfOIWEUmOHz+ON998E5GRkRgwYICuy3nlFXYe/eKLLzB9+nRdl0NEMsY+O0RERCRrDDtEREQkaww7REREJGvss0NERESyxis7REREJGsMO0RERCRr/FBBPH1/zL1792Bubs630xIREb0ihBDIyMhAvXr1irxg+Z8YdgDcu3evSt5LQ0RERFXv7t27aNCgQYnzGXYA6SP67969WyXvpyEiIqLKl56eDltb2+e+aodhB5BuXalUKoYdIiKiV8zzuqCwgzIRERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGt96TpVCCIGsrCxp3NTU9LlvoSUiInoZGHaoUmRlZaFv377S+O7du2FmZqbDioiIiJ7ibSwiIiKSNYYdIiIikjWGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpK1ahN2PvvsMygUCkyZMkWa9uTJE/j7+6N27dowMzODj48PkpKStJa7c+cOvL29YWJiAisrK8yYMQN5eXkvuXoiIiKqrqpF2Dl79iw2bNiAVq1aaU2fOnUq9uzZg8jISERFReHevXvo37+/ND8/Px/e3t7IycnBqVOnsHHjRoSFhWHevHkvexeIiIiomtJ52MnMzMSwYcPw9ddfo1atWtL0tLQ0hISEYMWKFejatSvatWuH0NBQnDp1CqdPnwYAHDx4ENeuXcP333+PNm3aoGfPnli0aBGCg4ORk5Ojq10iIiKiakTnYcff3x/e3t7w9PTUmh4TE4Pc3Fyt6c2bN0fDhg0RHR0NAIiOjoazszOsra2lNl5eXkhPT8fVq1dL3GZ2djbS09O1BiIiIpInnb71fMuWLTh//jzOnj1bZF5iYiKMjIxQs2ZNrenW1tZITEyU2vwz6BTOL5xXkqVLlyIwMPAFqyciIqJXgc6u7Ny9exeTJ09GeHg4jI2NX+q2AwICkJaWJg137959qdsnIiKil0dnYScmJgbJyclo27YtDAwMYGBggKioKKxevRoGBgawtrZGTk4OUlNTtZZLSkqCWq0GAKjV6iJPZxWOF7YpjlKphEql0hqIiIhInnQWdrp164bLly/jwoUL0uDi4oJhw4ZJXxsaGuLIkSPSMrGxsbhz5w40Gg0AQKPR4PLly0hOTpbaHDp0CCqVCk5OTi99n4iIiKj60VmfHXNzc7Rs2VJrmqmpKWrXri1N9/Pzw7Rp02BpaQmVSoVJkyZBo9GgQ4cOAIDu3bvDyckJI0aMwLJly5CYmIg5c+bA398fSqXype8TERERVT867aD8PCtXroSenh58fHyQnZ0NLy8vrF27Vpqvr6+PvXv3YsKECdBoNDA1NYWvry8WLlyow6qJiIioOlEIIYSui9C19PR0WFhYIC0tjf13KigzMxN9+/aVxnfv3g0zMzMdVkRERHJX1r/fOv+cHSIiIqKqxLBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLJWrV8X8Sqx2bJF1yXolF52Npr/Y7zZjh0o+Be/nyxh8GBdl0BERP+HV3aIiIhI1hh2iIiISNYYdoiIiEjWGHaIiIhI1hh2iIiISNYYdoiIiEjWGHaIiIhI1hh2iIiISNYYdoiIiEjWGHaIiIhI1hh2iIiISNYYdoiIiEjWGHaIiIhI1hh2iIiISNYYdoiIiEjWGHaIiIhI1hh2iIiISNYYdoiIiEjWGHaIiIhI1hh2iIiISNYYdoiIiEjWdBp21q1bh1atWkGlUkGlUkGj0eC///2vNN/DwwMKhUJrGD9+vNY67ty5A29vb5iYmMDKygozZsxAXl7ey94VIiIiqqYMdLnxBg0a4LPPPsNrr70GIQQ2btyIvn374rfffkOLFi0AAGPHjsXChQulZUxMTKSv8/Pz4e3tDbVajVOnTiEhIQEjR46EoaEhPv3005e+P0RERFT96DTs9OnTR2t8yZIlWLduHU6fPi2FHRMTE6jV6mKXP3jwIK5du4bDhw/D2toabdq0waJFizBr1iwsWLAARkZGVb4PREREVL1Vmz47+fn52LJlC7KysqDRaKTp4eHhqFOnDlq2bImAgAA8evRImhcdHQ1nZ2dYW1tL07y8vJCeno6rV6+WuK3s7Gykp6drDURERCRPOr2yAwCXL1+GRqPBkydPYGZmhp07d8LJyQkAMHToUNjZ2aFevXq4dOkSZs2ahdjYWPzwww8AgMTERK2gA0AaT0xMLHGbS5cuRWBgYBXtEREREVUnOg87zZo1w4ULF5CWlobt27fD19cXUVFRcHJywrhx46R2zs7OsLGxQbdu3RAfHw97e/sKbzMgIADTpk2TxtPT02Fra/tC+0FERETVk85vYxkZGcHBwQHt2rXD0qVL0bp1a6xatarYtq6urgCAuLg4AIBarUZSUpJWm8Lxkvr5AIBSqZSeACsciIiISJ50HnaeVVBQgOzs7GLnXbhwAQBgY2MDANBoNLh8+TKSk5OlNocOHYJKpZJuhREREdG/m05vYwUEBKBnz55o2LAhMjIyEBERgePHj+PAgQOIj49HREQEevXqhdq1a+PSpUuYOnUqunTpglatWgEAunfvDicnJ4wYMQLLli1DYmIi5syZA39/fyiVSl3uGhEREVUTOg07ycnJGDlyJBISEmBhYYFWrVrhwIEDeOutt3D37l0cPnwYQUFByMrKgq2tLXx8fDBnzhxpeX19fezduxcTJkyARqOBqakpfH19tT6Xh4iIiP7dFEIIoesidC09PR0WFhZIS0urcP8dmy1bKrmqV4wQ0MvJkUYLjIwAhUKHBelWwuDBui6BiEj2yvr3W+dPY5FMKBQo4K1DIiKqhqpdB2UiIiKiysSwQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxheBEpFsCSGQlZUljZuamkKhUOiwIiLSBYYdIpKtrKws9O3bVxrfvXs3zMzMdFgREekCb2MRERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrBnougAiqjrj123QdQk6lZ+TozU+NSQU+kZGOqpG99ZPeF/XJRDphE6v7Kxbtw6tWrWCSqWCSqWCRqPBf//7X2n+kydP4O/vj9q1a8PMzAw+Pj5ISkrSWsedO3fg7e0NExMTWFlZYcaMGcjLy3vZu0JERETVlE7DToMGDfDZZ58hJiYG586dQ9euXdG3b19cvXoVADB16lTs2bMHkZGRiIqKwr1799C/f39p+fz8fHh7eyMnJwenTp3Cxo0bERYWhnnz5ulql4iIiKia0eltrD59+miNL1myBOvWrcPp06fRoEEDhISEICIiAl27dgUAhIaGwtHREadPn0aHDh1w8OBBXLt2DYcPH4a1tTXatGmDRYsWYdasWViwYAGMSrhcnZ2djezsbGk8PT296naSiIiIdKradFDOz8/Hli1bkJWVBY1Gg5iYGOTm5sLT01Nq07x5czRs2BDR0dEAgOjoaDg7O8Pa2lpq4+XlhfT0dOnqUHGWLl0KCwsLabC1ta26HSMiIiKd0nnYuXz5MszMzKBUKjF+/Hjs3LkTTk5OSExMhJGREWrWrKnV3traGomJiQCAxMREraBTOL9wXkkCAgKQlpYmDXfv3q3cnSIiIqJqQ+dPYzVr1gwXLlxAWloatm/fDl9fX0RFRVXpNpVKJZRKZZVug4iIiKoHnYcdIyMjODg4AADatWuHs2fPYtWqVRg0aBBycnKQmpqqdXUnKSkJarUaAKBWq/Hrr79qra/waa3CNkRERPTvpvPbWM8qKChAdnY22rVrB0NDQxw5ckSaFxsbizt37kCj0QAANBoNLl++jOTkZKnNoUOHoFKp4OTk9NJrJyIioupHp1d2AgIC0LNnTzRs2BAZGRmIiIjA8ePHceDAAVhYWMDPzw/Tpk2DpaUlVCoVJk2aBI1Ggw4dOgAAunfvDicnJ4wYMQLLli1DYmIi5syZA39/f96mIiKqhnqHT9d1CVSN7B325UvZjk7DTnJyMkaOHImEhARYWFigVatWOHDgAN566y0AwMqVK6GnpwcfHx9kZ2fDy8sLa9eulZbX19fH3r17MWHCBGg0GpiamsLX1xcLFy7U1S4RERFRNaPTsBMSElLqfGNjYwQHByM4OLjENnZ2dti3b19ll0ZEREQyUe367BARERFVJoYdIiIikjWGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpI1nb8ugoioqugZGqLJ2/20xono34dhh4hkS6FQQN/ISNdlEJGO8TYWERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREckaww4RERHJGsMOERERyRrDDhEREcmaTsPO0qVL0b59e5ibm8PKygr9+vVDbGysVhsPDw8oFAqtYfz48Vpt7ty5A29vb5iYmMDKygozZsxAXl7ey9wVIiIiqqYMdLnxqKgo+Pv7o3379sjLy8Ps2bPRvXt3XLt2DaamplK7sWPHYuHChdK4iYmJ9HV+fj68vb2hVqtx6tQpJCQkYOTIkTA0NMSnn376UveHiIiIqh+dhp39+/drjYeFhcHKygoxMTHo0qWLNN3ExARqtbrYdRw8eBDXrl3D4cOHYW1tjTZt2mDRokWYNWsWFixYACMjoyrdByIiIqreqlWfnbS0NACApaWl1vTw8HDUqVMHLVu2REBAAB49eiTNi46OhrOzM6ytraVpXl5eSE9Px9WrV4vdTnZ2NtLT07UGIiIikiedXtn5p4KCAkyZMgVubm5o2bKlNH3o0KGws7NDvXr1cOnSJcyaNQuxsbH44YcfAACJiYlaQQeANJ6YmFjstpYuXYrAwMAq2hMiIiKqTqpN2PH398eVK1fw888/a00fN26c9LWzszNsbGzQrVs3xMfHw97evkLbCggIwLRp06Tx9PR02NraVqxwIiIiqtaqxW2siRMnYu/evTh27BgaNGhQaltXV1cAQFxcHABArVYjKSlJq03heEn9fJRKJVQqldZARERE8qTTsCOEwMSJE7Fz504cPXoUjRs3fu4yFy5cAADY2NgAADQaDS5fvozk5GSpzaFDh6BSqeDk5FQldRMREdGrQ6e3sfz9/REREYHdu3fD3Nxc6mNjYWGBGjVqID4+HhEREejVqxdq166NS5cuYerUqejSpQtatWoFAOjevTucnJwwYsQILFu2DImJiZgzZw78/f2hVCp1uXtERERUDej0ys66deuQlpYGDw8P2NjYSMPWrVsBAEZGRjh8+DC6d++O5s2b46OPPoKPjw/27NkjrUNfXx979+6Fvr4+NBoNhg8fjpEjR2p9Lg8RERH9e+n0yo4QotT5tra2iIqKeu567OzssG/fvsoqi4iIiGSkWnRQJiIiIqoqDDtEREQkaww7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0eltrMzMTOkqDQDcvHkTFy5cgKWlJSwtLREYGAgfHx+o1WrEx8dj5syZcHBwgJeXFwDA0dERPXr0wNixY7F+/Xrk5uZi4sSJGDx4MJ/EIiIiIgA6vrJz7tw5vP7663j99dcBANOmTcPrr7+OefPmQV9fH5cuXcLbb7+Npk2bws/PD+3atcPJkyehVCqldYSHh6N58+bo1q0bevXqhU6dOuGrr77S1S4RERFRNaPTKzseHh4QQpQ4/8CBA89dh6WlJSIiIiqzLCIiIpKRV6rPDhEREVF5MewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGs6TTsnDhxAn369EG9evWgUCiwa9curflCCMybNw82NjaoUaMGPD09cePGDa02KSkpGDZsGFQqFWrWrAk/Pz9kZma+xL0gIiKi6kynYScrKwutW7dGcHBwsfOXLVuG1atXY/369Thz5gxMTU3h5eWFJ0+eSG2GDRuGq1ev4tChQ9i7dy9OnDiBcePGvaxdICIiomrOQJcb79mzJ3r27FnsPCEEgoKCMGfOHPTt2xcA8N1338Ha2hq7du3C4MGDcf36dezfvx9nz56Fi4sLAGDNmjXo1asXvvzyS9SrV++l7QsRERFVT9W2z87NmzeRmJgIT09PaZqFhQVcXV0RHR0NAIiOjkbNmjWloAMAnp6e0NPTw5kzZ0pcd3Z2NtLT07UGIiIikqdqG3YSExMBANbW1lrTra2tpXmJiYmwsrLSmm9gYABLS0upTXGWLl0KCwsLabC1ta3k6omIiKi6qLZhpyoFBAQgLS1NGu7evavrkoiIiKiKVNuwo1arAQBJSUla05OSkqR5arUaycnJWvPz8vKQkpIitSmOUqmESqXSGoiIiEieqm3Yady4MdRqNY4cOSJNS09Px5kzZ6DRaAAAGo0GqampiImJkdocPXoUBQUFcHV1fek1ExERUfWj06exMjMzERcXJ43fvHkTFy5cgKWlJRo2bIgpU6Zg8eLFeO2119C4cWPMnTsX9erVQ79+/QAAjo6O6NGjB8aOHYv169cjNzcXEydOxODBg/kkFhEREQHQcdg5d+4c3nzzTWl82rRpAABfX1+EhYVh5syZyMrKwrhx45CamopOnTph//79MDY2lpYJDw/HxIkT0a1bN+jp6cHHxwerV69+6ftCRERE1ZNOw46HhweEECXOVygUWLhwIRYuXFhiG0tLS0RERFRFeURERCQD1bbPDhEREVFlYNghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWWPYISIiIllj2CEiIiJZY9ghIiIiWavWYWfBggVQKBRaQ/PmzaX5T548gb+/P2rXrg0zMzP4+PggKSlJhxUTERFRdVOtww4AtGjRAgkJCdLw888/S/OmTp2KPXv2IDIyElFRUbh37x769++vw2qJiIioujHQdQHPY2BgALVaXWR6WloaQkJCEBERga5duwIAQkND4ejoiNOnT6NDhw4lrjM7OxvZ2dnSeHp6euUXTkRERNVCtb+yc+PGDdSrVw9NmjTBsGHDcOfOHQBATEwMcnNz4enpKbVt3rw5GjZsiOjo6FLXuXTpUlhYWEiDra1tle4DERER6U61Djuurq4ICwvD/v37sW7dOty8eROdO3dGRkYGEhMTYWRkhJo1a2otY21tjcTExFLXGxAQgLS0NGm4e/duFe4FERER6VK1vo3Vs2dP6etWrVrB1dUVdnZ22LZtG2rUqFHh9SqVSiiVysookYiIiKq5an1l51k1a9ZE06ZNERcXB7VajZycHKSmpmq1SUpKKraPDxEREf07vVJhJzMzE/Hx8bCxsUG7du1gaGiII0eOSPNjY2Nx584daDQaHVZJRERE1Um1vo01ffp09OnTB3Z2drh37x7mz58PfX19DBkyBBYWFvDz88O0adNgaWkJlUqFSZMmQaPRlPokFhEREf27VOuw89dff2HIkCF48OAB6tati06dOuH06dOoW7cuAGDlypXQ09ODj48PsrOz4eXlhbVr1+q4aiIiIqpOqnXY2bJlS6nzjY2NERwcjODg4JdUEREREb1qXqk+O0RERETlxbBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyJpuwExwcjEaNGsHY2Biurq749ddfdV0SERERVQOyCDtbt27FtGnTMH/+fJw/fx6tW7eGl5cXkpOTdV0aERER6Zgsws6KFSswduxYjB49Gk5OTli/fj1MTEzw7bff6ro0IiIi0jEDXRfwonJychATE4OAgABpmp6eHjw9PREdHV3sMtnZ2cjOzpbG09LSAADp6ekVrqPg0aMKL0vy8yLnUmXKefxY1yVQNVIdzsvcR9nPb0T/Gi96ThYuL4QovaF4xf39998CgDh16pTW9BkzZog33nij2GXmz58vAHDgwIEDBw4cZDDcvXu31Kzwyl/ZqYiAgABMmzZNGi8oKEBKSgpq164NhUKhw8pebenp6bC1tcXdu3ehUql0XQ4RAJ6XVP3wnKw8QghkZGSgXr16pbZ75cNOnTp1oK+vj6SkJK3pSUlJUKvVxS6jVCqhVCq1ptWsWbOqSvzXUalU/AGmaofnJVU3PCcrh4WFxXPbvPIdlI2MjNCuXTscOXJEmlZQUIAjR45Ao9HosDIiIiKqDl75KzsAMG3aNPj6+sLFxQVvvPEGgoKCkJWVhdGjR+u6NCIiItIxWYSdQYMG4f79+5g3bx4SExPRpk0b7N+/H9bW1rou7V9FqVRi/vz5RW4REukSz0uqbnhOvnwKIZ73vBYRERHRq+uV77NDREREVBqGHSIiIpI1hh0iIiKSNYadfwmFQoFdu3YBAG7dugWFQoELFy7otKZCHh4emDJlSqltnq35+PHjUCgUSE1NrfL66NXzz/Od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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = \"Aerolínea\", \n",
    "              y = 'Costo',\n",
    "              data = df_vuelos_florencia, \n",
    "              palette=colores1)\n",
    "plt.title('Costo promedio por aerolínea MAD-FLR')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tengo la media de las dos principales aerolíneas, pero Air Europa no cuenta como media porque solo aparece una vez dentro de un paquete. Esto nos destaca donde se encuentra la media de precio por cada aerolínea."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\157670056.py:1: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x = \"Aerolínea\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Costo promedio por aerolínea MAD-LIS')"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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8MEHio2NVYcOHfT666/r/PnzmjVrllq0aKHvvvvOsa9ffPGFevTooTp16ig+Pl6nT5/WwIEDdccdd1z3WOzbt0/33XefvL29NXbsWJUuXVpvv/22WrVqpQ0bNigyMvK663j//fd17tw5DRs2TBcvXtT06dPVpk0bff/996pcuXKBfm4PP/ywatasqVdffVXGmDy3/b///U/Lly/Xww8/rGrVqunEiRN6++231bJlS/3www8KDg6WdOXqzIMPPqivv/5aQ4cOVUREhL7//ntNnTpVP/30k5YvX+603rVr1+rDDz/U8OHD5e/vr7CwsEI5Vn+WkJCgc+fO6YknnpDNZtMbb7yh7t2763//+59Kly4t6crPqHnz5qpSpYr+7//+T2XLltWHH36omJgYffTRR3rooYdu6FhczyOPPKL27dsrKSlJ4eHhjjp79uzpqOnP0tPT9dFHH+kvf/mLpCu3qQYOHJjr7bBriYqKUnh4uFavXp3vZW5UaGio1qxZo7Vr16pNmza3bDsoBAa4xf744w8jyXTr1i1f/Xft2mUkmccff9ypfcyYMUaSWbt2rTHGmI8//thIMtu2bctzXadOnTKSzPjx43PMa9SokQkICDCnT592tO3evdu4ubmZ/v37X7PGdevWGUmmSpUqJiUlxdH+4YcfGklm+vTpjraWLVsaSWb27NlO65g2bZqRZP7973872jIyMkxUVJQpV66cY73JyclGkqlUqZI5e/aso29cXJyRZBo2bGguXbrkaO/bt6/x8PAwFy9eNMYYc+7cOePr62uGDBnitP3jx48bHx8fp/ZGjRqZoKAgp+188cUXRpIJDQ11Wv7PxzUmJsZ4eHiYpKQkR9uvv/5qypcvb+6///68D+ZV++jl5WV+/vlnR/vWrVuNJDNq1CinGvPzcxs/fryRZPr27XvNbWe7ePGiyczMzFGX3W43kyZNcrR98MEHxs3NzXz11VdOfWfPnm0kmU2bNjnaJBk3Nzezb98+p775PVbZ59m6descbbGxsU4/i+xjV7FiRXPmzBlH+4oVK4wk88knnzja2rZta+rXr+84N4wxJisryzRr1szUrFnzho9FXkJDQ03nzp3N5cuXTWBgoHnppZeMMcb88MMPRpLZsGGDmTt3bq7/f5cuXWokmYMHDxpjjElJSTGenp5m6tSpOeqRZCZPnpxnHd26dTOS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n7755hvFxcXp2LFjevPNN/NcV3x8vCZOnFgUZQMAABcrEWHn0qVL6tWrl4wxmjVrltO80aNHO/7doEEDeXh46IknnlB8fLzsdnuu64uLi3NaLiUlRSEhIbemeAAA4FLFPuxkB53Dhw9r7dq1Tld1chMZGanLly/r0KFDql27dq597HZ7nkEIAABYS7EOO9lB5+DBg1q3bp0qVqx43WV27dolNzc3BQQEFEGFAACguHNp2ElNTVViYqJjOjk5Wbt27ZKfn5+CgoLUs2dP7dy5U59++qkyMzN1/PhxSZKfn588PDy0efNmbd26Va1bt1b58uW1efNmjRo1So8++qgqVKjgqt0CAADFiEvDzvbt29W6dWvHdPY4mtjYWE2YMEH/+c9/JEmNGjVyWm7dunVq1aqV7Ha7Fi1apAkTJig9PV3VqlXTqFGjnMbjAACA25tLw06rVq1kjMlz/rXmSVKTJk20ZcuWwi4LAABYSIn6nB0AAIAbRdgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACW5tKws3HjRnXt2lXBwcGy2Wxavny503xjjF588UUFBQXJy8tL7dq108GDB536nDlzRv369ZO3t7d8fX01ePBgpaamFuFeAACA4sylYSctLU0NGzbUzJkzc53/xhtv6B//+Idmz56trVu3qmzZsurQoYMuXrzo6NOvXz/t27dPq1ev1qeffqqNGzdq6NChRbULAACgmCvlyo1HR0crOjo613nGGE2bNk0vvPCCunXrJkl6//33VblyZS1fvlx9+vTR/v37tWrVKm3btk1NmzaVJM2YMUOdOnXS3//+dwUHBxfZvgAAgOKp2I7ZSU5O1vHjx9WuXTtHm4+PjyIjI7V582ZJ0ubNm+Xr6+sIOpLUrl07ubm5aevWrXmuOz09XSkpKU4vAABg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UqVKTtOvvfaawsPD1bJlS0dbmTJlFBgYmO91pqenKz093TGdkpJy84UCAIBiqdjfxrpaRkaG/v3vf2vQoEGy2WyO9gULFsjf31/16tVTXFyczp8/f831xMfHy8fHx/EKCQm51aUDAAAXKfZXdq62fPlynT17VgMGDHC0PfLIIwoNDVVwcLD27Nmj5557TgcOHNCyZcvyXE9cXJxGjx7tmE5JSSHwAABgUSUq7MyZM0fR0dEKDg52tA0dOtTx7/r16ysoKEht27ZVUlKSwsPDc12P3W6X3W6/5fUCAADXKzG3sQ4fPqw1a9bo8ccfv2a/yMhISVJiYmJRlAUAAIq5EhN25s6dq4CAAHXu3Pma/Xbt2iVJCgoKKoKqAABAcVcibmNlZWVp7ty5io2NValS/3/JSUlJSkhIUKdOnVSxYkXt2bNHo0aN0v33368GDRq4sGIAAFBclIiws2bNGh05ckSDBg1yavfw8NCaNWs0bdo0paWlKSQkRD169NALL7zgokoBAEBxUyLCTvv27WWMydEeEhKiDRs2uKAiAABQUpSYMTsAAAAFQdgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWRtgBAACWVqzDzoQJE2Sz2Zxed955p2P+xYsXNWzYMFWsWFHlypVTjx49dOLECRdWDAAAiptiHXYkqW7dujp27Jjj9fXXXzvmjRo1Sp988omWLFmiDRs26Ndff1X37t1dWC0AAChuSrm6gOspVaqUAgMDc7T/8ccfmjNnjhISEtSmTRtJ0ty5cxUREaEtW7bo3nvvLepSAQBAMVTsr+wcPHhQwcHBql69uvr166cjR45Iknbs2KFLly6pXbt2jr533nmnqlatqs2bN19znenp6UpJSXF6AQAAayrWYScyMlLz5s3TqlWrNGvWLCUnJ+u+++7TuXPndPz4cXl4eMjX19dpmcqVK+v48ePXXG98fLx8fHwcr5CQkFu4FwAAwJWK9W2s6Ohox78bNGigyMhIhYaG6sMPP5SXl1eB1xsXF6fRo0c7plNSUgg8AABYVLG+svNnvr6+qlWrlhITExUYGKiMjAydPXvWqc+JEydyHeNzNbvdLm9vb6cXAACwphIVdlJTU5WUlKSgoCDdddddKl26tL788kvH/AMHDujIkSOKiopyYZUAAKA4Kda3scaMGaOuXbsqNDRUv/76q8aPHy93d3f17dtXPj4+Gjx4sEaPHi0/Pz95e3trxIgRioqK4kksAADgUKzDzs8//6y+ffvq9OnTqlSpklq0aKEtW7aoUqVKkqSpU6fKzc1NPXr0UHp6ujp06KB//vOfLq4aAAAUJ8U67CxatOia8z09PTVz5kzNnDmziCoCAAAlTYkaswMAAHCjCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSCDsAAMDSinXYiY+P1913363y5csrICBAMTExOnDggFOfVq1ayWazOb2efPJJF1UMAACKm2IddjZs2KBhw4Zpy5YtWr16tS5duqT27dsrLS3Nqd+QIUN07Ngxx+uNN95wUcUAAKC4KeXqAq5l1apVTtPz5s1TQECAduzYofvvv9/RXqZMGQUGBhZ1eQAAoAQo1ld2/uyPP/6QJPn5+Tm1L1iwQP7+/qpXr57i4uJ0/vz5a64nPT1dKSkpTi8AAGBNxfrKztWysrI0cuRINW/eXPXq1XO0P/LIIwoNDVVwcLD27Nmj5557TgcOHNCyZcvyXFd8fLwmTpxYFGUDAAAXKzFhZ9iwYdq7d6++/vprp/ahQ4c6/l2/fn0FBQWpbdu2SkpKUnh4eK7riouL0+jRox3TKSkpCgkJuTWFAwAAlyoRYWf48OH69NNPtXHjRt1xxx3X7BsZGSlJSkxMzDPs2O122e32Qq8TAAAUP8U67BhjNGLECH388cdav369qlWrdt1ldu3aJUkKCgq6xdUBAICSoFiHnWHDhikhIUErVqxQ+fLldfz4cUmSj4+PvLy8lJSUpISEBHXq1EkVK1bUnj17NGrUKN1///1q0KCBi6sHAADFQbEOO7NmzZJ05YMDrzZ37lwNGDBAHh4eWrNmjaZNm6a0tDSFhISoR48eeuGFF1xQLQAAKI6KddgxxlxzfkhIiDZs2FBE1QAAgJKoRH3ODgAAwI0i7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEsj7AAAAEuzTNiZOXOmwsLC5OnpqcjISH377beuLgkAABQDlgg7ixcv1ujRozV+/Hjt3LlTDRs2VIcOHXTy5ElXlwYAAFzMEmHnzTff1JAhQzRw4EDVqVNHs2fPVpkyZfTee++5ujQAAOBipVxdwM3KyMjQjh07FBcX52hzc3NTu3bttHnz5lyXSU9PV3p6umP6jz/+kCSlpKQUuI5zF7MKvCys52bOpcJk0o2rS0AxUhzOS3PVey9ws+dk9vLGXPu9rsSHnd9++02ZmZmqXLmyU3vlypX1448/5rpMfHy8Jk6cmKM9JCTkltSI29B4H1dXAOTgM4vzEsWLz6xZhbKec+fOyccn7/O7xIedgoiLi9Po0aMd01lZWTpz5owqVqwom83mwspKtpSUFIWEhOjo0aPy9vZ2dTmAJM5LFD+ck4XHGKNz584pODj4mv1KfNjx9/eXu7u7Tpw44dR+4sQJBQYG5rqM3W6X3W53avP19b1VJd52vL29+Q+MYofzEsUN52ThuNYVnWwlfoCyh4eH7rrrLn355ZeOtqysLH355ZeKiopyYWUAAKA4KPFXdiRp9OjRio2NVdOmTXXPPfdo2rRpSktL08CBA11dGgAAcDFLhJ3evXvr1KlTevHFF3X8+HE1atRIq1atyjFoGbeW3W7X+PHjc9wiBFyJ8xLFDedk0bOZ6z2vBQAAUIKV+DE7AAAA10LYAQAAlkbYAQAAlkbYAVDstWrVSiNHjrwl6x4wYIBiYmJuybqBW4lzN/8IOyhShw4dks1m065du/K9zK38RYfiq6jeyKdPn6558+bd8u2g5BgwYIBsNptsNptKly6tatWqaezYsbp48aKrS3PCuZt/lnj0HABuVGZmpmw2W74+fRW3n44dO2ru3Lm6dOmSduzYodjYWNlsNr3++uuuLs3heuduRkaGPDw8iqia4o0rO7ehrKwsxcfHq1q1avLy8lLDhg21dOlSSVd+AQwePNgxr3bt2po+fbrT8uvXr9c999yjsmXLytfXV82bN9fhw4d16NAhubm5afv27U79p02bptDQUGVl5f7N8Hv37lV0dLTKlSunypUr67HHHtNvv/0m6cpfWBs2bND06dMdf2kdOnSo8A8Kir3Lly9r+PDh8vHxkb+/v8aNG+f0Tcfp6ekaM2aMqlSporJlyyoyMlLr1693zJ83b558fX31n//8R3Xq1JHdbteRI0dyXEFatWqVWrRoIV9fX1WsWFFdunRRUlJSEe4pigO73a7AwECFhIQoJiZG7dq10+rVqzVp0iTVq1cvR/9GjRpp3LhxkqRt27bpgQcekL+/v3x8fNSyZUvt3LnTqb/NZtO//vUvPfTQQypTpoxq1qyp//znP475+Xkv/vO526pVKw0fPlwjR46Uv7+/OnToUIhHpGQj7NyG4uPj9f7772v27Nnat2+fRo0apUcffVQbNmxQVlaW7rjjDi1ZskQ//PCDXnzxRT3//PP68MMPJV35hRMTE6OWLVtqz5492rx5s4YOHSqbzaawsDC1a9dOc+fOddre3LlzNWDAALm55Tzdzp49qzZt2qhx48bavn27Vq1apRMnTqhXr16SrlymjYqK0pAhQ3Ts2DEdO3aMb6e/Tc2fP1+lSpXSt99+q+nTp+vNN9/Uv/71L8f84cOHa/PmzVq0aJH27Nmjhx9+WB07dtTBgwcdfc6fP6/XX39d//rXv7Rv3z4FBATk2E5aWppGjx6t7du368svv5Sbm5seeuihPMM6rG/v3r365ptv5OHhoUGDBmn//v3atm2bY/53332nPXv2OD61/9y5c4qNjdXXX3+tLVu2qGbNmurUqZPOnTvntN6JEyeqV69e2rNnjzp16qR+/frpzJkzknTd9+K8zJ8/Xx4eHtq0aZNmz55dyEeiBDO4rVy8eNGUKVPGfPPNN07tgwcPNn379s11mWHDhpkePXoYY4w5ffq0kWTWr1+fa9/FixebChUqmIsXLxpjjNmxY4ex2WwmOTnZGGNMcnKykWS+++47Y4wxL730kmnfvr3TOo4ePWokmQMHDhhjjGnZsqV59tlnC7K7KMFiY2NNt27djDFXzoGIiAiTlZXlmP/cc8+ZiIgIY4wxhw8fNu7u7uaXX35xWkfbtm1NXFycMcaYuXPnGklm165deW4nN6dOnTKSzPfff18Ie4WSIDY21ri7u5uyZcsau91uJBk3NzezdOlSY4wx0dHR5qmnnnL0HzFihGnVqlWe68vMzDTly5c3n3zyiaNNknnhhRcc06mpqUaS+e9//5vneq5+L86u8+pzt2XLlqZx48Y3tK+3C67s3GYSExN1/vx5PfDAAypXrpzj9f777zsu1c+cOVN33XWXKlWqpHLlyumdd97RkSNHJEl+fn4aMGCAOnTooK5du2r69Ok6duyYY/0xMTFyd3fXxx9/LOnKrYPWrVsrLCws13p2796tdevWOdVy5513ShK3DuDk3nvvlc1mc0xHRUXp4MGDyszM1Pfff6/MzEzVqlXL6VzasGGD03nk4eGhBg0aXHM7Bw8eVN++fVW9enV5e3s7zt3s/wO4PbRu3Vq7du3S1q1bFRsbq4EDB6pHjx6SpCFDhmjhwoW6ePGiMjIylJCQoEGDBjmWPXHihIYMGaKaNWvKx8dH3t7eSk1NzXEOXX0uli1bVt7e3jp58qSj7VrvxXm56667CmP3LYcByreZ1NRUSdLKlStVpUoVp3l2u12LFi3SmDFjNGXKFEVFRal8+fKaPHmytm7d6ug3d+5cPfPMM1q1apUWL16sF154QatXr9a9994rDw8P9e/fX3PnzlX37t2VkJCQ4z7zn+vp2rVrroP+goKCCmmvYXWpqalyd3fXjh075O7u7jSvXLlyjn97eXk5BabcdO3aVaGhoXr33XcVHBysrKws1atXTxkZGbekdhRPZcuWVY0aNSRJ7733nho2bKg5c+Zo8ODB6tq1q+x2uz7++GN5eHjo0qVL6tmzp2PZ2NhYnT59WtOnT1doaKjsdruioqJynEOlS5d2mrbZbI7bpfl5L86rbuRE2LnNXD0ws2XLljnmb9q0Sc2aNdPTTz/taMvtCkvjxo3VuHFjxcXFKSoqSgkJCbr33nslSY8//rjq1aunf/7zn7p8+bK6d++eZz1NmjTRRx99pLCwMJUqlfvp6OHhoczMzBvdVVjMn9/ks8dCuLu7q3HjxsrMzNTJkyd13333FXgbp0+f1oEDB/Tuu+861vP111/fVN0o+dzc3PT8889r9OjReuSRR+Tl5aXY2FjNnTtXHh4e6tOnj7y8vBz9N23apH/+85/q1KmTJOno0aOOhy7yK7/vxcgfbmPdZsqXL68xY8Zo1KhRmj9/vpKSkrRz507NmDFD8+fPV82aNbV9+3Z9/vnn+umnnzRu3DingXjJycmKi4vT5s2bdfjwYX3xxRc6ePCgIiIiHH0iIiJ077336rnnnlPfvn2d3gT+bNiwYTpz5oz69u2rbdu2KSkpSZ9//rkGDhzoCDhhYWHaunWrDh06pN9++42BorepI0eOaPTo0Tpw4IAWLlyoGTNm6Nlnn5Uk1apVS/369VP//v21bNkyJScn69tvv1V8fLxWrlyZ721UqFBBFStW1DvvvKPExEStXbtWo0ePvlW7hBLk4Ycflru7u2bOnCnpyh91a9eu1apVq5xuYUlSzZo19cEHH2j//v3aunWr+vXrd833wdxc770YN4awcxt66aWXNG7cOMXHxysiIkIdO3bUypUrVa1aNT3xxBPq3r27evfurcjISJ0+fdrpL4syZcroxx9/VI8ePVSrVi0NHTpUw4YN0xNPPOG0jcGDBysjIyPHm0B2UMm+ihMcHKxNmzYpMzNT7du3V/369TVy5Ej5+vo6nt4aM2aM3N3dVadOHVWqVImxE7ep/v3768KFC7rnnns0bNgwPfvssxo6dKhj/ty5c9W/f3/95S9/Ue3atRUTE6Nt27apatWq+d6Gm5ubFi1apB07dqhevXoaNWqUJk+efCt2ByVMqVKlNHz4cL3xxhtKS0tTzZo11axZM915552KjIx06jtnzhz9/vvvatKkiR577DE988wzuT75dy3Xey/GjbEZc9UHVQCF5KWXXtKSJUu0Z88ep/YtW7YoKipKp06dkr+/v4uqA4CbY4xRzZo19fTTT3P1rwRgzA4KVWpqqg4dOqS33npLL7/8sqP98uXLOnTokCZPnqyGDRsSdACUWKdOndKiRYt0/Phxx2froHgj7KBQDR8+XAsXLlRMTIzTLay9e/eqWbNmatSokd5//30XVggANycgIED+/v565513VKFCBVeXg3zgNhYAALA0BigDAABLI+wAAABLI+wAAABLI+wAAABLI+wAuO0sXrzY8WW1AKyPsAPA0mw2m5YvX+6YXrVqlf72t78pKirKdUUBKFKEHQBFZvPmzXJ3d1fnzp1dsv3k5GQ9++yz+uyzzxQYGOiSGgAUPcIOgCIzZ84cjRgxQhs3btSvv/56U+u6dOnSDS9TrVo1HThwQLVq1bqpbQMoWQg7AIpEamqqFi9erKeeekqdO3fWvHnznOavWLFCTZo0kaenp6pXr66JEyfq8uXLjvk2m02zZs3Sgw8+qLJly+qVV16RJM2aNUvh4eHy8PBQ7dq19cEHH+RZw6FDh2Sz2bRr1y5J0vr162Wz2fTll1+qadOmKlOmjJo1a6YDBw7cUG1vvvmm6tevr7JlyyokJERPP/20UlNTb/KIASg0BgCKwJw5c0zTpk2NMcZ88sknJjw83GRlZRljjNm4caPx9vY28+bNM0lJSeaLL74wYWFhZsKECY7lJZmAgADz3nvvmaSkJHP48GGzbNkyU7p0aTNz5kxz4MABM2XKFOPu7m7Wrl3rtNzHH39sjDEmOTnZSDLfffedMcaYdevWGUkmMjLSrF+/3uzbt8/cd999plmzZo7l81Pb1KlTzdq1a01ycrL58ssvTe3atc1TTz11qw4lgBtE2AFQJJo1a2amTZtmjDHm0qVLxt/f36xbt84YY0zbtm3Nq6++6tT/gw8+MEFBQY5pSWbkyJE51jlkyBCntocffth06tTJabnrhZ01a9Y4+q9cudJIMhcuXMh3bX+2ZMkSU7FixTznAyha3MYCcMsdOHBA3377rfr27StJKlWqlHr37q05c+ZIknbv3q1JkyapXLlyjteQIUN07NgxnT9/3rGepk2bOq13//79at68uVNb8+bNtX///huqr0GDBo5/BwUFSZJOnjyZ79rWrFmjtm3bqkqVKipfvrwee+wxnT592ql2AK7Dt54DuOXmzJmjy5cvKzg42NFmjJHdbtdbb72l1NRUTZw4Ud27d8+xrKenp+PfZcuWvSX1lS5d2vFvm80mScrKypKk69Z26NAhdenSRU899ZReeeUV+fn56euvv9bgwYOVkZGhMmXK3JKaAeQfYQfALXX58mW9//77mjJlitq3b+80LyYmRgsXLlSTJk104MAB1ahR44bWHRERoU2bNik2NtbRtmnTJtWpU6dQapd03dp27NihrKwsTZkyRW5uVy6Wf/jhh4W2fQA3j7AD4Jb69NNP9fvvv2vw4MHy8fFxmtejRw/NmTNHL7/8srp06aKqVauqZ8+ecnNz0+7du7V37169/PLLea77r3/9q3r16qXGjRurXbt2+uSTT7Rs2TKtWbOm0Op/8cUXr1lbjRo1dOnSJc2YMUNdu3bVpk2bNHv27ELbPoCbx5gdALfUnDlz1K5duxxBR7oSdrZv366goCB9+umn+uKLL3T33Xfr3nvv1dSpUxUaGnrNdcfExGj69On6+9//rrp16+rtt9/W3Llz1apVq0Krv0OHDtesrWHDhnrzzTf1+uuvq169elqwYIHi4+MLbfsAbp7NGGNcXQQAAMCtwpUdAABgaYQdAABgaYQdAABgaYQdAABgaYQdAABgaYQdAABgaYQdAABgaYQdAABgaYQdAABgaYQdAABgaYQdAABgaf8fEhwR1jHJOYsAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = \"Aerolínea\", \n",
    "              y = 'Costo',\n",
    "              data = df_vuelos_lisboa, \n",
    "              palette=colores2)\n",
    "plt.title('Costo promedio por aerolínea MAD-LIS')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Hace referencia a la tabla ya presentada anteriormente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Número de paradas por aerolínea MAD-FLR')"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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woVNoUKFTHx8vDHGmE2bNhlJpkiRIsnWnpy757t586YpV66cqV+/vr3t1KlTxt3d3YwcOdJh3p9++sl4eHg4tNepU8dIMlOnTnWYd+LEiUaSmTt3rsO6qlevbrJly2YiIyPt7Xe/5xLfzydPnrS3JW67O/9vL168aLy8vMx//vMfe9vw4cONr6+v+fXXXx3qGTRokHF3dzdnzpy5r22RkpCQEOPr62uMMaZly5amQYMGxhhj4uPjTWBgoBk2bJj9PfHJJ584LHvhwgXj4eFhpk+fbm+rUaOGef7555Osp2DBgqZp06Yp1jFhwgQjyXz77bep1ptYS3KPTZs2Jfu6UpL4/7N+/Xpz6dIlc/bsWbNkyRKTO3du4+XlZc6ePZvq8kgdh5agIkWKqFOnTvryyy917ty5DOu3e/fu9n+7u7urSpUqMsaoW7du9vbs2bOrZMmS+v333+1tixcvVunSpVWqVCn99ddf9kf9+vUlSZs2bXJYT506dRzO2YmPj9e6devUokULFSlSxN4eFBSk9u3ba/v27akeSli9erU8PDwcjqG7u7vrtddec5jv77//1saNG9W6dWtFRUXZ67x8+bIaNWqk48ePp+mKhBYtWih//vz259WqVdMTTzyh1atX29t8fHzs/75x44b++usv+5UTBw4cSNLnq6++mqQtLX3Ex8dr7dq1atGihQoUKGCfv3Tp0mrUqFGqfUZEROivv/5SnTp19PvvvysiIkKS7CMRq1atUlxcXCpbInn58uVzGFHx9/dX586ddfDgQZ0/f17S7f+zatWq2Q+jSbe/fffs2VOnTp3S0aNHHfoMCQlxqD01d8535coVRUREqFatWg7b/ZtvvlFCQoJat27tsM8GBgaqePHiSfZZLy8vde3a1aFt9erVCgwMVLt27extWbJkUb9+/RQdHa0tW7akqd47lSlTxn74Qrp9kmpy77datWrpkUcecai9YcOGio+P19atW+9rW6RF+/bttXnzZp0/f14bN27U+fPnUz2stGDBArm5uemll16yt7Vr107//e9/deXKlftad+IVRlFRUWmav2fPnvr+++8dHhUqVLivdSZq2LChcufOreDgYLVs2VK+vr5asWKFHn300XT1h9s4tARJ0nvvvac5c+Zo9OjR+vTTTzOkzzv/EEq3h2O9vb2T3HcmICDA4TyN48eP69ixYyle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v799WqFChTRixAi9+uqr+uKLL+ztcXFx+uKLL1ShQgV7W/369R36/fLLL5U9e3Zt2bJFzZo10/r16/XLL79o7dq1ypcvnyTpo48+UuPGjR2We++99xzW/+abb2rBggX2MHXmzBkNHDhQpUqVkiQVL148YzZEKggyAAC4mFWrVilbtmyKi4tTQkKC2rdvrw8++EDr16/XqFGj9MsvvygyMlK3bt3SjRs3FBMTY7+5nKenpx577DGH/i5cuKD33ntPmzdv1sWLFxUfH6+YmBidOXNGknTs2DEFBwfbQ4wkVa9ePUldCxcu1GeffaYTJ04oOjpat27dkr+/v336gAED1L17d82ZM0cNGzZUq1atVLRo0Yexiew4tAQAgIupV6+eDh06pOPHj+v69euaPXu2Ll26pGbNmumxxx7T0qVLtX//fk2ePFmSdPPmTfuyPj4+SW40FxISokOHDunTTz/Vzp07dejQIeXMmdNhuXvZtWuXOnTooCZNmmjVqlU6ePCg3n33XYc+PvjgAx05ckRNmzbVxo0bVaZMGS1btuwBt0bqGJEBAMDF+Pr6qlixYg5t+/fvV0JCgsaNG2e/CmnRokVp6m/Hjh364osv1KRJE0nS2bNn9ddff9mnly5dWmfPntW5c+fsP+C4e/duhz527typggUL6t1337W3nT59Osm6SpQooRIlSuiNN95Qu3btFBoaqhdeeCFNdaYHIzIAAFhAsWLFFBcXp0mTJun333/XnDlzNHXq1DQtW7x4cc2ZM0fHjh3Tnj171KFDB/uPNkpSw4YNVaJECYWEhOjw4cPatm2bQ2BJ7OPMmTNasGCBTpw4oc8++8xhtOX69evq27evNm/erNOnT2vHjh3au3evSpcunTEbIAUEGQAALKBChQoaP368xowZo3LlyiksLEyjRo1K07IzZszQlStXVKlSJXXq1En9+vVTnjx57NPd3Ny0bNkyXb9+XdWqVVP37t01cuRIhz6ee+45vfHGG+rbt68qVqyonTt3asiQIfbp7u7uunz5sjp37qwSJUqodevWaty4sYYNG5YxGyAFNmOMeahrcLLIyEgFBAQoIiLC4YSk+8FVS/+Pq5YA4MHcuHFDJ0+eVOHCheXt7e3scpwqtW2R1r/fjMgAAADLIsgAAADLIsgAAADLIsgAAADLIsgAAADLIsgAAADLIsgAAADLIsgAAADLIsgAAADLIsgAAADL4tevAQBwUZn9Eznp/RmayZMn65NPPtH58+dVoUIFTZo0SdWqVcvg6pLHiAwAAEi3hQsXasCAARo6dKgOHDigChUqqFGjRrp48WKmrJ8gAwAA0m38+PHq0aOHunbtqjJlymjq1KnKmjWrZs6cmSnrJ8gAAIB0uXnzpvbv36+GDRva29zc3NSwYUPt2rUrU2ogyAAAgHT566+/FB8fr7x58zq0582bV+fPn8+UGggyAADAspwaZLZu3armzZsrX758stlsWr58uX1aXFyc3n77bZUvX16+vr7Kly+fOnfurD///NN5BQMAALtcuXLJ3d1dFy5ccGi/cOGCAgMDM6UGpwaZa9euqUKFCpo8eXKSaTExMTpw4ICGDBmiAwcO6JtvvlF4eLiee+45J1QKAADu5unpqcqVK2vDhg32toSEBG3YsEHVq1fPlBqceh+Zxo0bq3HjxslOCwgI0Pfff+/Q9vnnn6tatWo6c+aMChQokBklAgCAVAwYMEAhISGqUqWKqlWrpokTJ+ratWvq2rVrpqzfUjfEi4iIkM1mU/bs2VOcJzY2VrGxsfbnkZGRmVAZAAD/Tm3atNGlS5f0/vvv6/z586pYsaLWrFmT5ATgh8UyQebGjRt6++231a5dO/n7+6c436hRozRs2LBMrAwAgIcjvXfazWx9+/ZV3759nbJuS1y1FBcXp9atW8sYoylTpqQ67+DBgxUREWF/nD17NpOqBAAAmc3lR2QSQ8zp06e1cePGVEdjJMnLy0teXl6ZVB0AAHAmlw4yiSHm+PHj2rRpk3LmzOnskgAAgAtxapCJjo7Wb7/9Zn9+8uRJHTp0SDly5FBQUJBatmypAwcOaNWqVYqPj7ffJTBHjhzy9PR0VtkAAMBFODXI7Nu3T/Xq1bM/HzBggCQpJCREH3zwgVasWCFJqlixosNymzZtUt26dTOrTAAA4KKcGmTq1q0rY0yK01ObBgAAYImrlgAAAJJDkAEAAJZFkAEAAJZFkAEAAJbl0veRAQDg3+zcquaZur6gZivva/6tW7fqk08+0f79+3Xu3DktW7ZMLVq0eDjFpYARGQAAkC7Xrl1ThQoVNHnyZKfVwIgMAABIl8aNG6tx48ZOrYERGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFkEGQAAYFlctQQAANIlOjpav/32m/35yZMndejQIeXIkUMFChTIlBoIMgAAIF327dunevXq2Z8PGDBAkhQSEqJZs2ZlSg0EGQAAXNT93mk3s9WtW1fGGKfWwDkyAADAsggyAADAsggyAADAsggyAADAsggyAAA4gbNPknUFGbENCDIAAGSiLFmySJJiYmKcXInzJW6DxG2SHlx+DQBAJnJ3d1f27Nl18eJFSVLWrFlls9mcXFXmMsYoJiZGFy9eVPbs2eXu7p7uvggyAABkssDAQEmyh5l/q+zZs9u3RXoRZAAAyGQ2m01BQUHKkyeP4uLinF2OU2TJkuWBRmISEWQAAHASd3f3DPlj/m/Gyb4AAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCyCDIAAMCynBpktm7dqubNmytfvnyy2Wxavny5w3RjjN5//30FBQXJx8dHDRs21PHjx51TLAAAcDlODTLXrl1ThQoVNHny5GSnf/zxx/rss880depU7dmzR76+vmrUqJFu3LiRyZUCAABX5OHMlTdu3FiNGzdOdpoxRhMnTtR7772n559/XpL09ddfK2/evFq+fLnatm2bmaUCAAAX5LLnyJw8eVLnz59Xw4YN7W0BAQF64okntGvXrhSXi42NVWRkpMMDAAD8M7lskDl//rwkKW/evA7tefPmtU9LzqhRoxQQEGB/BAcHP9Q6AQCA87hskEmvwYMHKyIiwv44e/ass0sCAAAPicsGmcDAQEnShQsXHNovXLhgn5YcLy8v+fv7OzwAAMA/k8sGmcKFCyswMFAbNmywt0VGRmrPnj2qXr26EysDAACuwqlXLUVHR+u3336zPz958qQOHTqkHDlyqECBAurfv79GjBih4sWLq3DhwhoyZIjy5cunFi1aOK9oAADgMpwaZPbt26d69erZnw8YMECSFBISolmzZumtt97StWvX1LNnT129elVPPfWU1qxZI29vb2eVDAAAXIjNGGOcXcTDFBkZqYCAAEVERKT7fJnmy85lcFXWtfKFIGeXAAD4F0jr32+XPUcGAADgXggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAslw6yMTHx2vIkCEqXLiwfHx8VLRoUQ0fPlzGGGeXBgAAXICHswtIzZgxYzRlyhTNnj1bZcuW1b59+9S1a1cFBASoX79+zi4PAAA4mUsHmZ07d+r5559X06ZNJUmFChXS/Pnz9cMPPzi5MgAA4Apc+tBSjRo1tGHDBv3666+SpMOHD2v79u1q3LhxisvExsYqMjLS4QEAAP6ZXHpEZtCgQYqMjFSpUqXk7u6u+Ph4jRw5Uh06dEhxmVGjRmnYsGGZWCUAAHAWlx6RWbRokcLCwjRv3jwdOHBAs2fP1tixYzV79uwUlxk8eLAiIiLsj7Nnz2ZixQAAIDO59IjMwIEDNWjQILVt21aSVL58eZ0+fVqjRo1SSEhIsst4eXnJy8srM8sEAABO4tIjMjExMXJzcyzR3d1dCQkJTqoIAAC4EpcekWnevLlGjhypAgUKqGzZsjp48KDGjx+vl19+2dmlAQAAF+DSQWbSpEkaMmSIevfurYsXLypfvnx65ZVX9P777zu7NAAA4AJcOsj4+flp4sSJmjhxorNLAQAALsilz5EBAABIDUEGAABYFkEGAABYFkEGAABYFkEGAABYFkEGAABYFkEGAABYFkEGAABYVrqCTP369XX16tUk7ZGRkapfv/6D1gQAAJAm6Qoymzdv1s2bN5O037hxQ9u2bXvgogAAANLivn6i4Mcff7T/++jRozp//rz9eXx8vNasWaP8+fNnXHUAAACpuK8gU7FiRdlsNtlstmQPIfn4+GjSpEkZVhwAAEBq7ivInDx5UsYYFSlSRD/88INy585tn+bp6ak8efLI3d09w4sEAABIzn0FmYIFC0qSEhISHkoxAAAA9+O+gsydjh8/rk2bNunixYtJgs3777//wIUBAADcS7qCzPTp09WrVy/lypVLgYGBstls9mk2m40gAwAAMkW6gsyI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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = \"Aerolínea\", \n",
    "              data = df_vuelos_florencia, \n",
    "              palette=[\"#33B5FF\", \"#FFBB33\"], \n",
    "              hue = \"Paradas\")\n",
    "plt.title('Número de paradas por aerolínea MAD-FLR')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Este gráfico demuestra que para Florencia puedo tomar en cuenta las paradas y el tiempo de vuelo como se ve afectado. Solo lo hago para Florencia porque el Lisboa, todos los vuelos encontrados son directos"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Hospedajes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Debajo mostraré la relación que existe entre los precios de hospedaje de ambas ciudades y su calificación (en base 10)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Calificación', ylabel='Precio'>"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAGwCAYAAABIC3rIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABUeUlEQVR4nO3deXQT5f4G8CdJk7Rpm3RvUigtLVvLvol1QRCkLHIRcUFQirLotaiIKHLd6sqmqCjC1SvggsBVEREUhcqiUJYLlLXUUpYW6AZd0i1plvn9wY9oTIE2TTtp83zOyTnMO+9kvtMhzdOZd2YkgiAIICIiIvJgUrELICIiIhIbAxERERF5PAYiIiIi8ngMREREROTxGIiIiIjI4zEQERERkcdjICIiIiKP5yV2Ac2B1WrFhQsX4O/vD4lEInY5REREVAeCIKC8vBwRERGQSq99DIiBqA4uXLiAyMhIscsgIiIiJ+Tm5qJ169bX7MNAVAf+/v4ALv9A1Wq1yNUQERFRXej1ekRGRtq+x6+FgagOrpwmU6vVDERERETNTF2Gu3BQNREREXk8BiIiIiLyeAxERERE5PE4hsiFLBYLTCaT2GXQdcjlcshkMrHLICIiN8JA5AKCICA/Px+lpaVil0J1FBAQAK1Wy/tKERERAAYil7gShsLCwqBSqfgl68YEQUBVVRUKCwsBADqdTuSKiIjIHTAQNZDFYrGFoeDgYLHLoTrw8fEBABQWFiIsLIynz4iIiIOqG+rKmCGVSiVyJVQfV/YXx3wRERHAQOQyPE3WvHB/ERHRXzEQERERkcdjICIiomajvLoCRfpLEARB7FKohWEg8hASiQTr1q1r0HusWLECAQEBDa4lOjoa7733XoPfh4g8h8lswq4TezH5oydx79sT8cFPH+N8cZ7YZVELwkDUQuTn5+OJJ55ATEwMlEolIiMjMXLkSKSmpgIA8vLyMGzYMJGrJCJyzvFzmXjs3zNwLPcELuov4eNfPsPHv6xAjblG7NKohWAgagHOnDmD3r1749dff8WCBQtw5MgRbNq0CQMHDkRycjIAQKvVQqlUilwpEZFz9mbth1Ww2rWt2/sj8koKRKqIWhoGohbg8ccfh0Qiwd69ezFmzBh06NABnTt3xowZM7B7924A9qfMtm3bBolEYndn7fT0dEgkEpw5c8bWtmLFCrRp0wYqlQqjR4/GpUuX7NabnZ2NUaNGITw8HH5+fujbty+2bNli16ewsBAjR46Ej48P2rZti5UrVzbKz4CIWjal3PEPOi+ZDDIJv8bINfg/qZkrLi7Gpk2bkJycDF9fX4f5zo752bNnDyZNmoRp06YhPT0dAwcOxBtvvGHXp6KiAsOHD0dqaioOHjyIoUOHYuTIkcjJybH1mThxInJzc7F161Z88803+Oijj2x3iSYiqqsb2veG999C0aRBDyEiiHebJ9fgnaqbuZMnT0IQBHTq1Mml7/v+++9j6NCheO655wAAHTp0wK5du7Bp0yZbn+7du6N79+626ddffx3fffcd1q9fj2nTpuGPP/7ATz/9hL1796Jv374AgE8//RRxcXEurZWIWr5Ordrjsyc+wre7f8DZolzcfeNI3NihD6RS/l1PrsFA1Mw11qWnGRkZGD16tF1bQkKCXSCqqKhASkoKNm7ciLy8PJjNZlRXV9uOEGVkZMDLywu9e/e2LdOpUyeXXKlGRJ6nc5s4dG4TB6vVyiBELsdA1My1b98eEokEJ06cqPMyV36R/DVMOfMIi5kzZ2Lz5s14++230a5dO/j4+OCee+5BTQ2v+iCixsMwRI2B/6uauaCgICQmJmLx4sWorKx0mP/XgdNXhIaGArh8Kf4V6enpdn3i4uKwZ88eu7YrA7Sv2LlzJyZOnIjRo0eja9eu0Gq1doOyO3XqBLPZjP3799vaMjMza62JiIhITAxELcDixYthsVhwww034Ntvv0VWVhYyMjKwaNEiJCQkOPRv164dIiMjkZKSgqysLGzcuBHvvPOOXZ8nn3wSmzZtwttvv42srCx8+OGHdqfLgMtHp9auXYv09HQcOnQI48aNg9X652WxHTt2xNChQ/Hoo49iz5492L9/PyZPnmx72jwREZG7YCBqAWJiYnDgwAEMHDgQzzzzDLp06YI77rgDqampWLJkiUN/uVyOVatW4cSJE+jWrRvmzZvncAXZjTfeiE8++QTvv/8+unfvjl9++QUvvviiXZ+FCxciMDAQN910E0aOHInExET06tXLrs/y5csRERGB2267DXfffTemTp2KsLAw1/8QiIiIGkAi8IEw16XX66HRaFBWVga1Wm03z2Aw4PTp02jbti28vb1FqpDqi/uNiKjlu9b399/xCBERERF5PAYiIiKiFs5sMaOo7BKqjNVil+K2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9fLojIwMbNq0Cfv27UOfPn0AAB988AGGDx+Ot99+GxEREVi5ciVqamqwbNkyKBQKdO7cGenp6Vi4cKFdcPoro9EIo9Fom9br9U5uIRERETUHbj+GaNu2bQgLC0PHjh3xz3/+E5cuXbLNS0tLQ0BAgC0MAcDgwYMhlUqxZ88eW5/+/ftDoVDY+iQmJiIzMxMlJSW1rnPOnDnQaDS2V2RkZCNtHREREbkDtw5EQ4cOxeeff47U1FTMmzcP27dvx7Bhw2CxWAAA+fn5CAsLs1vGy8sLQUFByM/Pt/UJDw+363Nl+kqfv5s9ezbKyspsr9zcXFdvGhEREbkRt74P0dixY23/7tq1K7p164bY2Fhs27YNgwYNarT1KpVKKJXKRnt/IiIici9ufYTo72JiYhASEoKTJ08CuPzIjL8/LsNsNqO4uNg27kir1aKgoMCuz5VpPrqBiIiIgGYWiM6dO4dLly5Bp9MBABISElBaWor9+/fb+vz666+wWq3o16+frc+OHTvsHqmxefNmdOzYEYGBgU27AUREROSWRA1EFRUVSE9PR3p6OgDg9OnTSE9PR05ODioqKvDss89i9+7dOHPmDFJTUzFq1Ci0a9cOiYmJAIC4uDgMHToUU6ZMwd69e7Fz505MmzYNY8eORUREBABg3LhxUCgUmDRpEo4dO4Y1a9bg/fffx4wZM8TabCIiInIzEkEQBLFWvm3bNgwcONChPSkpCUuWLMFdd92FgwcPorS0FBERERgyZAhef/11u0HSxcXFmDZtGn744QdIpVKMGTMGixYtgp+fn63P4cOHkZycjH379iEkJARPPPEEZs2aVec69Xo9NBoNysrKoFarG7bRRERE1CTq8/0taiBqLhiIiIiImp/6fH83qzFERERERI2BgYiIiIg8HgMREREReTwGIiIiIvJ4DERERETk8RiIiIiIyOMxEBEREZHHYyAiIiIij8dARERERB6PgYiIiIg8HgMREREReTwGIiIiIvJ4DERERETk8RiIiIiIyOMxEBEREZHHYyAiIiIij8dARERERB6PgYiIiIg8HgMREREReTwGIiIiIvJ4DERERETk8RiIiIiIyOMxEBEREZHHYyAiIiIij8dARERERB6PgYiIiIg8HgMREREReTwGIiIiIvJ4DERERETk8RiIiIiIyOMxEBEREZHHYyAiIiIij8dARERE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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.scatterplot(x = \"Calificación\", # variable que queremos en el eje x\n",
    "                y = \"Precio\", # variable que queremos en el eje y\n",
    "                data = df_florencia_lisboa, # conjunto de datos de donde vienen los datos\n",
    "                hue = \"Ciudad\", # de que queremos que dependa el color de los puntos\n",
    "                palette= \"cubehelix\", # color de los puntos\n",
    "                s = 20) # tamaño de los puntos"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Gráfico de dispersión donde se muestra la relación entre el Rating de cada hospedaje en relación al precio del mismo. A medida que el rating aumenta, se ve un ligero aumento en el precio."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Al perder las llamadas de la API, no pude agrandar la muestra."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\862146273.py:1: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.boxplot(x = \"Ciudad\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Boxplot por ciudades')"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAHHCAYAAABeLEexAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABDyklEQVR4nO3dfVwVZf7/8fcB5QAKeIPcFYFS4T1mGtGNaZqIrtVmt5qiWXYDVFqturYrWi2mrWlmbu4vsVpLtztzLU0wyV00a3VB02S9yZsSUDNBNEFgfn+0zNcTaEDgOYd5PR+P84i55joznzk95Ly55poZm2EYhgAAACzMw9kFAAAAOBuBCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCECDs9lsSk1NdXYZLmP06NGKjIx0+W3y/w1WRiAC3MjixYtls9kcXkFBQerXr59WrVrl7PJ+tR07dig1NVX79u1zdikALKaZswsAUHfTp09X+/btZRiGCgsLtXjxYg0ePFj/+Mc/9Jvf/MbZ5dXbjh07NG3aNPXt27fBRz+c6a9//asqKyudXQaA8yAQAW4oISFBvXr1MpfHjh2r4OBgvf32224diFxRZWWlysrK5O3tXe9tNG/evAErAtAYOGUGNAGtWrWSj4+PmjVz/Bvn5MmTeuKJJxQeHi673a7o6Gi98MILMgxDkvTjjz+qY8eO6tixo3788UfzfceOHVNoaKiuueYaVVRUSPppzkrLli21d+9excfHq0WLFgoLC9P06dPN7Z3Pf/7zHyUkJMjf318tW7ZU//799fnnn5vrFy9erDvuuEOS1K9fP/OUYFZW1jm3WZeafumzqGKz2ZScnKwlS5aoS5custvtWr169XmPbdWqVbrhhhvk5+cnf39/9e7dW2+99ZZDnWePeGVlZdV4bPv27ZPNZtPixYsd2pcvX66uXbvK29tbXbt21QcffFBjHS+88IKuueYatW3bVj4+Prryyiv17rvvVutXWlqq8ePHq127dvLz89PNN9+sb7/9tsZtfvfdd7rvvvsUHBwsu92uLl26aNGiRdX6zZs3T126dJGvr69at26tXr16OXwGgKtjhAhwQ0VFRTp69KgMw9Dhw4c1b948lZSU6N577zX7GIahm2++WevWrdPYsWPVo0cPffLJJ3rqqaf03Xff6cUXX5SPj49ef/11XXvttZoyZYpmz54tSUpKSlJRUZEWL14sT09Pc5sVFRUaNGiQrr76as2cOVOrV6/W1KlTVV5erunTp5+z3u3bt+v666+Xv7+/fve736l58+Z69dVX1bdvX3322WeKjY1Vnz599Oijj+qll17S73//e3Xq1EmSzP+eS21qqs1ncbZPP/1Uf//735WcnKzAwMDznr5bvHix7rvvPnXp0kWTJ09Wq1at9J///EerV6/W8OHDz1t7baxZs0bDhg1T586dlZaWpu+//15jxozRxRdfXK3v3LlzdfPNN2vEiBEqKyvT0qVLdccdd2jlypUaMmSI2e/+++/X3/72Nw0fPlzXXHONPv30U4f1VQoLC3X11VebIbFdu3ZatWqVxo4dq+LiYj3++OOSfjol+Oijj+r222/XY489ptOnT2vr1q3atGlTg3wGwAVhAHAb6enphqRqL7vdbixevNih7/Llyw1JxrPPPuvQfvvttxs2m83YvXu32TZ58mTDw8PDWL9+vfHOO+8Ykow5c+Y4vC8xMdGQZKSkpJhtlZWVxpAhQwwvLy/jyJEjZrskY+rUqebyrbfeanh5eRl79uwx2w4dOmT4+fkZffr0Mduq9r1u3bpafR61rakun4Ukw8PDw9i+ffsv7v/48eOGn5+fERsba/z4448O6yorKx3qjIiIMJfXrVtX43F+8803hiQjPT3dbOvRo4cRGhpqHD9+3Gxbs2aNIclhm4ZhGKdOnXJYLisrM7p27WrceOONZltOTo4hyXjkkUcc+g4fPrza/7exY8caoaGhxtGjRx363n333UZAQIC5v1tuucXo0qWLAbgzTpkBbmj+/PnKyMhQRkaG/va3v6lfv366//779f7775t9Pv74Y3l6eurRRx91eO8TTzwhwzAcrkpLTU1Vly5dlJiYqEceeUQ33HBDtfdVSU5ONn+uGjkoKytTZmZmjf0rKiq0Zs0a3XrrrerQoYPZHhoaquHDh+tf//qXiouL6/U51LamunwWknTDDTeoc+fOv7jfjIwMnThxQpMmTao2x8hms9X3cEz5+fnKyclRYmKiAgICzPabbrqpxvp8fHzMn3/44QcVFRXp+uuv15YtW8z2jz/+WJKqfRZVoz1VDMPQe++9p6FDh8owDB09etR8xcfHq6ioyNxuq1at9O233+rLL7/81ccMOAuBCHBDV111lQYMGKABAwZoxIgR+uijj9S5c2czCEjS/v37FRYWJj8/P4f3Vp2C2r9/v9nm5eWlRYsW6ZtvvtGJEyeUnp5e4xe6h4eHQ6iRpMsvv1ySznmp/JEjR3Tq1ClFR0dXW9epUydVVlbq4MGDtT/4etRUl89Cktq3b1+rfe/Zs0eS1LVr1zrXXRtVdV122WXV1tX0ea5cuVJXX321vL291aZNG7Vr104LFixQUVGRwzY9PDwUFRV13u0dOXJEx48f18KFC9WuXTuH15gxYyRJhw8fliRNnDhRLVu21FVXXaXLLrtMSUlJys7O/nUHD1xgBCKgCfDw8FC/fv2Un5+vXbt21Wsbn3zyiSTp9OnT9d5GU3H2SEtjONfoUdUE9vr45z//qZtvvlne3t565ZVX9PHHHysjI0PDhw+v1aT3n6u6TcC9995rjkb+/HXttddK+ilY5uXlaenSpbruuuv03nvv6brrrtPUqVPrfTzAhcakaqCJKC8vlySVlJRIkiIiIpSZmakTJ044jIzs3LnTXF9l69atmj59usaMGaOcnBzdf//92rZtm8NpGumnL8m9e/eaIzCS9N///leSzjnxuF27dvL19VVeXl61dTt37pSHh4fCw8Ml1e80U21qqstnURdVoyxfffWVLr300lq/r3Xr1pKk48ePO7T/fKSqqq6aAurPP8/33ntP3t7e+uSTT2S328329PT0atusrKzUnj17HEaFfr69qivQKioqNGDAgF88phYtWuiuu+7SXXfdpbKyMt1222167rnnNHny5F91ywLgQmGECGgCzpw5ozVr1sjLy8s8DTR48GBVVFTo5Zdfduj74osvymazKSEhwXzv6NGjFRYWprlz52rx4sUqLCzU+PHja9zX2dszDEMvv/yymjdvrv79+9fY39PTUwMHDtSHH37ocFqtsLBQb731lq677jr5+/tL+ulLVaoeFH7JL9VU28+irgYOHCg/Pz+lpaXp9OnTDuvONyoTEREhT09PrV+/3qH9lVdecVgODQ1Vjx499Prrrzuc9srIyNCOHTsc+np6espmszmMMu3bt0/Lly936Fd1rC+99JJD+5w5c6ptb9iwYXrvvff01VdfVTuGI0eOmD9///33Duu8vLzUuXNnGYahM2fOVHsv4IoYIQLc0KpVq8zRjcOHD+utt97Srl27NGnSJDNcDB06VP369dOUKVO0b98+xcTEaM2aNfrwww/1+OOPm6Mbzz77rHJycrR27Vr5+fmpe/fu+uMf/6inn35at99+uwYPHmzu19vbW6tXr1ZiYqJiY2O1atUqffTRR/r973+vdu3anbPeZ599VhkZGbruuuv0yCOPqFmzZnr11VdVWlqqmTNnmv169OghT09PPf/88yoqKpLdbteNN96ooKCgc267NjXV9rOoK39/f7344ou6//771bt3bw0fPlytW7dWbm6uTp06pddff73G9wUEBOiOO+7QvHnzZLPZFBUVpZUrV5pzcs6WlpamIUOG6LrrrtN9992nY8eOmff8qRoNlKQhQ4Zo9uzZGjRokIYPH67Dhw9r/vz5uvTSS7V161aHz/iee+7RK6+8oqKiIl1zzTVau3atdu/eXW3fM2bM0Lp16xQbG6sHHnhAnTt31rFjx7RlyxZlZmbq2LFjkn4KhiEhIbr22msVHBysr7/+Wi+//LKGDBlSbd4W4LKcdn0bgDqr6bJ7b29vo0ePHsaCBQscLvU2DMM4ceKEMX78eCMsLMxo3ry5cdlllxmzZs0y+23evNlo1qyZw2XrhmEY5eXlRu/evY2wsDDjhx9+MAzjp0vHW7RoYezZs8cYOHCg4evrawQHBxtTp041KioqHN6vn12+bRiGsWXLFiM+Pt5o2bKl4evra/Tr18/YsGFDtWP861//anTo0MHw9PT8xUvw61LTL30WZ9eelJR0zn3WZMWKFcY111xj+Pj4GP7+/sZVV11lvP322w51/vwS+SNHjhjDhg0zfH19jdatWxsPPvig8dVXX1W77N4wDOO9994zOnXqZNjtdqNz587G+++/X+M2X3vtNeOyyy4z7Ha70bFjRyM9Pd2YOnWq8fNf9T/++KPx6KOPGm3btjVatGhhDB061Dh48GCN/98KCwuNpKQkIzw83GjevLkREhJi9O/f31i4cKHZ59VXXzX69OljtG3b1rDb7UZUVJTx1FNPGUVFRXX6HAFnshlGPWbbAbCc0aNH691333UYlXA2V6wJgHtiDhEAALA8AhEAALA8AhEAALA85hABAADLY4QIAABYHoEIAABYHjdmrIXKykodOnRIfn5+DfIEawAA0PgMw9CJEycUFhYmD4/zjwERiGrh0KFD5rOWAACAezl48KAuvvji8/YhENVC1a3nDx48aD4W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u91uLrds2VIHDx6Un5+fbDbbhSobTlJcXKzw8HAdPHiQh/kCTQz/vq3FMAydOHFCYWFhv9jXEoFIkiZMmKDExET16tVLV111lebMmaOTJ09qzJgxv/heDw8PXXzxxRegSrgSf39/fmECTRT/vq3jl0aGqlgmEN111106cuSI/vjHP6qgoEA9evTQ6tWrq020BgAA1mMzajPTCLCQ4uJiBQQEqKioiL8ggSaGf984F0vchwioC7vdrqlTpzrMIwPQNPDvG+fCCBEAALA8RogAAIDlEYgAAIDlEYgAAIDlEYjg9vr27avHH3/c2WUAuMBsNpuWL1/e4H1hTQQiuIXRo0fLZrNVe+3evdvZpQFoRKNHjzafMPBz+fn5SkhIuLAFocmyzI0Z4f4GDRqk9PR0h7Z27dr96u1WVFTIZrPJw4O/DwB3UtOzKIH64hsAbsNutyskJMTh5enpWa3fDz/8oFGjRql169by9fVVQkKCdu3aZa5fvHixWrVqpRUrVqhz586y2+06cOCASktL9eSTT+qiiy5SixYtFBsbq6ysrGrv++STT9SpUye1bNlSgwYNUn5+vsP+Fy1apC5dushutys0NNTheXnHjx/X/fffr3bt2snf31833nijcnNzG/7DAizg7NNgZWVlSk5OVmhoqLy9vRUREaG0tDSH/lUjSj4+PurQoYPeffddh/Xbtm3TjTfeKB8fH7Vt21bjxo1TSUmJub5qtOqFF15QaGio2rZtq6SkJJ05c6bRjxWNj0CEJmf06NH697//rRUrVmjjxo0yDEODBw92+KV16tQpPf/88/p//+//afv27QoKClJycrI2btyopUuXauvWrbrjjjs0aNAghzB16tQpvfDCC3rzzTe1fv16HThwQE8++aS5fsGCBUpKStK4ceO0bds2rVixQpdeeqm5/o477tDhw4e1atUqbd68WT179lT//v117NixC/PhAE3USy+9pBUrVujvf/+78vLytGTJEkVGRjr0+cMf/qBhw4YpNzdXI0aM0N13362vv/5aknTy5EnFx8erdevW+vLLL/XOO+8oMzOz2gPA161bpz179mjdunV6/fXXtXjxYi1evPgCHSUalQG4gcTERMPT09No0aKF+br99tsNwzCMG264wXjssccMwzCM//73v4YkIzs723zv0aNHDR8fH+Pvf/+7YRiGkZ6ebkgycnJyzD779+83PD09je+++85hv/379zcmT57s8L7du3eb6+fPn28EBweby2FhYcaUKVNqPIZ//vOfhr+/v3H69GmH9qioKOPVV1+t60cCWEJiYqJxyy231LhOkvHBBx8YhmEYKSkpxo033mhUVlaes+9DDz3k0BYbG2s8/PDDhmEYxsKFC43WrVsbJSUl5vqPPvrI8PDwMAoKCsxaIiIijPLycrPPHXfcYdx11131PTy4EOYQwW3069dPCxYsMJdbtGhRrc/XX3+tZs2aKTY21mxr27atoqOjzb8EJcnLy0vdu3c3l7dt26aKigpdfvnlDtsrLS1V27ZtzWVfX19FRUWZy6GhoTp8+LAk6fDhwzp06JD69+9fY/25ubkqKSlx2J4k/fjjj9qzZ895jx3A+Y0ePVo33XSToqOjNWjQIP3mN7/RwIEDHfrExcVVW87JyZH00++OmJgYh98r1157rSorK5WXl2c+CLxLly4Op+pDQ0O1bdu2RjoqXEgEIriNFi1aOJx++jV8fHxks9nM5ZKSEnl6emrz5s3V5iW1bNnS/Ll58+YO62w2m4z/Pf3Gx8fnvPssKSlRaGiow7ykKq1atarjEQA4W8+ePfXNN99o1apVyszM1J133qkBAwZUmyf0a9X0O6CysrJB9wHnYA4RmpROnTqpvLxcmzZtMtu+//575eXlqXPnzud83xVXXKGKigodPnxYl156qcOrtley+Pn5KTIyUmvXrq1xfc+ePVVQUKBmzZpV20dgYGDdDhRANf7+/rrrrrv017/+VcuWLdN7773nMD/v888/d+j/+eefq1OnTpJ++t2Rm5urkydPmuuzs7Pl4eGh6OjoC3MAcCpGiNCkXHbZZbrlllv0wAMP6NVXX5Wfn58mTZqkiy66SLfccss533f55ZdrxIgRGjVqlP785z/riiuu0JEjR7R27Vp1795dQ4YMqdX+U1NT9dBDDykoKEgJCQk6ceKEsrOzlZKSogEDBiguLk633nqrZs6cqcsvv1yHDh3SRx99pN/+9rfq1atXQ30MQJNSVFRkntqq8vNTz7Nnz1ZoaKiuuOIKeXh46J133lFISIjD6Os777yjXr166brrrtOSJUv0xRdf6LXXXpMkjRgxQlOnTlViYqJSU1N15MgRpaSkaOTIkebpMjRtBCI0Oenp6Xrsscf0m9/8RmVlZerTp48+/vjjakPdNb3v2Wef1RNPPKHvvvtOgYGBuvrqq/Wb3/ym1vtOTEzU6dOn9eKLL+rJJ59UYGCgbr/9dkk/Da1//PHHmjJlisaMGaMjR44oJCREffr04RcucB5ZWVm64oorHNrGjh3rsOzn56eZM2dq165d8vT0VO/evfXxxx873F9s2rRpWrp0qR555BGFhobq7bffNkeOfX199cknn+ixxx5T79695evrq2HDhmn27NmNf4BwCTajagIEAACARTGHCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCAAAWB6BCECTYrPZtHz58l+1jcWLFzfI8+UiIyM1Z86cX70dAI2PQATArRQUFCglJUUdOnSQ3W5XeHi4hg4daj5DLj8/XwkJCU6uEoC74dEdANzGvn37dO2116pVq1aaNWuWunXrpjNnzuiTTz5RUlKSdu7cWeuH8QLA2RghAuA2HnnkEdlsNn3xxRcaNmyYLr/8cnXp0kUTJkwwn2R+9imzrKws2Ww2HT9+3NxGTk6ObDab9u3bZ7YtXrxYl1xyiXx9ffXb3/5W33//vcN+9+zZo1tuuUXBwcFq2bKlevfurczMTIc+hw8f1tChQ+Xj46P27dtryZIljfIZAGgcBCIAbuHYsWNavXq1kpKS1KJFi2rr6zvnZ9OmTRo7dqySk5OVk5Ojfv366dlnn3XoU1JSosGDB2vt2rX6z3/+o0GDBmno0KE6cOCA2Wf06NE6ePCg1q1bp3fffVevvPKKDh8+XK+aAFx4nDID4BZ2794twzDUsWPHBt3u3LlzNWjQIP3ud7+TJF1++eXasGGDVq9ebfaJiYlRTEyMufzMM8/ogw8+0IoVK5ScnKz//ve/WrVqlb744gv17t1bkvTaa6+pU6dODVorgMbDCBEAt2AYRqNs9+uvv1ZsbKxDW1xcnMNySUmJnnzySXXq1EmtWrVSy5Yt9fXXX5sjRF9//bWaNWumK6+80nxPx44dG+RKNQAXBiNEANzCZZddJpvNpp07d9b6PR4eP/3Nd3aYOnPmTJ33/eSTTyojI0MvvPCCLr30Uvn4+Oj2229XWVlZnbcFwDUxQgTALbRp00bx8fGaP3++Tp48WW392ROnq7Rr107ST5fiV8nJyXHo06lTJ23atMmhrWqCdpXs7GyNHj1av/3tb9WtWzeFhIQ4TMru2LGjysvLtXnzZrMtLy+vxpoAuCYCEQC3MX/+fFVUVOiqq67Se++9p127dunrr7/WSy+9VO00lyRdeumlCg8PV2pqqnbt2qWPPvpIf/7znx36PProo1q9erVeeOEF7dq1Sy+//LLD/CHpp9Gp999/Xzk5OcrNzdXw4cNVWVlpro+OjtagQYP04IMPatOmTdq8ebPuv/9++fj4NM4HAaDBEYgAuI0OHTpoy5Yt6tevn5544gl17dpVN910k9auXasFCxZU69+8eXO9/fbb2rlzp7p3767nn3++2hVkV199tf76179q7ty5iomJ0Zo1a/T000879Jk9e7Zat26ta665RkOHDlV8fLx69uzp0Cc9PV1hYWG64YYbdNttt2ncuHEKCgpq+A8BQKOwGY01UxEAAMBNMEIEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAsj0AEAAAs7/8DKBkxXpetOqwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x = \"Ciudad\",\n",
    "            y = \"Precio\",\n",
    "            data = df_florencia_lisboa, \n",
    "            palette = 'viridis');\n",
    "plt.title('Boxplot por ciudades')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Boxplot: podemos ver desde el percentil 25% hasta el 75% de ambas ciudades y sus alojamientos. Se puede ver una continuación de lo visto en las tablas, existe una concentración de precios para Florencia pero cuenta con datos atípicos muy por encima de su mediana lo que hace que su media suba por encima de su mediana. Mientras que en el caso de Lisboa, su media es apenas superior a su mediana donde se encuentra una mayor concentración."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\3362341638.py:1: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x = \"Ciudad\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Costo promedio por hospedaje 25-28 de octubre')"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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u83cuXPNsmXLzIkTJ0ydOnVM6dKlzfDhw82MGTPMddddZySZ6dOnW/Pv3bvXSDINGzY00dHRZtq0aebRRx81Xl5epkWLFubhhx821157rZkxY4a55557jMPhMLfffrtLf1999VXjcDhMx44dTXJyspk0aZKpUqWKCQoKchnrqlWrjIeHh6lXr56ZNm2aeeSRR0xgYKCpW7euqVy5sssyJZkxY8ZYz7/99lvj5+dnwsPDzfjx483TTz9tqlatapxOp9m0adM512f+GGNiYkyVKlXMpEmTzLhx40y5cuVMhQoVTEpKilX3Ql+3MWPGGEkmOjradO/e3cyePdvMmjXrrH2YN2+ekWQaNWpk2rVrZ5KTk839999vPD09zc033+xSN3/ZcXFxJjk52SQlJRlPT0/TrFkzk52dbYwxJisry1StWtVERESYCRMmmJdeesmMGzfONGvWzOzbt89lPdarV88EBwebJ554wkyaNMlUrlzZ+Pj4mB07dlj1UlJSzDXXXGMiIyPNE088YebMmWNuvPFGI8k8++yzVr0TJ06YmjVrGm9vb/Pggw+a6dOnmyZNmpj69esbSeaTTz6x6t59992mc+fO5qmnnjJz5841gwcPNp6enqZ3796Fjvd0EyZMMA6Hw/Tt29fMnj3beh2qVKli/vzzz7Ou57PJy8szFStWNB06dHApHzhwoHE4HMbX19dIMmXLljXDhg0zx48fv+g2ztdW3759jaenp5kxY4bZu3ev2blzpxk2bJjx8fExGzZsOO8yW7dubTw8PMywYcNMcnKyadeunbXe582bZ9X99ttvTWBgoImOjjaTJk0yM2fONK1btzYOh8O88847522nXbt2xuFwmDvuuMPMnDnTdOvWzUgy9913n0vdsWPHGknm2muvNVOmTDHPPfec+fe//20eeughY4wx7777rrnmmmtM7dq1re3j6tWrjTGFv+bG/O99cvp7rXLlyqZmzZomKCjIjBo1ykybNs3ExMQYDw8Pa3mnzxsdHW3atGljkpOTzdNPP22MufBtlJ0Rdq5yx44dM5JM9+7dL6j+N998YySZO+64w6V85MiRRpL5+OOPjTF/v1Elma1bt551WUeOHCnwoZyvYcOGJiQkxPzxxx9W2fbt242Hh4cZMGDAOfuYH3YqVqxo0tPTrfK3337bSDLPPfecVdamTRsjyTz//PMuy5g+fbqRZF5//XWrLDs728TGxhp/f39ruflBoEKFCiYtLc2qO3r0aCPJNGjQwJw6dcoqv+WWW4yXl5c5efKkMcaY48ePm6CgIDNkyBCX9lNSUkxgYKBLecOGDU14eLhLO6tXrzaSzht2evToYby8vMxPP/1klR06dMiUKVPGtG7d+uwr87Qx+vj4mF9++cUq37x5s5Fkhg8f7tLHC3nd8jfWt9xyyznbzpe/IY6LizN5eXlW+fDhw42np6e1Tg4fPmy8vLxMhw4dTG5urlVv5syZRpJ55ZVXjDHGfP3110aSWbx48TnblWQkmS+//NIq279/v/H29jY9e/a0ygYPHmzCw8PN77//7jJ/v379TGBgoBWw8/+v3n77batOZmamiYqKKhB2Tg/l+SZOnGgcDofZv3+/VXbmB9++ffuMp6enefLJJ13m3bFjhylVqlSB8gvx2muvGUnm5ZdfdikfNWqUeeihh8xbb71l3njjDeuLUMuWLV3+74uirdTUVNO+fXvrNZFkgoODzxt0jDFm2bJlRpKZPHmyVZaTk2N9gTk97LRv397ExMRY71Fj/g4x1157ralRo8YFtTNhwgSX8t69exuHw2F+/PFHY4wxe/bsMR4eHqZnz54u/6f5beWrW7euadOmTYF2LjbsSDJLly61yo4dO2bCw8NNo0aNCszbqlUrk5OTY5VfzDbKzgg7V7mDBw8aSebWW2+9oPpPPfWUkWS+//57l/LffvvNSDL333+/MeZ/gWPMmDHWt+kznS3sHDp0yEgyDz74YIF54uPjTXBw8Dn7mN/26NGjXcrz8vJMeHi4iY+Pt8ratGljnE6nycrKcqnboUMHExYWVmBD9MYbbxhJ5r333jPG/C8IDBs2zKVe/kZvypQpLuX5H3b5oeOdd96xQuKRI0dcHh06dDBRUVEu62TUqFEFxhsdHX3OsJOTk2N8fX0L7AExxpg777zTeHh4mGPHjhWYli9/jIUFk+bNm5tatWq59PFCXrf8jfX69evP2u7p8jfEp4cEY/63/vL3CC5atMhIMh9++KFLvaysLBMQEGB69epljDHm559/tkJ7ZmbmWduVZGJjYwuU9+3b1/j6+pqcnByTl5dngoKCzNChQwu8hvn9/u9//2uM+fv/Kjw83OUDzRhjJk+eXCDsnC4jI8McOXLErF+/3kgyy5Yts6ad+cE3bdo043A4zJ49ewr0p06dOiYuLu6s4y3Mzp07TUBAgImNjXX5EDybJ5980kgyb7zxxkW1c762jh8/boYNG2YGDhxoFi9ebF555RUTExNjwsLCzJ49e8653KFDh5pSpUoV2OOU/wUoP+z88ccfxuFwmPHjxxdYd+PGjTOSXAJ/Ye14enq6fMkyxpiNGzcaSSY5OdkYY8yUKVOMJPP111+fs99FFXYiIiIK/M899NBDRpL57bffXOZdsGCBS70L3UbZHefsXOUCAgIkScePH7+g+vv375eHh4eioqJcysPCwhQUFKT9+/dLktq0aaNevXpp3LhxCg4OVvfu3TVv3rxCz00orA1JqlWrVoFpderU0e+//67MzMzzLqdGjRouzx0Oh6Kiogocz65YsWKB8wb279+vGjVqyMPD9V+8Tp06Ln3MV6lSJZfn+VejREZGFlr+559/Svr7vBFJateunSpUqODyWL16tQ4fPuzS3pljkgpfT6c7cuSITpw4cdb1mZeXd0HnchTWds2aNa31eSmvW9WqVc/b7unOXM9ly5aV9L/1ebY+eHl5qVq1atb0qlWrasSIEXrppZcUHBys+Ph4zZo1y+V8nXxnG/eJEyd05MgRHTlyRGlpaXrhhRcKvIa33367JLm8jlFRUQXOtyhsnR04cEAJCQkqV66c/P39VaFCBbVp00aSCu1nvj179sgYoxo1ahToz86dO62+XIiUlBR16dJFgYGBWrJkiTw9Pc87z/Dhw+Xh4aG1a9dK+vt8npSUFJdHdnb2RbfVp08fHThwQPPnz1fv3r11++2369NPP1V2drYeeeSRc/Zp//79Cg8Pl7+/v0v5mev9xx9/lDFGjz32WIF1N2bMGEk65/rbv3+/IiIiVKZMGZfyM7cbP/30kzw8PBQdHX3OfheVwv7natasKUkFtodnvicvdBtld1yNdZULCAhQREREoSeansv5bmLmcDi0ZMkSbdq0Se+9955WrVqlQYMG6ZlnntGmTZsKbHTc6UJObjyfs30InK3c/P+TFfPy8iRJr732msLCwgrUs/vl4xe77s+3Pi/GM888o4SEBC1fvlyrV6/WPffco4kTJ2rTpk0uJ2aeT/5reOutt2rgwIGF1qlfv/5F9S03N1c33HCDjh49qoceeki1a9eWn5+ffv31VyUkJFhtnq0/DodDH330UaHr60Lfe8eOHVOn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mzaVJCUnJ6tz586aOnWqIiIi3DM4AABQIrh1z861116rdevWaffu3ZKk7du367///a86deokSdq7d69SUlIUFxdnzRMYGKjmzZtr48aNkqSNGzcqKCjICjqSFBcXJw8PD23evLnQdrOyspSenu7yAAAA9uTWPTujRo1Senq6ateuLU9PT+Xm5urJJ59U//79JUkpKSmSpNDQUJf5QkNDrWkpKSkKCQlxmV6qVCmVK1fOqnOmiRMnaty4cUU9HAAAUAK5dc/O22+/rYULF2rRokX66quvtGDBAk2dOlULFiwo1nZHjx6tY8eOWY+DBw8Wa3sAAMB93Lpn54EHHtCoUaPUr18/SVJMTIz279+viRMnauDAgQoLC5MkpaamKjw83JovNTVVDRs2lCSFhYXp8OHDLsvNycnR0aNHrfnP5HQ65XQ6i2FEAACgpHHrnp0TJ07Iw8O1C56ensrLy5MkVa1aVWFhYVq3bp01PT09XZs3b1ZsbKwkKTY2Vmlpadq2bZtV5+OPP1ZeXp6aN29+BUYBAABKMrfu2enWrZuefPJJVapUSXXr1tXXX3+tadOmadCgQZIkh8Oh++67TxMmTFCNGjVUtWpVPfbYY4qIiFCPHj0kSXXq1FHHjh01ZMgQPf/88zp16pSSkpLUr18/rsQCAADuDTvJycl67LHHNGzYMB0+fFgRERG688479fjjj1t1HnzwQWVmZmro0KFKS0tTq1attHLlSnl7e1t1Fi5cqKSkJLVv314eHh7q1auXZsyY4Y4hAQCAEsZhTr9d8T9Uenq6AgMDdezYMQUEBLi7OyhGGRkZ1j2bJGn58uXy9/d3Y48AAJfqQj+/+W0sAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga4QdAABga6Xc3YF/iuvuHO/uLkCSck/J67Snne6bLHmWdlt3IH0+9zF3dwGAzbFnBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2BphBwAA2Fopd3cAAICiYIxRZmam9dzPz08Oh8ONPUJJQdgBANhCZmamunfvbj1fvny5/P393dgjlBQcxgIAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALZG2AEAALbm9rDz66+/6tZbb1X58uXl4+OjmJgYffnll9Z0Y4wef/xxhYeHy8fHR3FxcdqzZ4/LMo4ePar+/fsrICBAQUFBGjx4sDIyMq70UAAAQAnk1rDz559/qmXLlipdurQ++ugjff/993rmmWdUtmxZq87kyZM1Y8YMPf/889q8ebP8/PwUHx+vkydPWnX69++v7777TmvWrNH777+vzz77TEOHDnXHkAAAQAlTyp2NT5o0SZGRkZo3b55VVrVqVetvY4ymT5+uRx99VN27d5ckvfrqqwoNDdWyZcvUr18/7dy5UytXrtTWrVvVtGlTSVJycrI6d+6sqVOnKiIi4soOCgAAlChu3bOzYsUKNW3aVH369FFISIgaNWqkF1980Zq+d+9epaSkKC4uzioLDAxU8+bNtXHjRknSxo0bFRQUZAUdSYqLi5OHh4c2b95caLtZWVlKT093eQAAAHtya9j5+eefNWfOHNWoUUOrVq3SXXfdpXvuuUcLFiyQJKWkpEiSQkNDXeYLDQ21pqWkpCgkJMRleqlSpVSuXDmrzpkmTpyowMBA6xEZGVnUQwMAACWEW8NOXl6eGjdurKeeekqNGjXS0KFDNWTIED3//PPF2u7o0aN17Ngx63Hw4MFibQ8AALiPW8NOeHi4oqOjXcrq1KmjAwcOSJLCwsIkSampqS51UlNTrWlhYWE6fPiwy/ScnBwdPXrUqnMmp9OpgIAAlwcAALAnt4adli1bateuXS5lu3fvVuXKlSX9fbJyWFiY1q1bZ01PT0/X5s2bFRsbK0mKjY1VWlqatm3bZtX5+OOPlZeXp+bNm1+BUQAAgJLMrVdjDR8+XNdee62eeuop3XzzzdqyZYteeOEFvfDCC5Ikh8Oh++67TxMmTFCNGjVUtWpVPfbYY4qIiFCPHj0k/b0nqGPHjtbhr1OnTikpKUn9+vXjSiwAAODesNOsWTO9++67Gj16tJ544glVrVpV06dPV//+/a06Dz74oDIzMzV06FClpaWpVatWWrlypby9va06CxcuVFJSktq3by8PDw/16tVLM2bMcMeQAABACePWsCNJXbt2VdeuXc863eFw6IknntATTzxx1jrlypXTokWLiqN7AADgKuf2n4sAAAAoToQdAABga4QdAABga4QdAABga4QdAABga4QdAABga26/9By4ojxKKbtqS5fnAAB7Y0uPfxaHQ/Is7e5eAACuIA5jAQAAWyPsAAAAWyPsAAAAW+OcHQC4TB3eHO3uLkCSycpxed5z6Tg5nHzMudPqfhPd3QVJ7NkBAAA2R9gBAAC2RtgBAAC2RtgBAAC2RtgBAAC2RtgBAAC2RtgBAAC2RtgBAAC2dll3Wzpy5Ih27dolSapVq5YqVKhQJJ0CAAAoKpe0ZyczM1ODBg1SRESEWrdurdatWysiIkKDBw/WiRMnirqPAAAAl+ySws6IESO0fv16rVixQmlpaUpLS9Py5cu1fv163X///UXdRwAAgEt2SYexli5dqiVLluj666+3yjp37iwfHx/dfPPNmjNnTlH1DwAA4LJc0p6dEydOKDQ0tEB5SEgIh7EAAECJcklhJzY2VmPGjNHJkyetsr/++kvjxo1TbGxskXUOAADgcl3SYaznnntO8fHxuuaaa9SgQQNJ0vbt2+Xt7a1Vq1YVaQcBAAAuxyWFnXr16mnPnj1auHChfvjhB0nSLbfcov79+8vHx6dIOwgAAHA5Lvk+O76+vhoyZEhR9gUAAKDIXXDYWbFihTp16qTSpUtrxYoV56x74403XnbHAAAAisIFh50ePXooJSVFISEh6tGjx1nrORwO5ebmFkXfAAAALtsFh528vLxC/wYAACjJ+CFQAABga5cUdu655x7NmDGjQPnMmTN13333XW6fAAAAiswlhZ2lS5eqZcuWBcqvvfZaLVmy5LI7BQAAUFQuKez88ccfCgwMLFAeEBCg33///bI7BQAAUFQuKexERUVp5cqVBco/+ugjVatW7bI7BQAAUFQu6aaCI0aMUFJSko4cOaJ27dpJktatW6dnnnlG06dPL8r+AQAAXJZLCjuDBg1SVlaWnnzySY0fP16SVKVKFc2ZM0cDBgwo0g4CAABcjkv+uYi77rpLd911l44cOSIfHx/5+/sXZb8AAACKxCXfZycnJ0dr167VO++8I2OMJOnQoUPKyMgoss4BAABcrkvas7N//3517NhRBw4cUFZWlm644QaVKVNGkyZNUlZWlp5//vmi7icAAMAluaQ9O/fee6+aNm2qP//8Uz4+PlZ5z549tW7duiLrHAAAwOW6pD07n3/+uTZs2CAvLy+X8ipVqujXX38tko4BAAAUhUvas5OXl1foL5v/8ssvKlOmzGV3CgAAoKhcUtjp0KGDy/10HA6HMjIyNGbMGHXu3Lmo+gYAAHDZLukw1tSpU9WxY0dFR0fr5MmT+ve//609e/YoODhYb7zxRlH3EQAA4JJdUtiJjIzU9u3b9dZbb2n79u3KyMjQ4MGD1b9/f5cTlgEAANztosPOqVOnVLt2bb3//vvq37+/+vfvXxz9AgAAKBIXfc5O6dKldfLkyeLoCwAAQJG7pBOUExMTNWnSJOXk5BR1fwAAAIrUJZ2zs3XrVq1bt06rV69WTEyM/Pz8XKa/8847RdI5AACAy3VJYScoKEi9evUq6r4AAHDpvDzlMaCxy3NAusiwk5eXpylTpmj37t3Kzs5Wu3btNHbsWK7AAgC4ncPhkJyX9B0eNndR5+w8+eSTevjhh+Xv76+KFStqxowZSkxMLK6+AQAAXLaLCjuvvvqqZs+erVWrVmnZsmV67733tHDhQuXl5RVX/wAAAC7LRYWdAwcOuPwcRFxcnBwOhw4dOlTkHQMAACgKFxV2cnJy5O3t7VJWunRpnTp1qkg7BQAAUFQu6kwuY4wSEhLkdDqtspMnT+o///mPy+XnXHoOAABKiosKOwMHDixQduuttxZZZwAAAIraRYWdefPmFVc/AAAAisUl/VwEAADA1YKwAwAAbI2wAwAAbI2wAwAAbK3EhJ2nn35aDodD9913n1V28uRJJSYmqnz58vL391evXr2UmprqMt+BAwfUpUsX+fr6KiQkRA888IBycnKucO8BAEBJVSLCztatWzV37lzVr1/fpXz48OF67733tHjxYq1fv16HDh3STTfdZE3Pzc1Vly5dlJ2drQ0bNmjBggWaP3++Hn/88Ss9BAAAUEK5PexkZGSof//+evHFF1W2bFmr/NixY3r55Zc1bdo0tWvXTk2aNNG8efO0YcMGbdq0SZK0evVqff/993r99dfVsGFDderUSePHj9esWbOUnZ3triEBAIASxO1hJzExUV26dFFcXJxL+bZt23Tq1CmX8tq1a6tSpUrauHGjJGnjxo2KiYlRaGioVSc+Pl7p6en67rvvrswAAABAiXZRNxUsam+++aa++uorbd26tcC0lJQUeXl5KSgoyKU8NDRUKSkpVp3Tg07+9PxpZ5OVlaWsrCzreXp6+qUOAQAAlHBu27Nz8OBB3XvvvVq4cGGBHxctbhMnTlRgYKD1iIyMvKLtAwCAK8dtYWfbtm06fPiwGjdurFKlSqlUqVJav369ZsyYoVKlSik0NFTZ2dlKS0tzmS81NVVhYWGSpLCwsAJXZ+U/z69TmNGjR+vYsWPW4+DBg0U7OAAAUGK4Ley0b99eO3bs0DfffGM9mjZtqv79+1t/ly5dWuvWrbPm2bVrlw4cOKDY2FhJUmxsrHbs2KHDhw9bddasWaOAgABFR0eftW2n06mAgACXBwAAsCe3nbNTpkwZ1atXz6XMz89P5cuXt8oHDx6sESNGqFy5cgoICNDdd9+t2NhYtWjRQpLUoUMHRUdH67bbbtPkyZOVkpKiRx99VImJiXI6nVd8TAAAoORx6wnK5/Pss8/Kw8NDvXr1UlZWluLj4zV79mxruqenp95//33dddddio2NlZ+fnwYOHKgnnnjCjb0GAAAlSYkKO59++qnLc29vb82aNUuzZs066zyVK1fWhx9+WMw9AwAAVyu332cHAACgOBF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACArRF2AACA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/m/fvl0ZGRkuy5Okv/76Sz/99NM5xw7g/BISEnTDDTeoVq1a6tixo7p27aoOHTq41ImNjS3w/JtvvpH09/ajQYMGLtuWli1bKi8vT7t27bJ+S7Fu3bouh9DDw8O1Y8eOYhoVrhTCDkoEPz8/l0NCl8PHx0cOh8N6npGRIU9PT23btq3AeUD+/v7W36VLl3aZ5nA4ZP7/r6n4+Pics82MjAyFh4e7nAeULygo6CJHAOBMjRs31t69e/XRRx9p7dq1uvnmmxUXF1fgvJzLVdh2IC8vr0jbwJXHOTu4atSpU0c5OTnavHmzVfbHH39o165dio6OPut8jRo1Um5urg4fPqyoqCiXx4Ve7VGmTBlVqVJF69atK3R648aNlZKSolKlShVoIzg4+OIGCqBQAQEB6tu3r1588UW99dZbWrp0qcs5cZs2bXKpv2nTJtWpU0fS39uP7du3KzMz05r+xRdfyMPDQ7Vq1boyA4DbsGcHV40aNWqoe/fuGjJkiObOnasyZcpo1KhRqlixorp3737W+WrWrKn+/ftrwIABeuaZZ9SoUSMdOXJE69atU/369dWlS5cLan/s2LH6z3/+o5CQEHXq1EnHjx/XF198obvvvltxcXGKjY1Vjx49NHnyZNWsWVOHDh3SBx98oJ49e6pp06ZFtRoA2zl27Jh1uCnfmYeEp02bpvDwcDVq1EgeHh5avHixwsLCXPacLl68WE2bNlWrVq20cOFCbdmyRS+//LIkqX///hozZowGDhyosWPH6siRI7r77rt12223WYewYF+EHVxV5s2bp3vvvVddu3ZVdna2WrdurQ8//LDArufC5pswYYLuv/9+/frrrwoODlaLFi3UtWvXC2574MCBOnnypJ599lmNHDlSwcHB6t27t6S/d3V/+OGHeuSRR3T77bfryJEjCgsLU+vWrdmQAufx6aefqlGjRi5lgwcPdnlepkwZTZ48WXv27JGnp6eaNWumDz/80OUeWuPGjdObb76pYcOGKTw8XG+88Ya119fX11erVq3Svffeq2bNmsnX11e9evXStGnTin+AcDuHyT8pAQAAwIY4ZwcAANgaYQcAANgaYQcAANgaYQcAANgaYQcAANgaYQcAANgaYQcAANgaYQfAVcPhcGjZsmWXtYz58+cXye+VValSRdOnT7/s5QAofoQdACVGSkqK7r77blWrVk1Op1ORkZHq1q2b9Ztkv/32mzp16uTmXgK42vBzEQBKhH379qlly5YKCgrSlClTFBMTo1OnTmnVqlVKTEzUDz/8cME/3AoAp2PPDoASYdiwYXI4HNqyZYt69eqlmjVrqm7duhoxYoT1a9anH8b69NNP5XA4lJaWZi3jm2++kcPh0L59+6yy+fPnq1KlSvL19VXPnj31xx9/uLT7008/qXv37goNDZW/v7+aNWumtWvXutQ5fPiwunXrJh8fH1WtWlULFy4slnUAoHgQdgC43dGjR7Vy5UolJibKz8+vwPRLPcdm8+bNGjx4sJKSkvTNN9+obdu2mjBhgkudjIwMde7cWevWrdPXX3+tjh07qlu3bjpw4IBVJyEhQQcPHtQnn3yiJUuWaPbs2Tp8+PAl9QnAlcdhLABu9+OPP8oYo9q1axfpcp977jl17NhRDz74oCSpZs2a2rBhg1auXGnVadCggRo0aGA9Hz9+vN59912tWLFCSUlJ2r17tz766CNt2bJFzZo1kyS9/PLLqlOnTpH2FUDxYc8OALczxhTLcnfu3KnmzZu7lMXGxro8z8jI0MiRI1WnTh0FBQXJ399fO3futPbs7Ny5U6VKlVKTJk2seWrXrl0kV3QBuDLYswPA7WrUqCGHw6Effvjhgufx8Pj7u9rpQenUqVMX3fbIkSO1Zs0aTZ06VVFRUfLx8VHv3r2VnZ190csCUDKxZweA25UrV07x8fGaNWuWMjMzC0w//STkfBUqVJD09+Xo+b755huXOnXq1NHmzZtdyvJPds73xRdfKCEhQT179lRMTIzCwsJcTnCuXbu2cnJytG3bNqts165dhfYJQMlE2AFQIsyaNUu5ubn617/+paVLl2rPnj3auXOnZsyYUeDQkyRFRUUpMjJSY8eO1Z49e/TBBx/omWeecalzzz33aOXKlZo6dar27NmjmTNnupyvI/29V+mdd97RN998o+3bt+vf//638vLyrOm1atVSx44ddeedd2rz5s3atm2b7rjjDvn4+BTPigBQ5Ag7AEqEatWq6auvvlLbtm11//33q169errhhhu0bt06zZkzp0D90qVL64033tAPP/yg+vXra9KkSQWutGrRooVefPFFPffcc2rQoIFWr16tRx991KXOtGnTVLZsWV177bXq1q2b4uPj1bhxY5c68+bNU0REhNq0aaObbrpJQ4cOVUhISNGvBADFwmGK68xAAACAEoA9OwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNYIOwAAwNb+H0WZz1UqRZGXAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = \"Ciudad\", \n",
    "              y = 'Precio',\n",
    "              data = df_florencia_lisboa, \n",
    "              palette='viridis')\n",
    "plt.title('Costo promedio por hospedaje 25-28 de octubre')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# anotaciones"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Anotaciones"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Excursiones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\2626008194.py:1: UserWarning: \n",
      "The palette list has fewer values (2) than needed (10) and will cycle, which may produce an uninterpretable plot.\n",
      "  sns.countplot(x = \"Tipo de excursión\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],\n",
       " [Text(0, 0, 'Excursiones de un día'),\n",
       "  Text(1, 0, 'Museos y Monumentos'),\n",
       "  Text(2, 0, 'Tours a pie'),\n",
       "  Text(3, 0, 'Free Tours'),\n",
       "  Text(4, 0, 'Tours en Bus turístico'),\n",
       "  Text(5, 0, 'Experiencias Gastronómicas'),\n",
       "  Text(6, 0, 'Visitas Guiadas'),\n",
       "  Text(7, 0, 'Tours en Bicicleta'),\n",
       "  Text(8, 0, 'Espectáculos'),\n",
       "  Text(9, 0, 'Traslados Aeropuertos')])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkYAAAJXCAYAAAB2V5tSAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAC3vUlEQVR4nOzddVwU+f8H8PeCgoqUioGiooKKgAkYiNgoYncjxtme7dnddXacnl1nnoXd3d3dgYKK9Ov3B7vzY0X9Ki7swr2ejwePO2dmd94zO/Gez3xCBQBCRERERGKk7wCIiIiIDAUTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyKSBw8eiEqlkr///lvfoaQYKW2fqlQqGTZsmL7DIEp0TIyIftDff/8tKpXqm38nTpzQd4iURFq3bv3N42Dnzp36Do+IfkEqfQdAlNyMGDFC7O3t403Ply+fHqLRjVy5csnnz58lderU+g4l2TA1NZWFCxfGm164cGE9RJP4Pn/+LKlS8ZZBKR+PcqKfVK1aNSlRooS+w/ifAEhYWJikTZv2fy6rUqkkTZo0SRBVypEqVSpp3rx5kq3v06dPYmZmlmTr+xKPD/qv4Ks0Ih0bOnSoGBkZyd69e7Wmt2/fXkxMTOTixYvKtKdPn0pAQIDY2tqKqamp2NvbS8eOHSUiIkJERIYNGyYqlSreOjSv9R48eKBMy507t9SoUUMCAwOlRIkSkjZtWpk3b56IiOzevVs8PT3FyspK0qdPL/nz55c//vhD+ey36sPs27dPypYtK2ZmZmJlZSW1atWS69evay2jifHOnTvSunVrsbKyEktLS/H395fQ0NB4sS9fvlyKFy8uadOmlQwZMkjjxo3l8ePHWsvcvn1b6tWrJ1mzZpU0adJIjhw5pHHjxhIcHPydPR/r5MmT4uPjI5aWlpIuXTopV66cHD169Jdi1qWf2afXrl2Tpk2birW1tXh6eirzf2Qfent7i7Ozs1y7dk3Kly8v6dKlk+zZs8uECRPixRQWFibDhg0TR0dHSZMmjWTLlk3q1q0rd+/eVZb5so7Rw4cPpVOnTpI/f35JmzatZMyYURo0aKB1TBIlRywxIvpJwcHB8ubNG61pKpVKMmbMKCIigwYNkn///VcCAgLk8uXLYm5uLoGBgbJgwQIZOXKk8qrl2bNn4u7uLu/fv5f27dtLgQIF5OnTp/LPP/9IaGiomJiY/HRsN2/elCZNmkiHDh2kXbt2kj9/frl69arUqFFDXF1dZcSIEWJqaip37tyJlyx8ac+ePVKtWjXJkyePDBs2TD5//iwzZsyQMmXKyLlz5yR37txayzds2FDs7e1l7Nixcu7cOVm4cKFkzpxZxo8frywzevRoGTx4sDRs2FDatm0rr1+/lhkzZoiXl5ecP39erKysJCIiQqpWrSrh4eHStWtXyZo1qzx9+lS2bt0q79+/F0tLy2/GvG/fPqlWrZoUL15cSVAXL14sFSpUkMOHD4u7u/tPx/w9Xx4HqVOn/m58P7tPGzRoIA4ODjJmzBgB8MP7UOPdu3fi4+MjdevWlYYNG8o///wj/fr1ExcXF6lWrZqIiERHR0uNGjVk79690rhxY+nevbt8+PBBdu/eLVeuXJG8efN+dVtOnz4tx44dk8aNG0uOHDnkwYMHMmfOHPH29pZr165JunTpfmgfEhkcENEPWbx4MUTkq3+mpqZay16+fBkmJiZo27Yt3r17h+zZs6NEiRKIjIxUlmnZsiWMjIxw+vTpeOuKiYkBAAwdOhRfO001sdy/f1+ZlitXLogIdu7cqbXs1KlTISJ4/fr1N7ft/v37EBEsXrxYmVakSBFkzpwZb9++VaZdvHgRRkZGaNmypTJNE2ObNm20vrNOnTrImDGj8u8HDx7A2NgYo0eP1lru8uXLSJUqlTL9/PnzEBGsW7fum/F+TUxMDBwcHFC1alVl/wFAaGgo7O3tUbly5Z+O+VtatWr11eOgXLlyyjK62KdNmjTRWu+P7kMAKFeuHEQES5cuVaaFh4cja9asqFevnjJt0aJFEBFMmTIl3nbG3Y8igqFDhyr/Dg0Njbf88ePH462TKLnhqzSinzRr1izZvXu31t+OHTu0lnF2dpbhw4fLwoULpWrVqvLmzRtZsmSJUnk1JiZGNm3aJH5+fl+tr/S112c/wt7eXqpWrao1TVOCsHnzZomJifmh73n+/LlcuHBBWrduLRkyZFCmu7q6SuXKlWX79u3xPvPbb79p/bts2bLy9u1bCQkJERGRDRs2SExMjDRs2FDevHmj/GXNmlUcHBxk//79IiJKiUtgYOBPvda6cOGC3L59W5o2bSpv375Vvv/Tp09SsWJFOXToULzt/18xf0+aNGniHQeTJ0/+5vK62Kc/ug810qdPr1UPysTERNzd3eXevXvKtPXr10umTJmka9eu8db/veMwbt21yMhIefv2reTLl0+srKzk3Llz3/wckaHjqzSin+Tu7v5Dla/79Okjq1evllOnTsmYMWPEyclJmff69WsJCQkRZ2dnncb2tdZyjRo1koULF0rbtm2lf//+UrFiRalbt67Ur19fjIy+/mz08OFDERHJnz9/vHkFCxaUwMDAeJWBc+bMqbWctbW1iMS+zrGwsJDbt28LAHFwcPjqOjUt4uzt7aVnz54yZcoUWbFihZQtW1Zq1qwpzZs3/+5rqtu3b4uISKtWrb65THBwsBLXj8T8PcbGxlKpUqXvLhNXQvbpl7/nj+5DjRw5csRLbqytreXSpUvKv+/evSv58+f/6RZnnz9/lrFjx8rixYvl6dOnyqs+EfmhumBEhoqJEVEiuXfvnnKzvnz5coK+41tP7NHR0V+d/rUWaGnTppVDhw7J/v37Zdu2bbJz505Zs2aNVKhQQXbt2iXGxsYJiu1L3/oezQ0zJiZGVCqV7Nix46vLpk+fXvn/yZMnS+vWrWXz5s2ya9cu6datm4wdO1ZOnDghOXLk+Op6NKVBEydOlCJFinx1mbjr+JGY9e3L3/Nn9qFI4m5f165dZfHixdKjRw8pVaqUWFpaikqlksaNG/9wySSRIWJiRJQIYmJipHXr1mJhYSE9evSQMWPGSP369aVu3boiImJjYyMWFhZy5cqV736PpgTj/fv3WpVqNaUPP8rIyEgqVqwoFStWlClTpsiYMWNk4MCBsn///q+WeuTKlUtEYitzf+nGjRuSKVOmn246njdvXgEg9vb24ujo+D+Xd3FxERcXFxk0aJAcO3ZMypQpI3PnzpVRo0Z98/tFRCwsLH6qJCep6GKf/uw+/BF58+aVkydPSmRk5E/1Y/XPP/9Iq1attF4fhoWFyfv373USF5G+sI4RUSKYMmWKHDt2TObPny8jR46U0qVLS8eOHZVWTEZGRlK7dm35999/5cyZM/E+r3mi19zsDx06pMz79OmTLFmy5IdjCQoKijdNU6ISHh7+1c9ky5ZNihQpIkuWLNG60V25ckV27dol1atX/+H1a9StW1eMjY1l+PDh8UosAMjbt29FRCQkJESioqK05ru4uIiRkdE34xURKV68uOTNm1cmTZokHz9+jDf/9evXPx2zLulin/7oPvwZ9erVkzdv3sjMmTPjzfteyZKxsXG8+TNmzPhmaSZRcsESI6KftGPHDrlx40a86aVLl5Y8efLI9evXZfDgwdK6dWvx8/MTkdh+h4oUKSKdOnWStWvXiojImDFjZNeuXVKuXDlp3769FCxYUJ4/fy7r1q2TI0eOiJWVlVSpUkVy5swpAQEB0qdPHzE2NpZFixaJjY2NPHr06IfiHTFihBw6dEh8fX0lV65c8urVK5k9e7bkyJFDq2+cL02cOFGqVasmpUqVkoCAAKVpuaWlZYLGzMqbN6+MGjVKBgwYIA8ePJDatWuLubm53L9/XzZu3Cjt27eX3r17y759+6RLly7SoEEDcXR0lKioKFm2bJkYGxtLvXr1vvn9RkZGsnDhQqlWrZoUKlRI/P39JXv27PL06VPZv3+/WFhYyL///vvTcevSr+7TH92HP6Nly5aydOlS6dmzp5w6dUrKli0rnz59kj179kinTp2kVq1aX/1cjRo1ZNmyZWJpaSlOTk5y/Phx2bNnj9JtBVGypYeWcETJ0vea64u6WXZUVBTc3NyQI0cOvH//Xuvz06dPh4hgzZo1yrSHDx+iZcuWsLGxgampKfLkyYPOnTsjPDxcWebs2bPw8PCAiYkJcubMiSlTpnyzub6vr2+8uPfu3YtatWrB1tYWJiYmsLW1RZMmTXDr1i1lma81LQeAPXv2oEyZMkibNi0sLCzg5+eHa9euaS2jaVr+ZXcAX4sRANavXw9PT0+YmZnBzMwMBQoUQOfOnXHz5k0AwL1799CmTRvkzZsXadKkQYYMGVC+fHns2bPn2z9OHOfPn0fdunWRMWNGmJqaIleuXGjYsCH27t2b4Ji/1KpVK5iZmX13mcTYpxr/ax8Csc31CxUq9NXYc+XKpTUtNDQUAwcOhL29PVKnTo2sWbOifv36uHv3rrKMfNFc/927d/D390emTJmQPn16VK1aFTdu3ECuXLnQqlWr7+4bIkOmAgykliERERGRnrGOEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJL8R08xsTEyLNnz8Tc3DzBI5YTERFR0gIgHz58EFtb228OeJ0YUnxi9OzZM7Gzs9N3GERERJQAjx8//ubg0YkhxSdG5ubmIhK7Yy0sLPQcDREREf2IkJAQsbOzU+7jSSXFJ0aa12cWFhZMjIiIiJKZpK4Gw8rXRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjU9JoYHTp0SPz8/MTW1lZUKpVs2rRJmRcZGSn9+vUTFxcXMTMzE1tbW2nZsqU8e/ZMfwETERFRiqbXxOjTp09SuHBhmTVrVrx5oaGhcu7cORk8eLCcO3dONmzYIDdv3pSaNWvqIVIiIiL6L1ABgL6DEIkdJG7jxo1Su3btby5z+vRpcXd3l4cPH0rOnDl/6HtDQkLE0tJSgoODOYgsERFRMqGv+3eyqmMUHBwsKpVKrKys9B0KERERpUCp9B3AjwoLC5N+/fpJkyZNvps5hoeHS3h4uPLvkJCQpAiPiIiIUoBkkRhFRkZKw4YNBYDMmTPnu8uOHTtWhg8f/j+/M+zOKV2FlyjS5HPXdwhERET/OQb/Kk2TFD18+FB27979P98zDhgwQIKDg5W/x48fJ1GkRERElNwZdImRJim6ffu27N+/XzJmzPg/P2NqaiqmpqZJEB0RERGlNHpNjD5+/Ch37txR/n3//n25cOGCZMiQQbJlyyb169eXc+fOydatWyU6OlpevHghIiIZMmQQExMTfYVNREREKZRem+sfOHBAypcvH296q1atZNiwYWJvb//Vz+3fv1+8vb1/aB3fau7HOkZERESGS1/N9fVaYuTt7S3fy8sMpIslIiIi+o8w+MrXREREREmFiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpKbXxOjQoUPi5+cntra2olKpZNOmTVrzAciQIUMkW7ZskjZtWqlUqZLcvn1bP8ESERFRiqfXxOjTp09SuHBhmTVr1lfnT5gwQf7880+ZO3eunDx5UszMzKRq1aoSFhaWxJESERHRf0Eqfa68WrVqUq1ata/OAyDTpk2TQYMGSa1atUREZOnSpZIlSxbZtGmTNG7cOClDJSIiov8Ag61jdP/+fXnx4oVUqlRJmWZpaSkeHh5y/Pjxb34uPDxcQkJCtP6IiIiIfoTBJkYvXrwQEZEsWbJoTc+SJYsy72vGjh0rlpaWyp+dnV2ixklEREQph8EmRgk1YMAACQ4OVv4eP36s75CIiIgomTDYxChr1qwiIvLy5Uut6S9fvlTmfY2pqalYWFho/RERERH9CINNjOzt7SVr1qyyd+9eZVpISIicPHlSSpUqpcfIiIiIKKXSa6u0jx8/yp07d5R/379/Xy5cuCAZMmSQnDlzSo8ePWTUqFHi4OAg9vb2MnjwYLG1tZXatWvrL2giIiJKsfSaGJ05c0bKly+v/Ltnz54iItKqVSv5+++/pW/fvvLp0ydp3769vH//Xjw9PWXnzp2SJk0afYVMREREKZgKAPQdRGIKCQkRS0tLCQ4O1qpvFHbnlB6j+t/S5HPXdwhERER68637d2Iz2DpGREREREmNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpGbQiVF0dLQMHjxY7O3tJW3atJI3b14ZOXKkANB3aERERJQCpdJ3AN8zfvx4mTNnjixZskQKFSokZ86cEX9/f7G0tJRu3brpOzwiIiJKYQw6MTp27JjUqlVLfH19RUQkd+7csmrVKjl16pSeIyMiIqKUyKBfpZUuXVr27t0rt27dEhGRixcvypEjR6RatWrf/Ex4eLiEhIRo/RERERH9CIMuMerfv7+EhIRIgQIFxNjYWKKjo2X06NHSrFmzb35m7NixMnz48CSMkoiIiFIKgy4xWrt2raxYsUJWrlwp586dkyVLlsikSZNkyZIl3/zMgAEDJDg4WPl7/PhxEkZMREREyZlBlxj16dNH+vfvL40bNxYRERcXF3n48KGMHTtWWrVq9dXPmJqaiqmpaVKGSURERCmEQZcYhYaGipGRdojGxsYSExOjp4iIiIgoJTPoEiM/Pz8ZPXq05MyZUwoVKiTnz5+XKVOmSJs2bfQdGhEREaVABp0YzZgxQwYPHiydOnWSV69eia2trXTo0EGGDBmi79CIiIgoBVIhhXcjHRISIpaWlhIcHCwWFhbK9LA7ht0XUpp87voOgYiISG++df9ObAZdx4iIiIgoKTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGqpfnTBnj17/vCXTpkyJUHBEBEREenTDydG58+f1/r3uXPnJCoqSvLnzy8iIrdu3RJjY2MpXry4biMkIiIiSiI/nBjt379f+f8pU6aIubm5LFmyRKytrUVE5N27d+Lv7y9ly5bVfZRERERESUAFAD/7oezZs8uuXbukUKFCWtOvXLkiVapUkWfPnukswF8VEhIilpaWEhwcLBYWFsr0sDun9BjV/5Ymn7u+QyAiItKbb92/E1uCKl+HhITI69ev401//fq1fPjw4ZeDIiIiItKHBCVGderUEX9/f9mwYYM8efJEnjx5IuvXr5eAgACpW7eurmMkIiIiShI/XMcorrlz50rv3r2ladOmEhkZGftFqVJJQECATJw4UacBEhERESWVBNUx0vj06ZPcvXtXRETy5s0rZmZmOgtMV1jHiIiIKPnRVx2jBJUYaZiZmYmrq6uuYiEiIiLSqwQnRmfOnJG1a9fKo0ePJCIiQmvehg0bfjkwIiIioqSWoMrXq1evltKlS8v169dl48aNEhkZKVevXpV9+/aJpaWlrmMkIiIiShIJSozGjBkjU6dOlX///VdMTExk+vTpcuPGDWnYsKHkzJlT1zESERERJYkEJUZ3794VX19fERExMTGRT58+iUqlkt9//13mz5+v0wCJiIiIkkqCEiNra2ulI8fs2bPLlStXRETk/fv3EhoaqrvoiIiIiJJQgipfe3l5ye7du8XFxUUaNGgg3bt3l3379snu3bulYsWKuo6RiIiIKEkkKDGaOXOmhIWFiYjIwIEDJXXq1HLs2DGpV6+eDBo0SKcBEhERESWVBCVGGTJkUP7fyMhI+vfvr7OAiIiIiPTlhxOjkJCQH/7SpOyhkoiIiEhXfjgxsrKyEpVK9UPLRkdHJzggIiIiIn354cRo//79yv8/ePBA+vfvL61bt5ZSpUqJiMjx48dlyZIlMnbsWN1HSURERJQEEjSIbMWKFaVt27bSpEkTrekrV66U+fPny4EDB3QV3y/jILJERETJj74GkU1QP0bHjx+XEiVKxJteokQJOXXKsBMOIiIiom9JUGJkZ2cnCxYsiDd94cKFYmdn98tBEREREelDgprrT506VerVqyc7duwQDw8PERE5deqU3L59W9avX6/TAImIiIiSSoJKjKpXry63bt0SPz8/CQoKkqCgIPHz85Nbt25J9erVdR0jERERUZJIUImRSOzrtDFjxugyFiIiIiK9+uHE6NKlS+Ls7CxGRkZy6dKl7y7r6ur6y4ERERERJbUfToyKFCkiL168kMyZM0uRIkVEpVLJ11r6q1QqdvBIREREydIPJ0b3798XGxsb5f+JiIiIUpofToxy5cql/P/Dhw+ldOnSkiqV9sejoqLk2LFjWssSERERJRcJapVWvnx5CQoKijc9ODhYypcv/8tBEREREelDghIjAF8dUPbt27diZmb2y0ERERER6cNPNdevW7euiMRWsG7durWYmpoq86Kjo+XSpUtSunRpnQb49OlT6devn+zYsUNCQ0MlX758snjx4q8OSUJERET0K34qMbK0tBSR2BIjc3NzSZs2rTLPxMRESpYsKe3atdNZcO/evZMyZcpI+fLlZceOHWJjYyO3b98Wa2trna2DiIiISOOnEqPFixeLiEju3Lmld+/eif7abPz48WJnZ6esV0TE3t4+UddJRERE/10JqmM0dOjQJKlLtGXLFilRooQ0aNBAMmfOLEWLFv3q4LVEREREupCgxOjly5fSokULsbW1lVSpUomxsbHWn67cu3dP5syZIw4ODhIYGCgdO3aUbt26yZIlS775mfDwcAkJCdH6IyIiIvoRCRorrXXr1vLo0SMZPHiwZMuW7ast1HQhJiZGSpQooYzJVrRoUbly5YrMnTtXWrVq9dXPjB07VoYPH54o8RiaNnOb6juE71r020p9h0BERPRTEpQYHTlyRA4fPixFihTRcTjasmXLJk5OTlrTChYsKOvXr//mZwYMGCA9e/ZU/h0SEiJ2dnaJFiMRERGlHAlKjOzs7L46TpqulSlTRm7evKk17datW9/tWdvU1FSrGwEiIiKiH5WgOkbTpk2T/v37y4MHD3Qcjrbff/9dTpw4IWPGjJE7d+7IypUrZf78+dK5c+dEXS8RERH9NyWoxKhRo0YSGhoqefPmlXTp0knq1Km15n9tuJCEcHNzk40bN8qAAQNkxIgRYm9vL9OmTZNmzZrp5PuJiIiI4kpQYjRt2jQdh/FtNWrUkBo1aiTZ+oiIiOi/K0GJ0bdahBERERElZwlKjOIKCwuTiIgIrWkWFha/+rVERERESS5Bla8/ffokXbp0kcyZM4uZmZlYW1tr/RERERElRwlKjPr27Sv79u2TOXPmiKmpqSxcuFCGDx8utra2snTpUl3HSERERJQkEvQq7d9//5WlS5eKt7e3+Pv7S9myZSVfvnySK1cuWbFiBVuNERERUbKUoBKjoKAgyZMnj4jE1ifSNM/39PSUQ4cO6S46IiIioiSUoMQoT548cv/+fRERKVCggKxdu1ZEYkuSrKysdBYcERERUVJKUGLk7+8vFy9eFBGR/v37y6xZsyRNmjTSo0cP6dOnj04DJCIiIkoqCapj9Pvvvyv/X6lSJblx44acPXtWHBwcxMXFRWfBERERESWlnyox2rdvnzg5OUlISIjW9Fy5cknFihWlcePGcvjwYZ0GSERERJRUfioxmjZtmrRr1+6rHThaWlpKhw4dZMqUKToLjoiIiCgp/VRidPHiRfHx8fnm/CpVqsjZs2d/OSgiIiIiffipxOjly5eSOnXqb85PlSqVvH79+peDIiIiItKHn0qMsmfPLleuXPnm/EuXLkm2bNl+OSgiIiIiffipxKh69eoyePBgCQsLizfv8+fPMnToUKlRo4bOgiMiIiJKSj/VXH/QoEGyYcMGcXR0lC5dukj+/PlFROTGjRsya9YsiY6OloEDByZKoERERESJ7acSoyxZssixY8ekY8eOMmDAAAEgIiIqlUqqVq0qs2bNkixZsiRKoERERESJ7ac7eMyVK5ds375d3r17J3fu3BEA4uDgINbW1okRHxEREVGSSVDP1yIi1tbW4ubmpstYiIiIiPQqQWOlEREREaVETIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpJasEqNx48aJSqWSHj166DsUIiIiSoGSTWJ0+vRpmTdvnri6uuo7FCIiIkqhkkVi9PHjR2nWrJksWLBArK2t9R0OERERpVDJIjHq3Lmz+Pr6SqVKlf7nsuHh4RISEqL1R0RERPQjUuk7gP9l9erVcu7cOTl9+vQPLT927FgZPnx4IkdFRIaszdym+g7huxb9tlLfIRDRNxh0idHjx4+le/fusmLFCkmTJs0PfWbAgAESHBys/D1+/DiRoyQiIqKUwqBLjM6ePSuvXr2SYsWKKdOio6Pl0KFDMnPmTAkPDxdjY2Otz5iamoqpqWlSh0pEREQpgEEnRhUrVpTLly9rTfP395cCBQpIv3794iVFRERERL/CoBMjc3NzcXZ21ppmZmYmGTNmjDediIiI6FcZdB0jIiIioqRk0CVGX3PgwAF9h0BEREQpFEuMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyIiIiK1VPoOgIiI4gu7c0rfIXxXmnzu+g6BKFGwxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKRm0InR2LFjxc3NTczNzSVz5sxSu3ZtuXnzpr7DIiIiohTKoBOjgwcPSufOneXEiROye/duiYyMlCpVqsinT5/0HRoRERGlQKn0HcD37Ny5U+vff//9t2TOnFnOnj0rXl5eeoqKiIiIUiqDToy+FBwcLCIiGTJk+OYy4eHhEh4ervw7JCQk0eMiIiKilCHZJEYxMTHSo0cPKVOmjDg7O39zubFjx8rw4cOTMDL6VWF3Tuk7hO9Kk89d3yEQEVESMeg6RnF17txZrly5IqtXr/7ucgMGDJDg4GDl7/Hjx0kUIRERESV3yaLEqEuXLrJ161Y5dOiQ5MiR47vLmpqaiqmpaRJFRkRERCmJQSdGAKRr166yceNGOXDggNjb2+s7JCIiIkrBDDox6ty5s6xcuVI2b94s5ubm8uLFCxERsbS0lLRp0+o5OiIiIkppDLqO0Zw5cyQ4OFi8vb0lW7Zsyt+aNWv0HRoRERGlQAZdYgRA3yEQERHRf4hBlxgRERERJSUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpMbEiIiIiEiNiRERERGRGhMjIiIiIjUmRkRERERqTIyIiIiI1JgYEREREakxMSIiIiJSY2JEREREpJZK3wEQpRRt5jbVdwjftOi3lT+0XNidU4kcya9Jk89d3yHQTzLk80IkZZwbP3pepJTfIrGxxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGpMTEiIiIiUmNiRERERKTGxIiIiIhIjYkRERERkRoTIyIiIiI1JkZEREREakyMiIiIiNSYGBERERGp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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = \"Tipo de excursión\", \n",
    "              data = excursiones_florencia, \n",
    "              palette=[\"#FFDAC1\", \"#59A14F\"], \n",
    "              hue = \"Tipo de excursión\")\n",
    "plt.title('Excursiones en Florencia')\n",
    "plt.ylabel('Cantidad')\n",
    "plt.xlabel('')\n",
    "plt.xticks(rotation=60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\4263993969.py:1: UserWarning: \n",
      "The palette list has fewer values (2) than needed (11) and will cycle, which may produce an uninterpretable plot.\n",
      "  sns.countplot(x = \"Tipo de excursión\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\n",
       " [Text(0, 0, 'Visitas Guiadas'),\n",
       "  Text(1, 0, 'Excursiones de un día'),\n",
       "  Text(2, 0, 'Pases turísticos'),\n",
       "  Text(3, 0, 'Espectáculos'),\n",
       "  Text(4, 0, 'Tours en Bus turístico'),\n",
       "  Text(5, 0, 'Tours a pie'),\n",
       "  Text(6, 0, 'Traslados Aeropuertos'),\n",
       "  Text(7, 0, 'Paseos en barco'),\n",
       "  Text(8, 0, 'Experiencias Gastronómicas'),\n",
       "  Text(9, 0, 'Tours en Bicicleta'),\n",
       "  Text(10, 0, 'Alquiler de Vehículos')])"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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J6dUnfioq7fMzc2Z+BAREaUy+mimwsbNREREZDCY+BAREZHBYOJDREREBoOJDxERERkMJj5ERERkMJj4EBERkcFg4kNEREQGg4kPERERGQwmPkRERGQwmPgQERGRwdBr4hMTEyNDhgwRW1tbMTMzEzs7Oxk1apQA0GdYRERElEbpda6uCRMmyNy5c2XZsmXi6uoqZ8+elcDAQLGwsJDu3bvrMzQiIiJKg/Sa+Bw/flzq1Kkj/v7+IiJSsGBBWb16tZw+fVqfYREREVEapdeqrjJlysj+/fvl9u3bIiJy6dIlOXbsmNSoUUOfYREREVEapdcSnwEDBkhoaKg4OzuLsbGxxMTEyJgxY6RFixaJrh8RESERERHK76GhockVKhEREaUBek181q5dKytXrpRVq1aJq6urXLx4UXr27ClWVlbSunXrBOuPGzdORowYoYdIdW/hupRVvdehkae+QyAiItI6FfTYhcra2loGDBggXbp0UZaNHj1aVqxYITdv3kywfmIlPtbW1hISEiLm5ubJErOuMPEhIiJDERoaKhYWFnq5f+u1xCc8PFyMjDSbGRkbG0tsbGyi65uamoqpqWlyhEZERERpkF4Tn4CAABkzZowUKFBAXF1d5cKFCzJlyhRp27atPsMiIiKiNEqvic/MmTNlyJAh0rlzZ3n9+rVYWVlJx44dZejQofoMi4iIiNIovSY+WbJkkWnTpsm0adP0GQYREREZCM7VRURERAaDiQ8REREZDCY+REREZDCY+BAREZHBYOJDREREBoOJDxERERkMJj5ERERkMJj4EBERkcFg4kNEREQGg4kPERERGQwmPkRERGQwmPgQERGRwWDiQ0RERAaDiQ8REREZDCY+REREZDCY+BAREZHBYOJDREREBoOJDxERERkMJj5ERERkMJj4EBERkcFg4kNEREQGg4kPERERGQwmPkRERGQwmPgQERGRwWDiQ0RERAaDiQ8REREZDCY+REREZDCY+BAREZHBYOJDREREBoOJDxERERkMJj5ERERkMJj4EBERkcFg4kNEREQGQ6+JT8GCBUWlUiX46dKliz7DIiIiojTKRJ8bP3PmjMTExCi/X716VapUqSKNGjXSY1RERESUVuk18bG0tNT4ffz48WJnZyflypXTU0RERESUlqWYNj6RkZGyYsUKadu2rahUKn2HQ0RERGmQXkt8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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = \"Tipo de excursión\", \n",
    "              data = excursiones_lisboa, \n",
    "              palette=[\"#FF6F61\", \"#92A8D1\"], \n",
    "              hue = \"Tipo de excursión\")\n",
    "plt.title('Excursiones en Lisboa')\n",
    "plt.ylabel('Cantidad')\n",
    "plt.xlabel('')\n",
    "plt.xticks(rotation=60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\3026289306.py:1: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x = \"Tipo de excursión\",\n",
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\3026289306.py:1: UserWarning: \n",
      "The palette list has fewer values (5) than needed (10) and will cycle, which may produce an uninterpretable plot.\n",
      "  sns.barplot(x = \"Tipo de excursión\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],\n",
       " [Text(0, 0, 'Excursiones de un día'),\n",
       "  Text(1, 0, 'Museos y Monumentos'),\n",
       "  Text(2, 0, 'Tours a pie'),\n",
       "  Text(3, 0, 'Free Tours'),\n",
       "  Text(4, 0, 'Tours en Bus turístico'),\n",
       "  Text(5, 0, 'Experiencias Gastronómicas'),\n",
       "  Text(6, 0, 'Visitas Guiadas'),\n",
       "  Text(7, 0, 'Tours en Bicicleta'),\n",
       "  Text(8, 0, 'Espectáculos'),\n",
       "  Text(9, 0, 'Traslados Aeropuertos')])"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk8AAAJrCAYAAAD5+ndOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAADNnElEQVR4nOzdd1gUZ9cG8LOAFKkWBFFU7A0VFRELoqKoiCV2iS3Ye0ksSey99x5jiz3W2BWNJfZeosaKWLAhICBIub8//HZeVtC4urALuX/XtZfuzDBzZndm9swzT1EBgBARERHRZzHSdwBEREREGQmTJyIiIiItMHkiIiIi0gKTJyIiIiItMHkiIiIi0gKTJyIiIiItMHkiIiIi0gKTJyIiIiItMHkiIiIi0gKTJ/rP6tixoxQoUEDfYejMn3/+KSqVSv78809lWmbbx09ZsWKFqFQqefDggb5DUahUKhk1apS+w9DKgwcPRKVSyYoVK7T+28893r5mGx8zatQoUalUOlsf0acweaJ0o/5xU7/Mzc2laNGi0rt3b3n27Jm+w6MMYsKECbJt2zZ9h5HhrV27VmbNmqXvMNJdx44dNa5DyV979+4Vkf8ld9OmTfvkugoUKKDx95aWllKpUiVZtWpVeuwK6ZGJvgOg/54xY8aIi4uLxMbGyvHjx2XhwoWye/duuXbtmmTNmjXd4li6dKkkJSWl2/b0ITPu44QJE6R58+bSpEkTjent2rWT1q1bi5mZmX4Cy2DWrl0r165dk/79+2tMz58/v7x9+1ayZMmi9TozyvFmZmYmv/zyS4rpZcuW1Xpd5cqVk0GDBomIyNOnT+WXX36RDh06SFxcnHTp0uWrYyXDxOSJ0l39+vWlYsWKIiLSuXNnyZEjh8yYMUO2b98ubdq0SfVvoqOjxdLSUqdxfMmPQ0aTEfcxISFBkpKSxNTUVKu/MzY2FmNj4zSK6r9DXSr8JTLK8WZiYiLffvutTtaVJ08ejXV17NhRChYsKDNnzmTylInxsR3pXa1atURE5P79+yLy/uJjZWUld+/elQYNGoi1tbUEBASIiEhSUpLMmjVLSpUqJebm5uLg4CDdunWT169fp1jvnj17pEaNGmJtbS02Njbi7u4ua9euVeanVj8jOjpaBg0aJM7OzmJmZibFihWTadOmCYB/3Q9vb28pXbq0XLlyRWrUqCFZs2aVwoULy++//y4iIkeOHBEPDw+xsLCQYsWKycGDB1Os4/Hjx/Ldd9+Jg4ODmJmZSalSpeTXX39NsdyjR4+kSZMmYmlpKbly5ZIBAwZIXFxciuXSah/Pnz8vVapUEQsLC3FxcZFFixalWPb58+cSGBgoDg4OYm5uLmXLlpWVK1dqLJP88cisWbOkUKFCYmZmJn///Xeq21epVBIdHS0rV65UHpV07NhRRFKv81SgQAFp2LCh7N+/X8qVKyfm5uZSsmRJ2bJlS4p137t3T1q0aCHZs2eXrFmzSuXKlWXXrl3/+pmIiMTFxcmAAQPE3t5erK2tpVGjRvLo0aNUl/3c7zg1y5cvl1q1akmuXLnEzMxMSpYsKQsXLkx12U8d/97e3rJr1y4JDg5WPkf1cfJhfaRp06aJSqWS4ODgFNsYNmyYmJqaKudfasdbeHi4dOzYUWxtbcXOzk46dOgg4eHhKdZ15coVJfEwNzcXR0dH+e677+TVq1cplj1+/Li4u7uLubm5FCpUSBYvXvxZn196sLe3l+LFi8vdu3f1HQqlIZY8kd6pLzI5cuRQpiUkJIivr69Uq1ZNpk2bpjzO69atm6xYsUI6deokffv2lfv378u8efPk4sWL8tdffyl3vitWrJDvvvtOSpUqJcOGDRM7Ozu5ePGi7N27V9q2bZtqHACkUaNGcvjwYQkMDJRy5crJvn375IcffpDHjx/LzJkz/3VfXr9+LQ0bNpTWrVtLixYtZOHChdK6dWtZs2aN9O/fX7p37y5t27aVqVOnSvPmzSUkJESsra1FROTZs2dSuXJlUalU0rt3b7G3t5c9e/ZIYGCgREZGKo9X3r59K7Vr15aHDx9K3759xcnJSVavXi2HDh361/h0tY8NGjSQli1bSps2bWTjxo3So0cPMTU1le+++06J0dvbW+7cuSO9e/cWFxcX2bRpk3Ts2FHCw8OlX79+Gutcvny5xMbGSteuXcXMzEyyZ8+e6rZXr14tnTt3lkqVKknXrl1FRKRQoUKfjPf27dvSqlUr6d69u3To0EGWL18uLVq0kL1790qdOnVE5P1nX6VKFYmJiZG+fftKjhw5ZOXKldKoUSP5/fffpWnTpp/cRufOneW3336Ttm3bSpUqVeTQoUPi5+eXYrnP/Y4/ZuHChVKqVClp1KiRmJiYyB9//CE9e/aUpKQk6dWrl7Lcvx3/P/30k0RERMijR4+U79zKyirVbbZs2VIGDx4sGzdulB9++EFj3saNG6Vu3bqSLVu2VP8WgDRu3FiOHz8u3bt3lxIlSsjWrVulQ4cOKZY9cOCA3Lt3Tzp16iSOjo5y/fp1WbJkiVy/fl1OnTqlVAa/evWq1K1bV+zt7WXUqFGSkJAgI0eOFAcHh09+dh96+fKlxvssWbKIra2tVutITUJCgjx69OijnwllEiBKJ8uXL4eI4ODBg3jx4gVCQkKwfv165MiRAxYWFnj06BEAoEOHDhARDB06VOPvjx07BhHBmjVrNKbv3btXY3p4eDisra3h4eGBt2/faiyblJSk/L9Dhw7Inz+/8n7btm0QEYwbN07jb5o3bw6VSoU7d+58cv9q1KgBEcHatWuVaTdv3oSIwMjICKdOnVKm79u3DyKC5cuXK9MCAwORO3duvHz5UmO9rVu3hq2tLWJiYgAAs2bNgohg48aNyjLR0dEoXLgwRASHDx9O832cPn26Mi0uLg7lypVDrly58O7dO40Yf/vtN2W5d+/ewdPTE1ZWVoiMjAQA3L9/HyICGxsbPH/+/JPbVrO0tESHDh1STFcfX/fv31em5c+fHyKCzZs3K9MiIiKQO3duuLm5KdP69+8PEcGxY8eUaW/evIGLiwsKFCiAxMTEj8Zz6dIliAh69uypMb1t27YQEYwcOVKZ9rnf8cekNt/X1xcFCxZU3n/u8e/n56dxbKipv5Pkx6anpycqVKigsdyZM2cgIli1apUy7WPH25QpU5RpCQkJqF69eoptpLZv69atg4jg6NGjyrQmTZrA3NwcwcHByrS///4bxsbG+JyfNPX15cNXjRo1UnwGU6dO/eS68ufPj7p16+LFixd48eIFrl69inbt2kFE0KtXr3+NhTIuPrajdOfj4yP29vbi7OwsrVu3FisrK9m6davkyZNHY7kePXpovN+0aZPY2tpKnTp15OXLl8qrQoUKYmVlJYcPHxaR93ewb968kaFDh6aou/Gppsy7d+8WY2Nj6du3r8b0QYMGCQDZs2fPv+6blZWVtG7dWnlfrFgxsbOzkxIlSoiHh4cyXf3/e/fuicj7O/TNmzeLv7+/ANDYP19fX4mIiJALFy4ocebOnVuaN2+urC9r1qxKScyn6GIfTUxMpFu3bsp7U1NT6datmzx//lzOnz+vbMfR0VGjDluWLFmkb9++EhUVJUeOHNFYZ7NmzcTe3v5ft/0lnJycNEqObGxspH379nLx4kUJDQ1V4q1UqZJUq1ZNWc7Kykq6du0qDx48+OhjRPXfikiKz/TDUiRtvuOPsbCwUP4fEREhL1++lBo1asi9e/ckIiJCRL78+P+UVq1ayfnz5zUeRW3YsEHMzMykcePGH/273bt3i4mJica5bGxsLH369PnkvsXGxsrLly+lcuXKIiLK55KYmCj79u2TJk2aSL58+ZTlS5QoIb6+vp+9P+bm5nLgwAGN1/Tp0z/775Pbv3+/2Nvbi729vbi6usrq1aulU6dOMnXq1C9aH2UMfGxH6W7+/PlStGhRMTExEQcHBylWrJgYGWnm8SYmJpI3b16Nabdv35aIiAjJlStXqut9/vy5iPzvMWDp0qW1iis4OFicnJyUx2hqJUqUUOb/m7x586b4gbK1tRVnZ+cU00REqSvy4sULCQ8PlyVLlsiSJUtSXbd6/4KDg6Vw4cIptlOsWLF/jU8X++jk5JSi8n7RokVF5H19mcqVK0twcLAUKVIkxff6se24uLj863a/VGqfVfJ4HR0dJTg4WCO5VUse78eOp+DgYDEyMkrx+PDD70Ob7/hj/vrrLxk5cqScPHlSYmJiNOZFRESIra3tFx//n9KiRQsZOHCgbNiwQX788UcBIJs2bZL69euLjY3NR/8uODhYcufOneKRYGrHalhYmIwePVrWr1+f4nNQJ4YvXryQt2/fSpEiRVL8fbFixZRE9t8YGxuLj4/PZy37bzw8PGTcuHGSmJgo165dk3Hjxsnr16+1bvBAGQuTJ0p3lSpVUlrbfYyZmVmKH96kpCTJlSuXrFmzJtW/SauSC218rLXXx6bj/ytpq5t3f/vtt6nWBxERKVOmjA4iNEzJSx0yq6/9ju/evSu1a9eW4sWLy4wZM8TZ2VlMTU1l9+7dMnPmzDTtIsDJyUmqV68uGzdulB9//FFOnTolDx8+lMmTJ+tsGy1btpQTJ07IDz/8IOXKlRMrKytJSkqSevXqGXT3Bzlz5lQSMV9fXylevLg0bNhQZs+eLQMHDtRzdJRWmDxRhlGoUCE5ePCgVK1a9ZM/tuoSgGvXrknhwoU/e/358+eXgwcPyps3bzRKZm7evKnMTyvqVlqJiYn/ekecP39+uXbtmgDQKFG5devWv25HF/v45MmTFF1H/PPPPyIiSkur/Pnzy5UrVyQpKUkjCdbFZ6nto6c7d+6k+KxSize1z+9z4s2fP78kJSXJ3bt3NUpUPlyfNt9xav744w+Ji4uTHTt2aDyyUj+uVvvc41/bz7FVq1bSs2dPuXXrlmzYsEGyZs0q/v7+n/yb/PnzS1BQkERFRWmUPn342bx+/VqCgoJk9OjRMmLECGX67du3NZazt7cXCwuLFNNTW6e++Pn5SY0aNWTChAnSrVs3nXexQoaBdZ4ow2jZsqUkJibK2LFjU8xLSEhQmj/XrVtXrK2tZeLEiRIbG6uxHD7RHL9BgwaSmJgo8+bN05g+c+ZMUalUUr9+/a/fiY8wNjaWZs2ayebNm+XatWsp5r948UIjzidPnihdIIiIxMTEfPRRUHK62MeEhASNpuHv3r2TxYsXi729vVSoUEHZTmhoqGzYsEHj7+bOnStWVlZSo0aNf93Ox1haWqba1P1jnjx5Ilu3blXeR0ZGyqpVq6RcuXLi6OioxHvmzBk5efKkslx0dLQsWbJEChQoICVLlvzo+tWf2Zw5czSmf9h7tzbfcWrUpZfJj+GIiAhZvny5xnKfe/xbWloqj8M+R7NmzcTY2FjWrVsnmzZtkoYNG/5rYtCgQQNJSEjQ6E4hMTFR5s6d+6/7JpL6Z+jr6yvbtm2Thw8fKtNv3Lgh+/bt++x9SWtDhgyRV69eydKlS/UdCqURljxRhlGjRg3p1q2bTJw4US5duiR169aVLFmyyO3bt2XTpk0ye/Zsad68udjY2MjMmTOlc+fO4u7uLm3btpVs2bLJ5cuXJSYmJkVfQ2r+/v5Ss2ZN+emnn+TBgwdStmxZ2b9/v2zfvl369+//r03iv9akSZPk8OHD4uHhIV26dJGSJUtKWFiYXLhwQQ4ePChhYWEiItKlSxeZN2+etG/fXs6fPy+5c+eW1atXf1bv7LrYRycnJ5k8ebI8ePBAihYtKhs2bJBLly7JkiVLlK4iunbtKosXL5aOHTvK+fPnpUCBAvL777/LX3/9JbNmzUpR50obFSpUkIMHD8qMGTPEyclJXFxcUq2vpFa0aFEJDAyUs2fPioODg/z666/y7NkzjaRj6NChsm7dOqlfv7707dtXsmfPLitXrpT79+/L5s2bUzxCTq5cuXLSpk0bWbBggUREREiVKlUkKChI7ty5k2LZz/2OU1O3bl0xNTUVf39/6datm0RFRcnSpUslV65c8vTpU2W5zz3+K1SoIBs2bJCBAweKu7u7WFlZfbIkKVeuXFKzZk2ZMWOGvHnzRlq1avXRZdX8/f2latWqMnToUHnw4IHSx9aHSZuNjY14eXnJlClTJD4+XvLkySP79+9X+n5LbvTo0bJ3716pXr269OzZU0nKS5UqJVeuXPnXmLQRFBSUIgEVEWnSpMkn65TVr19fSpcuLTNmzJBevXplmM5DSQv6aOJH/03qpuRnz5795HIdOnSApaXlR+cvWbIEFSpUgIWFBaytreHq6orBgwfjyZMnGsvt2LEDVapUgYWFBWxsbFCpUiWsW7dOYzsfNtV+8+YNBgwYACcnJ2TJkgVFihTB1KlTNZp4f0yNGjVQqlSpFNPz588PPz+/FNMllebMz549Q69eveDs7IwsWbLA0dERtWvXxpIlSzSWCw4ORqNGjZA1a1bkzJkT/fr1U7ps+FRXBbrax3PnzsHT0xPm5ubInz8/5s2bl2LZZ8+eoVOnTsiZMydMTU3h6uqq0TQd+Pwm4cndvHkTXl5esLCwgIgo3RZ8rKsCPz8/7Nu3D2XKlIGZmRmKFy+OTZs2pVjv3bt30bx5c9jZ2cHc3ByVKlXCzp07Pyumt2/fom/fvsiRIwcsLS3h7++PkJCQFF0VqD+Xz/mOU7Njxw6UKVMG5ubmKFCgACZPnoxff/01xX6rl/3U8R8VFYW2bdvCzs4OIqIcJ6l1VaC2dOlSiAisra1TdIMApH68vXr1Cu3atYONjQ1sbW3Rrl07XLx4McU2Hj16hKZNm8LOzg62trZo0aIFnjx5kupneOTIEVSoUAGmpqYoWLAgFi1ahJEjR352VwWfur4k/ww+9lq9ejWAj5/bALBixYqPfo6U8amAz+hWmIhI3vdM/fLly1QfOxmiAgUKSOnSpWXnzp36DoWIMhHWeSIiIiLSApMnIiIiIi0weSIiIiLSAus8EREREWmBJU9EREREWmDyRERERKQFdpIp78ecevLkiVhbW3/xqONERESUvgDImzdvxMnJ6ZOd2eoakyd5P3zDh6PeExERUcYQEhIiefPmTbftMXkSUYaKCAkJERsbGz1HQ0RERJ8jMjJSnJ2dv2rIpy/B5En+N7q4jY0NkyciIqIMJr2r3LDCOBEREZEWmDwRERERaYHJExEREZEWmDwRERERaYHJExEREZEWmDwRERERaYHJExEREZEWmDwRERERaYHJExEREZEWmDwRERERaYHJExEREZEW9Jo8HT16VPz9/cXJyUlUKpVs27bto8t2795dVCqVzJo1S2N6WFiYBAQEiI2NjdjZ2UlgYKBERUWlbeBERET0n6XX5Ck6OlrKli0r8+fP/+RyW7dulVOnTomTk1OKeQEBAXL9+nU5cOCA7Ny5U44ePSpdu3ZNq5D/swBIVFSU8gKg75CIiIj0wkSfG69fv77Ur1//k8s8fvxY+vTpI/v27RM/Pz+NeTdu3JC9e/fK2bNnpWLFiiIiMnfuXGnQoIFMmzYt1WSLvkx0dLQ0btxYeb99+3axsrLSY0RERET6YdB1npKSkqRdu3byww8/SKlSpVLMP3nypNjZ2SmJk4iIj4+PGBkZyenTpz+63ri4OImMjNR4EREREX0Og06eJk+eLCYmJtK3b99U54eGhkquXLk0ppmYmEj27NklNDT0o+udOHGi2NraKi9nZ2edxk1ERESZl8EmT+fPn5fZs2fLihUrRKVS6XTdw4YNk4iICOUVEhKi0/UTERFR5mWwydOxY8fk+fPnki9fPjExMRETExMJDg6WQYMGSYECBURExNHRUZ4/f67xdwkJCRIWFiaOjo4fXbeZmZnY2NhovIiIiIg+h14rjH9Ku3btxMfHR2Oar6+vtGvXTjp16iQiIp6enhIeHi7nz5+XChUqiIjIoUOHJCkpSTw8PNI9ZiIiIsr89Jo8RUVFyZ07d5T39+/fl0uXLkn27NklX758kiNHDo3ls2TJIo6OjlKsWDERESlRooTUq1dPunTpIosWLZL4+Hjp3bu3tG7dmi3tiIiIKE3o9bHduXPnxM3NTdzc3EREZODAgeLm5iYjRoz47HWsWbNGihcvLrVr15YGDRpItWrVZMmSJWkVMhEREf3H6bXkydvbW6vOFh88eJBiWvbs2WXt2rU6jIqIiIjo4wy2wjgRERGRIWLyRERERKQFJk9EREREWmDyRERERKQFJk9EREREWmDyRERERKQFJk9EREREWmDyRERERKQFJk9EREREWmDyRERERKQFJk9EREREWmDyRERERKQFJk9EREREWmDyRERERKQFE30HQESUUQGQ6Oho5b2lpaWoVCo9RkRE6YHJExHRF4qOjpbGjRsr77dv3y5WVlZ6jIiI0gMf2xERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpQa/J09GjR8Xf31+cnJxEpVLJtm3blHnx8fEyZMgQcXV1FUtLS3FycpL27dvLkydPNNYRFhYmAQEBYmNjI3Z2dhIYGChRUVHpvCdERET0X6HX5Ck6OlrKli0r8+fPTzEvJiZGLly4IMOHD5cLFy7Ili1b5NatW9KoUSON5QICAuT69ety4MAB2blzpxw9elS6du2aXrtARERE/zEm+tx4/fr1pX79+qnOs7W1lQMHDmhMmzdvnlSqVEkePnwo+fLlkxs3bsjevXvl7NmzUrFiRRERmTt3rjRo0ECmTZsmTk5Oab4PRERE9N+Soeo8RUREiEqlEjs7OxEROXnypNjZ2SmJk4iIj4+PGBkZyenTpz+6nri4OImMjNR4EREREX2ODJM8xcbGypAhQ6RNmzZiY2MjIiKhoaGSK1cujeVMTEwke/bsEhoa+tF1TZw4UWxtbZWXs7NzmsZOREREmUeGSJ7i4+OlZcuWAkAWLlz41esbNmyYREREKK+QkBAdRElERET/BXqt8/Q51IlTcHCwHDp0SCl1EhFxdHSU58+fayyfkJAgYWFh4ujo+NF1mpmZiZmZWZrFTERERJmXQZc8qROn27dvy8GDByVHjhwa8z09PSU8PFzOnz+vTDt06JAkJSWJh4dHeodLRERE/wF6LXmKioqSO3fuKO/v378vly5dkuzZs0vu3LmlefPmcuHCBdm5c6ckJiYq9ZiyZ88upqamUqJECalXr5506dJFFi1aJPHx8dK7d29p3bo1W9oRERFRmtBr8nTu3DmpWbOm8n7gwIEiItKhQwcZNWqU7NixQ0REypUrp/F3hw8fFm9vbxERWbNmjfTu3Vtq164tRkZG0qxZM5kzZ066xE9ERET/PXpNnry9vQXAR+d/ap5a9uzZZe3atboMi4iIiOijDLrOExEREZGhYfJEREREpAWD76ogowMg0dHRyntLS0tRqVR6jIiIiIi+BpOnNBYdHS2NGzdW3m/fvl2srKz0GBERERF9DT62IyIiItICS56IiP7jWL2ASDtMnoiI/uNYvYBIO3xsR0RERKQFJk9EREREWmDyRERERKQFJk9EREREWmDyRERERKQFJk9EREREWmDyRERERKQF9vOUydm0tdHJeoyTjKW8lFfeO3d2lkSjxK9eb+TayK9eBxERUXpiyRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWlBr8nT0aNHxd/fX5ycnESlUsm2bds05gOQESNGSO7cucXCwkJ8fHzk9u3bGsuEhYVJQECA2NjYiJ2dnQQGBkpUVFQ67gURERH9l+g1eYqOjpayZcvK/PnzU50/ZcoUmTNnjixatEhOnz4tlpaW4uvrK7GxscoyAQEBcv36dTlw4IDs3LlTjh49Kl27dk2vXSAiIqL/GBN9brx+/fpSv379VOcBkFmzZsnPP/8sjRs3FhGRVatWiYODg2zbtk1at24tN27ckL1798rZs2elYsWKIiIyd+5cadCggUybNk2cnJzSbV+IiIjov8Fg6zzdv39fQkNDxcfHR5lma2srHh4ecvLkSREROXnypNjZ2SmJk4iIj4+PGBkZyenTpz+67ri4OImMjNR4EREREX0Og02eQkNDRUTEwcFBY7qDg4MyLzQ0VHLlyqUx38TERLJnz64sk5qJEyeKra2t8nJ2dtZx9ERERJRZGWzylJaGDRsmERERyiskJETfIREREVEGYbDJk6Ojo4iIPHv2TGP6s2fPlHmOjo7y/PlzjfkJCQkSFhamLJMaMzMzsbGx0XgRERERfQ6DTZ5cXFzE0dFRgoKClGmRkZFy+vRp8fT0FBERT09PCQ8Pl/PnzyvLHDp0SJKSksTDwyPdYyYiIqLMT6+t7aKiouTOnTvK+/v378ulS5cke/bski9fPunfv7+MGzdOihQpIi4uLjJ8+HBxcnKSJk2aiIhIiRIlpF69etKlSxdZtGiRxMfHS+/evaV169ZsaUdERERpQq/J07lz56RmzZrK+4EDB4qISIcOHWTFihUyePBgiY6Olq5du0p4eLhUq1ZN9u7dK+bm5srfrFmzRnr37i21a9cWIyMjadasmcyZMyfd94WIiIj+G/SaPHl7ewuAj85XqVQyZswYGTNmzEeXyZ49u6xduzYtwiMiIiJKwWDrPBEREREZIr2WPBER6Yulj+VXr8MYxuIu7sp7p8ZOkqhK/Or1Rh+M/up1EFHaYckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgZ1kfgI70SMiIqIPseSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0wOSJiIiISAtMnoiIiIi0YNDJU2JiogwfPlxcXFzEwsJCChUqJGPHjhUAyjIAZMSIEZI7d26xsLAQHx8fuX37th6jJiIioszMoJOnyZMny8KFC2XevHly48YNmTx5skyZMkXmzp2rLDNlyhSZM2eOLFq0SE6fPi2Wlpbi6+srsbGxeoyciIiIMisTfQfwKSdOnJDGjRuLn5+fiIgUKFBA1q1bJ2fOnBGR96VOs2bNkp9//lkaN24sIiKrVq0SBwcH2bZtm7Ru3VpvsRMREVHm9FUlTy9evJDjx4/L8ePH5cWLF7qKSVGlShUJCgqSf/75R0RELl++LMePH5f69euLiMj9+/clNDRUfHx8lL+xtbUVDw8POXny5EfXGxcXJ5GRkRovIiIios/xRSVP0dHR0qdPH1m9erUkJiaKiIixsbG0b99e5s6dK1mzZtVJcEOHDpXIyEgpXry4GBsbS2JioowfP14CAgJERCQ0NFRERBwcHDT+zsHBQZmXmokTJ8ro0aN1EiMRERH9t3xRydPAgQPlyJEjsmPHDgkPD5fw8HDZvn27HDlyRAYNGqSz4DZu3Chr1qyRtWvXyoULF2TlypUybdo0Wbly5Vetd9iwYRIREaG8QkJCdBQxERERZXZfVPK0efNm+f3338Xb21uZ1qBBA7GwsJCWLVvKwoULdRLcDz/8IEOHDlXqLrm6ukpwcLBMnDhROnToII6OjiIi8uzZM8mdO7fyd8+ePZNy5cp9dL1mZmZiZmamkxiJiIjov+WLSp5iYmJSPCoTEcmVK5fExMR8dVDJt2NkpBmisbGxJCUliYiIi4uLODo6SlBQkDI/MjJSTp8+LZ6enjqLg4iIiEjti5InT09PGTlypEZ3AG/fvpXRo0frNGnx9/eX8ePHy65du+TBgweydetWmTFjhjRt2lRERFQqlfTv31/GjRsnO3bskKtXr0r79u3FyclJmjRporM4iIiIiNS+6LHd7NmzxdfXV/LmzStly5YVkfct4czNzWXfvn06C27u3LkyfPhw6dmzpzx//lycnJykW7duMmLECGWZwYMHS3R0tHTt2lXCw8OlWrVqsnfvXjE3N9dZHERERERqX5Q8lS5dWm7fvi1r1qyRmzdviohImzZtJCAgQCwsLHQWnLW1tcyaNUtmzZr10WVUKpWMGTNGxowZo7PtEhEREX3MF3eSmTVrVunSpYsuYyEiIiIyeJ+dPO3YsUPq168vWbJkkR07dnxy2UaNGn11YERERESG6LOTpyZNmkhoaKjkypXrk5WxVSqV0nEmERERUWbz2cmTunuAD/9PRERE9F/yVWPbEREREf3XfFHy1LdvX5kzZ06K6fPmzZP+/ft/bUxEREREBuuLkqfNmzdL1apVU0yvUqWK/P77718dFBEREZGh+qKuCl69eiW2trYpptvY2MjLly+/OigyPImqRLlgf0HjPRER0X/RF5U8FS5cWPbu3Zti+p49e6RgwYJfHRQZIJVIolGi8hKVvgMiIiLSjy8qeRo4cKD07t1bXrx4IbVq1RIRkaCgIJk+ffonewMnIiIiyui+KHn67rvvJC4uTsaPHy9jx44VEZECBQrIwoULpX379joNkIiIiMiQfPHwLD169JAePXrIixcvxMLCQqysrHQZFxEREZFB+uLkKSEhQf7880+5e/eutG3bVkREnjx5IjY2NkykkkmURDkrZzXeExERUcb1RclTcHCw1KtXTx4+fChxcXFSp04dsba2lsmTJ0tcXJwsWrRI13FmXComTERERJnJF7W269evn1SsWFFev34tFhYWyvSmTZtKUFCQzoIjIiIiMjRfVPJ07NgxOXHihJiammpML1CggDx+/FgngREREREZoi8qeUpKSpLExJSPoh49eiTW1tZfHRQRERGRofqi5Klu3boa/TmpVCqJioqSkSNHSoMGDXQVGxEREZHB+aLHdtOmTZN69epJyZIlJTY2Vtq2bSu3b9+WnDlzyrp163QdIxEREZHB+KLkydnZWS5fviwbNmyQy5cvS1RUlAQGBkpAQIBGBXIiIiKizEbr5Ck+Pl6KFy8uO3fulICAAAkICEiLuIiIiIgMktbJU5YsWSQ2NjYtYiEiIi3YtLXRyXqMk4ylvJRX3jt3dn4/APhXilwb+dXrIDJEX1RhvFevXjJ58mRJSEjQdTxEREREBu2L6jydPXtWgoKCZP/+/eLq6iqWlpYa87ds2aKT4IiIiIgMzRclT3Z2dtKsWTNdx0JERERk8LRKnpKSkmTq1Knyzz//yLt376RWrVoyatQotrAjIiKi/wyt6jyNHz9efvzxR7GyspI8efLInDlzpFevXmkVGxEREZHB0Sp5WrVqlSxYsED27dsn27Ztkz/++EPWrFkjSUlJaRUfERERkUHRKnl6+PChxvArPj4+olKp5MmTJzoPjIiIiMgQaZU8JSQkiLm5uca0LFmySHx8vE6DIiIiIjJUWlUYByAdO3YUMzMzZVpsbKx0795do7sCdlVAREREmZVWyVOHDh1STPv22291FgwRERGRodMqeVq+fHlaxUFERESUIXzR8CxERERE/1VMnoiIiIi08EXDsxARkUiiJMpZOavxnogyPyZPRERfSsWEiei/iI/tiIiIiLTA5ImIiIhIC3xsR0RERCIiMmDjAH2H8EkzW87UdwgikgFKnh4/fizffvut5MiRQywsLMTV1VXOnTunzAcgI0aMkNy5c4uFhYX4+PjI7du39RgxERERZWYGnTy9fv1aqlatKlmyZJE9e/bI33//LdOnT5ds2bIpy0yZMkXmzJkjixYtktOnT4ulpaX4+vpKbGysHiMnIiKizMqgH9tNnjxZnJ2dNXo2d3FxUf4PQGbNmiU///yzNG7cWEREVq1aJQ4ODrJt2zZp3bp1usdMREREmZtBlzzt2LFDKlasKC1atJBcuXKJm5ubLF26VJl///59CQ0NFR8fH2Wara2teHh4yMmTJz+63ri4OImMjNR4EREREX0Og06e7t27JwsXLpQiRYrIvn37pEePHtK3b19ZuXKliIiEhoaKiIiDg4PG3zk4OCjzUjNx4kSxtbVVXs7Ozmm3E0RERJSpGHTylJSUJOXLl5cJEyaIm5ubdO3aVbp06SKLFi36qvUOGzZMIiIilFdISIiOIiYiIqLMzqCTp9y5c0vJkiU1ppUoUUIePnwoIiKOjo4iIvLs2TONZZ49e6bMS42ZmZnY2NhovIiIiIg+h0EnT1WrVpVbt25pTPvnn38kf/78IvK+8rijo6MEBQUp8yMjI+X06dPi6emZrrESERHRf4NBt7YbMGCAVKlSRSZMmCAtW7aUM2fOyJIlS2TJkiUiIqJSqaR///4ybtw4KVKkiLi4uMjw4cPFyclJmjRpot/giYiIKFMy6OTJ3d1dtm7dKsOGDZMxY8aIi4uLzJo1SwICApRlBg8eLNHR0dK1a1cJDw+XatWqyd69e8Xc3FyPkRMREVFmZdDJk4hIw4YNpWHDhh+dr1KpZMyYMTJmzJh0jIqIiIj+qwy6zhMRERGRoWHyRERERKQFJk9EREREWmDyRERERKQFJk9EREREWjD41nZERJS5ZRuQTd8hfNTrma/1HQIZIJY8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFpg8EREREWmByRMRERGRFkz0HQBRegIg0dHRyntLS0tRqVR6jIiIiDKaDFXyNGnSJFGpVNK/f39lWmxsrPTq1Uty5MghVlZW0qxZM3n27Jn+giSDFh0dLY0bN1ZeyRMpIiKiz5FhkqezZ8/K4sWLpUyZMhrTBwwYIH/88Yds2rRJjhw5Ik+ePJFvvvlGT1ESERFRZpchkqeoqCgJCAiQpUuXSrZs2ZTpERERsmzZMpkxY4bUqlVLKlSoIMuXL5cTJ07IqVOn9BgxERERZVYZInnq1auX+Pn5iY+Pj8b08+fPS3x8vMb04sWLS758+eTkyZMfXV9cXJxERkZqvIiIiIg+h8FXGF+/fr1cuHBBzp49m2JeaGiomJqaip2dncZ0BwcHCQ0N/eg6J06cKKNHj9Z1qERERPQfYNAlTyEhIdKvXz9Zs2aNmJub62y9w4YNk4iICOUVEhKis3UTERFR5mbQydP58+fl+fPnUr58eTExMRETExM5cuSIzJkzR0xMTMTBwUHevXsn4eHhGn/37NkzcXR0/Oh6zczMxMbGRuNFRERE9DkM+rFd7dq15erVqxrTOnXqJMWLF5chQ4aIs7OzZMmSRYKCgqRZs2YiInLr1i15+PCheHp66iNkIiIiyuQMOnmytraW0qVLa0yztLSUHDlyKNMDAwNl4MCBkj17drGxsZE+ffqIp6enVK5cWR8hExERUSZn0MnT55g5c6YYGRlJs2bNJC4uTnx9fWXBggX6DouIiIgyqQyXPP35558a783NzWX+/Pkyf/58/QRERERE/ykGXWGciIiIyNAweSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi0weSIiIiLSApMnIiIiIi2Y6DsAIspYBmwcoO8QPmlmy5n6DoGIMjmWPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgckTERERkRaYPBERERFpgT2MExERfaWa02vqO4RPOjzosL5DyFRY8kRERESkBSZPRERERFpg8kRERESkBSZPRERERFpg8kRERESkBSZPRERERFpg8kRERESkBYNOniZOnCju7u5ibW0tuXLlkiZNmsitW7c0lomNjZVevXpJjhw5xMrKSpo1aybPnj3TU8RERESU2Rl08nTkyBHp1auXnDp1Sg4cOCDx8fFSt25diY6OVpYZMGCA/PHHH7Jp0yY5cuSIPHnyRL755hs9Rk1ERESZmUH3ML53716N9ytWrJBcuXLJ+fPnxcvLSyIiImTZsmWydu1aqVWrloiILF++XEqUKCGnTp2SypUr6yNsIiIiysQMOnn6UEREhIiIZM+e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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = \"Tipo de excursión\", \n",
    "              y = 'Precio',\n",
    "              data = excursiones_florencia, \n",
    "              palette=['#004d00', '#006600', '#008000', '#339933', '#66b266'])\n",
    "plt.title('Precio medio por tipo de actividad FLR')\n",
    "plt.xticks(rotation=60)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se puede observar que su índice de certeza esta en un rango muy abierto ya que cuenta con una muestra pequeña donde los valores del precio entre ellos dista mucho. Mientras que aquellos donde el indice de confianza se ve más reducido es porque tienen mas actividades y los precios son mas regulares entre ellos."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Con 95% de certeza, la media está en esos intervalos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\2269571236.py:1: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x = \"Tipo de excursión\",\n",
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_7936\\2269571236.py:1: UserWarning: \n",
      "The palette list has fewer values (5) than needed (11) and will cycle, which may produce an uninterpretable plot.\n",
      "  sns.barplot(x = \"Tipo de excursión\",\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\n",
       " [Text(0, 0, 'Visitas Guiadas'),\n",
       "  Text(1, 0, 'Excursiones de un día'),\n",
       "  Text(2, 0, 'Pases turísticos'),\n",
       "  Text(3, 0, 'Espectáculos'),\n",
       "  Text(4, 0, 'Tours en Bus turístico'),\n",
       "  Text(5, 0, 'Tours a pie'),\n",
       "  Text(6, 0, 'Traslados Aeropuertos'),\n",
       "  Text(7, 0, 'Paseos en barco'),\n",
       "  Text(8, 0, 'Experiencias Gastronómicas'),\n",
       "  Text(9, 0, 'Tours en Bicicleta'),\n",
       "  Text(10, 0, 'Alquiler de Vehículos')])"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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JGfOnFK4cGEREbly5YoYGRnJ3r17kzRAIiIiouSSoMSoUKFCcufOHVm9erXcvHlTRESaNWsmLVq0EGPjhHeJJCIiItKnBI9jZGJiIu3bt0/KWIiIiIj06rsTo+3bt0uNGjUkQ4YMsn379n98b506dRIdGBGlbWEHj+s7BC3GlcrqOwQiSgG+OzHy8/OTFy9eiLW1tfj5+X3zfSqVSqKjo5MiNiIiIqJk9d2JUUxMTLz/T0RERJRWJKi7PhEREVFalKDEqHv37jJr1qw4y+fMmSM9e/ZMbExEREREepGgxGjTpk1SunTpOMtLlSolGzduTHRQRERERPqQoMTo7du3YmlpGWe5hYWFvHnzJtFBEREREelDghIjJycn2bNnT5zlu3fvljx58iQ6KCIiIiJ9SNAAj71795auXbvK69evpWLFiiIicvDgQZk6darMmDEjKeMjIiIiSjYJSozatm0rERERMnbsWBk9erSIiOTOnVvmz58vLVu2TNIAiYiIiJJLgqcE6dy5s3Tu3Flev34txsbGYmZmlpRxERERESW7BI9jFBUVJQcOHJDNmzcLABERefbsmYSEhCRZcERERETJKUElRoGBgVK9enV59OiRRERESJUqVcTc3FwmTpwoERERsmDBgqSOk4iIiEjnElRi1KNHDylevLi8f/9ejI2NleX16tWTgwcPJllwRERERMkpQSVGx48fl5MnT0rGjBm1lufOnVuePn2aJIERERERJbcElRjFxMRIdHR0nOVPnjwRc3PzRAdFREREpA8JSoyqVq2qNV6RSqWSkJAQGT58uNSsWTOpYiMiIiJKVgmqSpsyZYpUr15dChYsKOHh4dK8eXO5c+eOZMuWTdauXZvUMRIREREliwQlRvb29nLlyhX5/fff5cqVKxISEiL+/v7SokULrcbYRERERKnJDydGkZGR4uLiIjt27JAWLVpIixYtdBEXERERUbL74TZGGTJkkPDwcF3EQkRERKRXCWp8HRAQIBMnTpSoqKikjoeIiIhIbxLUxujcuXNy8OBB2bdvn7i5uYmpqanW65s3b06S4IiIiIiSU4ISo0yZMkmDBg2SOhYiIiIivfqhxCgmJkYmT54st2/fls+fP0vFihVlxIgR7IlGREREacIPtTEaO3asDBo0SMzMzCRHjhwya9YsCQgI0FVsRERERMnqhxKjlStXyrx5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5fPnzxIUFKRVavTy5UuxtbWN97sMDQ3F0NBQ1yETERFRGqTXEiMA0rVrV9myZYscOnRIHB0dtV738PCQDBkyyMGDB5Vlt27dkkePHom3t3dyh0tERERpnF5LjAICAmTNmjWybds2MTc3V9oNWVpairGxsVhaWoq/v7/07t1bsmTJIhYWFtKtWzfx9vZmjzQiIiJKcnpNjObPny8iIuXLl9davmzZMmndurWIiEyfPl3SpUsnDRo0kIiICKlWrZrMmzcvmSMlIiKi/wK9JkYA/vU9RkZGMnfuXJk7d24yRERERET/ZSmmVxoRERGRvjExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGpMjIiIiIjUmBgRERERqTExIiIiIlJjYkRERESkxsSIiIiISI2JEREREZEaEyMiIiIiNSZGRERERGqpIjGaO3eu5M6dW4yMjMTLy0vOnj2r75CIiIgoDUrxidHvv/8uvXv3luHDh8vFixelcOHCUq1aNXn16pW+QyMiIqI0JsUnRtOmTZP27dtLmzZtpGDBgrJgwQIxMTGRpUuX6js0IiIiSmPS6zuAf/L582e5cOGCDBw4UFmWLl06qVy5spw6dSrez0REREhERITyd3BwsIiIfPjwQVkWFhqqo4gTJjJWbP8k7GPqizssLIXFHPnvMYeGhSRDJN/vw/fE/DEsGSL5fh8+RP7re1LjechzMPF4DiaPtHAO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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = \"Tipo de excursión\", \n",
    "              y = 'Precio',\n",
    "              data = excursiones_lisboa, \n",
    "              palette=['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF'])\n",
    "plt.title('Precio medio por tipo de actividad LIS')\n",
    "plt.xticks(rotation=60)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se puede observar que su índice de certeza esta en un rango muy abierto ya que cuenta con una muestra pequeña donde los valores del precio entre ellos dista mucho. Mientras que aquellos donde el indice de confianza se ve más reducido es porque tienen mas actividades y los precios son mas regulares entre ellos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>62.400000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>33.671835</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>27.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>46.100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>64.450000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>79.725000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>95.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Precio\n",
       "count   3.000000\n",
       "mean   62.400000\n",
       "std    33.671835\n",
       "min    27.750000\n",
       "25%    46.100000\n",
       "50%    64.450000\n",
       "75%    79.725000\n",
       "max    95.000000"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "excursiones_lisboa[excursiones_lisboa['Tipo de excursión']=='Paseos en barco'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Costo', 'ID Salida', 'Salida', 'ID Llegada', 'Llegada', 'Tiempo',\n",
       "       'Paradas', 'Aerolínea', 'Hora de Salida', 'Hora de Llegada'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Costo</th>\n",
       "      <th>ID Salida</th>\n",
       "      <th>Salida</th>\n",
       "      <th>ID Llegada</th>\n",
       "      <th>Llegada</th>\n",
       "      <th>Tiempo</th>\n",
       "      <th>Paradas</th>\n",
       "      <th>Aerolínea</th>\n",
       "      <th>Hora de Salida</th>\n",
       "      <th>Hora de Llegada</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>428.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T09:55:00</td>\n",
       "      <td>2024-10-25T12:15:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>428.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>429.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T15:35:00</td>\n",
       "      <td>2024-10-25T17:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>429.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>290.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>250</td>\n",
       "      <td>1</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T17:20:00</td>\n",
       "      <td>2024-10-25T21:30:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>290.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>281.68</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>300</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T05:50:00</td>\n",
       "      <td>2024-10-25T10:50:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>281.68</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>284</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-28T19:15:00</td>\n",
       "      <td>2024-10-28T23:59:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>451.98</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T09:55:00</td>\n",
       "      <td>2024-10-25T12:15:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>451.98</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T06:15:00</td>\n",
       "      <td>2024-10-28T08:45:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>438.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>140</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-25T15:35:00</td>\n",
       "      <td>2024-10-25T17:55:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>438.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T06:15:00</td>\n",
       "      <td>2024-10-28T08:45:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>295.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>380</td>\n",
       "      <td>1</td>\n",
       "      <td>Air Europa</td>\n",
       "      <td>2024-10-25T15:10:00</td>\n",
       "      <td>2024-10-25T21:30:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>295.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>308.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>450</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T07:05:00</td>\n",
       "      <td>2024-10-25T14:35:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>308.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>316.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>300</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T05:50:00</td>\n",
       "      <td>2024-10-25T10:50:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>316.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>340.00</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>415</td>\n",
       "      <td>1</td>\n",
       "      <td>ITA Airways</td>\n",
       "      <td>2024-10-25T11:35:00</td>\n",
       "      <td>2024-10-25T18:30:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>340.00</td>\n",
       "      <td>FLR</td>\n",
       "      <td>Florence</td>\n",
       "      <td>MAD</td>\n",
       "      <td>Madrid</td>\n",
       "      <td>150</td>\n",
       "      <td>0</td>\n",
       "      <td>Vueling Airlines</td>\n",
       "      <td>2024-10-28T12:35:00</td>\n",
       "      <td>2024-10-28T15:05:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Costo ID Salida    Salida ID Llegada   Llegada  Tiempo  Paradas  \\\n",
       "0   428.00       MAD    Madrid        FLR  Florence     140        0   \n",
       "1   428.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "2   429.00       MAD    Madrid        FLR  Florence     140        0   \n",
       "3   429.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "4   290.00       MAD    Madrid        FLR  Florence     250        1   \n",
       "5   290.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "6   281.68       MAD    Madrid        FLR  Florence     300        1   \n",
       "7   281.68       FLR  Florence        MAD    Madrid     284        1   \n",
       "8   451.98       MAD    Madrid        FLR  Florence     140        0   \n",
       "9   451.98       FLR  Florence        MAD    Madrid     150        0   \n",
       "10  438.00       MAD    Madrid        FLR  Florence     140        0   \n",
       "11  438.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "12  295.00       MAD    Madrid        FLR  Florence     380        1   \n",
       "13  295.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "14  308.00       MAD    Madrid        FLR  Florence     450        1   \n",
       "15  308.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "16  316.00       MAD    Madrid        FLR  Florence     300        1   \n",
       "17  316.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "18  340.00       MAD    Madrid        FLR  Florence     415        1   \n",
       "19  340.00       FLR  Florence        MAD    Madrid     150        0   \n",
       "\n",
       "           Aerolínea       Hora de Salida      Hora de Llegada  \n",
       "0   Vueling Airlines  2024-10-25T09:55:00  2024-10-25T12:15:00  \n",
       "1   Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "2   Vueling Airlines  2024-10-25T15:35:00  2024-10-25T17:55:00  \n",
       "3   Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "4   Vueling Airlines  2024-10-25T17:20:00  2024-10-25T21:30:00  \n",
       "5   Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "6        ITA Airways  2024-10-25T05:50:00  2024-10-25T10:50:00  \n",
       "7        ITA Airways  2024-10-28T19:15:00  2024-10-28T23:59:00  \n",
       "8   Vueling Airlines  2024-10-25T09:55:00  2024-10-25T12:15:00  \n",
       "9   Vueling Airlines  2024-10-28T06:15:00  2024-10-28T08:45:00  \n",
       "10  Vueling Airlines  2024-10-25T15:35:00  2024-10-25T17:55:00  \n",
       "11  Vueling Airlines  2024-10-28T06:15:00  2024-10-28T08:45:00  \n",
       "12        Air Europa  2024-10-25T15:10:00  2024-10-25T21:30:00  \n",
       "13  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "14       ITA Airways  2024-10-25T07:05:00  2024-10-25T14:35:00  \n",
       "15  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "16       ITA Airways  2024-10-25T05:50:00  2024-10-25T10:50:00  \n",
       "17  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  \n",
       "18       ITA Airways  2024-10-25T11:35:00  2024-10-25T18:30:00  \n",
       "19  Vueling Airlines  2024-10-28T12:35:00  2024-10-28T15:05:00  "
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Salida</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Florence</th>\n",
       "      <td>10.0</td>\n",
       "      <td>163.4</td>\n",
       "      <td>42.374521</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>284.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Madrid</th>\n",
       "      <td>10.0</td>\n",
       "      <td>265.5</td>\n",
       "      <td>122.530042</td>\n",
       "      <td>140.0</td>\n",
       "      <td>140.0</td>\n",
       "      <td>275.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>450.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          count   mean         std    min    25%    50%    75%    max\n",
       "Salida                                                               \n",
       "Florence   10.0  163.4   42.374521  150.0  150.0  150.0  150.0  284.0\n",
       "Madrid     10.0  265.5  122.530042  140.0  140.0  275.0  360.0  450.0"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_vuelos_florencia.groupby('Salida')['Tiempo'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Duración promedio de vuelo desde')"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjsAAAHHCAYAAABZbpmkAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABDL0lEQVR4nO3deXgO9/7/8dedkDuyS2StCGKNvckpOdQWFVvRcoo6RKt0CUqq2nSh1GlaWkqPcnQRR+tUtZZWrbWr0ApKFQeHRktEqYQgkWR+f/SX++uWBNFEYvp8XNd9XeYzn5l5z33fkVdmPjNjMQzDEAAAgEk5lHUBAAAApYmwAwAATI2wAwAATI2wAwAATI2wAwAATI2wAwAATI2wAwAATI2wAwAATI2wA5QThmFo6tSpWrBgQVmXAgCmQtgBbpPq1atr0KBBRc5/8803NWnSJLVo0eL2FWVC177PGzZskMVi0YYNG0p1u4mJibJYLDp27Fipbud2GDRokKpXr17q22nbtq3atm1b6tu52u36PqB8Ieyg3Mv/JZL/cnZ2VlBQkKKjozV9+nSdP3++rEv8w7755hslJCRo+fLlCgkJKetyAMBUKpR1AcDNmjBhgmrUqKErV64oNTVVGzZs0MiRIzVlyhR98cUXaty4cVmXeF0HDx6Ug0Phf1/s379fS5YsUbNmzW5zVebXunVrXbp0SU5OTmVdCoAyQtjBHaNz586KiIiwTcfHx2vdunXq1q2bunfvrv3796tSpUp/eDs5OTnKy8sr8V+OVqu1yHmPPfZYiW6rpOTl5Sk7O1vOzs5lXcotc3BwuKPrB/DHcRoLd7T27dvr5Zdf1k8//aSPPvrI1l7UWIBrxyIcO3ZMFotFb775pt5++22FhobKarXqxx9/VHZ2tsaOHavw8HB5enrK1dVV9957r9avX19gvXl5eZo2bZoaNWokZ2dn+fr6qlOnTtqxY4etT2Fjdv73v//pb3/7m7y9veXi4qIWLVroq6++suuTP8bg008/1T/+8Q9VrVpVzs7OioqK0uHDh2/4Hr3yyiuyWCw6cOCAHnroIXl4eMjHx0dPP/20Ll++bNfXYrFo2LBh+vjjj9WgQQNZrVatXLlSkrRr1y517txZHh4ecnNzU1RUlLZt22a3fP4pxy1btmjEiBHy9fWVl5eXHn/8cWVnZ+vcuXMaOHCgKleurMqVK2vMmDEyDKPAe/n222+rQYMGcnZ2lr+/vx5//HH99ttvdv0Mw9DEiRNVtWpVubi4qF27dtq3b1+B/S9qjMbChQsVHh6uSpUqqUqVKvr73/+uX3755YbvpyTt27dP7du3V6VKlVS1alVNnDhReXl5hfZdsWKF7r33Xrm6usrd3V1du3YttM6r7dixQxaLRXPnzi0wb9WqVbJYLFq2bJmkosfX5H/u1/roo49s++3t7a2+ffvq+PHjN9znzMxMPfPMMwoODpbValXdunX15ptvFvj8ijJ79myFhoaqUqVKuueee7R58+ZC+2VlZWncuHGqVauWrFargoODNWbMGGVlZdn1W7NmjVq1aiUvLy+5ubmpbt26euGFF+z6/Pzzz+rZs6dcXV3l5+enUaNGFVhPvu3bt6tTp07y9PSUi4uL2rRpo2+++eam9g3lH0d2cMcbMGCAXnjhBa1evVpDhgy5pXXMmTNHly9f1tChQ2W1WuXt7a2MjAy9//776tevn4YMGaLz58/rgw8+UHR0tL799ls1bdrUtvzgwYOVmJiozp0767HHHlNOTo42b96sbdu22R2NutqpU6f017/+VRcvXtSIESPk4+OjuXPnqnv37vrss8/0wAMP2PV//fXX5eDgoNGjRys9PV2TJk1S//79tX379pvax4ceekjVq1dXQkKCtm3bpunTp+u3337Tv//9b7t+69at06effqphw4apSpUqql69uvbt26d7771XHh4eGjNmjCpWrKh//etfatu2rTZu3KjmzZvbrWP48OEKCAjQ+PHjtW3bNs2ePVteXl7aunWrqlWrptdee03Lly/X5MmT1bBhQw0cONC27OOPP67ExEQ98sgjGjFihI4ePap//vOf2rVrl7755htVrFhRkjR27FhNnDhRXbp0UZcuXbRz50517NhR2dnZN3wv8tf/l7/8RQkJCTp16pSmTZumb775Rrt27ZKXl1eRy6ampqpdu3bKycnR888/L1dXV82ePbvQo4rz5s1TTEyMoqOj9cYbb+jixYuaOXOmWrVqpV27dhU5CDgiIkI1a9bUp59+qpiYGLt5CxYsUOXKlRUdHX3D/bzWP/7xD7388st66KGH9Nhjj+n06dN655131Lp16+vut2EY6t69u9avX6/BgweradOmWrVqlZ599ln98ssvmjp16nW3+8EHH+jxxx/X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LF25ckXDhg1T3759uRILAABIKuMjOzt27FCzZs3UrFkzSVJcXJyaNWumsWPHytHRUXv27FH37t1Vp04dDR48WOHh4dq8ebPdKaiPP/5Y9erVU1RUlLp06aJWrVpp9uzZZbVLAACgnCnTIztt27a97v17Vq1adcN1eHt7a/78+SVZFgAAMJE7aswOAABAcRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqRF2AACAqZVp2Nm0aZPuv/9+BQUFyWKxaMmSJXbzDcPQ2LFjFRgYqEqVKqlDhw46dOiQXZ+zZ8+qf//+8vDwkJeXlwYPHqwLFy7cxr0AAADlWZmGnczMTDVp0kQzZswodP6kSZM0ffp0zZo1S9u3b5erq6uio6N1+fJlW5/+/ftr3759WrNmjZYtW6ZNmzZp6NCht2sXAABAOVehLDfeuXNnde7cudB5hmHo7bff1ksvvaQePXpIkv7973/L399fS5YsUd++fbV//36tXLlS3333nSIiIiRJ77zzjrp06aI333xTQUFBt21fAABA+VRux+wcPXpUqamp6tChg63N09NTzZs3V1JSkiQpKSlJXl5etqAjSR06dJCDg4O2b99e5LqzsrKUkZFh9wIAAOZUbsNOamqqJMnf39+u3d/f3zYvNTVVfn5+dvMrVKggb29vW5/CJCQkyNPT0/YKDg4u4eoBAEB5UW7DTmmKj49Xenq67XX8+PGyLgkAAJSScht2AgICJEmnTp2yaz916pRtXkBAgNLS0uzm5+Tk6OzZs7Y+hbFarfLw8LB7AQAAcyq3YadGjRoKCAjQ2rVrbW0ZGRnavn27IiMjJUmRkZE6d+6ckpOTbX3WrVunvLw8NW/e/LbXDAAAyp8yvRrrwoULOnz4sG366NGj2r17t7y9vVWtWjWNHDlSEydOVO3a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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(y = 'Tiempo', data=df_vuelos_florencia, x= 'Salida')\n",
    "plt.title('Duración promedio de vuelo desde')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Este tiempo tiene una media distinta porque esta ruta de viaje suele tener escalas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Duración promedio de vuelo desde')"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjIAAAHHCAYAAACle7JuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA/RUlEQVR4nO3deVxUZf//8feAMKAIKCpLIqKZuKQplpKWa6FpbpRLVrikWS6pmbd0p6aZqJWa3aZphmZ6p+bS5pa4lCWWaN0tRuStYSloGqCUgMz5/dGP+TYCKgbOHO/X8/GYx8Nznetc53NmBnlznXNmLIZhGAIAADAhN2cXAAAAcLUIMgAAwLQIMgAAwLQIMgAAwLQIMgAAwLQIMgAAwLQIMgAAwLQIMgAAwLQIMsA1YBiG5s6dq9WrVzu7FAC4rhBkgDJQu3ZtDRw4sMT1L774ombPnq1WrVpdu6KuQxc/z7t27ZLFYtGuXbvKdb/Lli2TxWLR0aNHy3U/18LAgQNVu3btct9Pu3bt1K5du3Lfz19dq/cDXAtBBk5V+Aui8OHl5aWQkBBFR0dr/vz5Onv2rLNL/Ns+/fRTxcfHa9OmTQoLC3N2OQBwXang7AIASZo2bZrCw8OVn5+v9PR07dq1S2PGjNGcOXP03nvvqUmTJs4u8ZJSUlLk5lb83wWHDh3Sxo0b1axZs2tc1fXvzjvv1B9//CFPT09nlwLASQgycAldunRRixYt7MtxcXHasWOHunXrpu7du+vQoUPy9vb+2/u5cOGCbDZbmf/is1qtJa575JFHynRfZcVmsykvL09eXl7OLuWqubm5mbp+AH8fp5bgsjp06KBJkybpp59+0ltvvWVvL+nc+8Xn/o8ePSqLxaIXX3xR8+bNU926dWW1WvXdd98pLy9PkydPVmRkpPz8/FSpUiXdcccd2rlzZ5FxbTabXn75Zd18883y8vJS9erV1blzZ+3fv9/ep7hrZP773//q/vvvV9WqVVWxYkW1atVKH374oUOfwnP6a9as0fPPP6+aNWvKy8tLHTt21I8//njZ5+jZZ5+VxWLR999/rz59+sjX11cBAQF64okndP78eYe+FotFI0eO1MqVK9WoUSNZrVZt2bJFknTw4EF16dJFvr6+8vHxUceOHZWUlOSwfeFpwD179mj06NGqXr26/P399eijjyovL0+ZmZl6+OGHVaVKFVWpUkUTJkyQYRhFnst58+apUaNG8vLyUmBgoB599FH99ttvDv0Mw9D06dNVs2ZNVaxYUe3bt9e3335b5PhLuiZi7dq1ioyMlLe3t6pVq6YHH3xQv/zyy2WfT0n69ttv1aFDB3l7e6tmzZqaPn26bDZbsX03b96sO+64Q5UqVVLlypXVtWvXYuv8q/3798tisWj58uVF1m3dulUWi0UffPCBpJKvZyl83S/21ltv2Y+7atWq6tevn44dO3bZY87JydGTTz6p0NBQWa1W1a9fXy+++GKR168kixcvVt26deXt7a3bbrtNn3zySbH9cnNzNWXKFN14442yWq0KDQ3VhAkTlJub69Dvo48+Ups2beTv7y8fHx/Vr19fTz/9tEOfn3/+WT179lSlSpVUo0YNjR07tsg4hfbt26fOnTvLz89PFStWVNu2bfXpp59e0bHB9TEjA5f20EMP6emnn9a2bds0dOjQqxojISFB58+f17Bhw2S1WlW1alVlZ2fr9ddfV//+/TV06FCdPXtWS5cuVXR0tD7//HPdcsst9u2HDBmiZcuWqUuXLnrkkUd04cIFffLJJ0pKSnKYRfqrjIwM3X777fr99981evRoBQQEaPny5erevbveeecd9erVy6H/zJkz5ebmpvHjxysrK0uzZ8/WgAEDtG/fvis6xj59+qh27dqKj49XUlKS5s+fr99++01vvvmmQ78dO3ZozZo1GjlypKpVq6batWvr22+/1R133CFfX19NmDBBHh4eeu2119SuXTvt3r1bLVu2dBhj1KhRCgoK0tSpU5WUlKTFixfL399fn332mWrVqqUZM2Zo06ZNeuGFF9S4cWM9/PDD9m0fffRRLVu2TIMGDdLo0aN15MgR/etf/9LBgwf16aefysPDQ5I0efJkTZ8+Xffcc4/uueceHThwQHfffbfy8vIu+1wUjn/rrbcqPj5eGRkZevnll/Xpp5/q4MGD8vf3L3Hb9PR0tW/fXhcuXNDEiRNVqVIlLV68uNjZwBUrVig2NlbR0dGaNWuWfv/9dy1cuFBt2rTRwYMHS7ygtkWLFqpTp47WrFmj2NhYh3WrV69WlSpVFB0dfdnjvNjzzz+vSZMmqU+fPnrkkUd06tQpvfLKK7rzzjsvedyGYah79+7auXOnhgwZoltuuUVbt27VU089pV9++UVz58695H6XLl2qRx99VLfffrvGjBmj//73v+revbuqVq2q0NBQez+bzabu3btrz549GjZsmBo0aKCvv/5ac+fO1Q8//KCNGzdK+jNIduvWTU2aNNG0adNktVr1448/OgSPP/74Qx07dlRaWppGjx6tkJAQrVixQjt27ChS344dO9SlSxdFRkZqypQpcnNzU0JCgjp06KBPPvlEt912W6mfa7gYA3CihIQEQ5LxxRdflNjHz8/PaNasmX25bdu2Rtu2bYv0i42NNcLCwuzLR44cMSQZvr6+xsmTJx36XrhwwcjNzXVo++2334zAwEBj8ODB9rYdO3YYkozRo0cX2Z/NZrP/OywszIiNjbUvjxkzxpBkfPLJJ/a2s2fPGuHh4Ubt2rWNgoICwzAMY+fOnYYko0GDBg71vPzyy4Yk4+uvvy7hWfnTlClTDElG9+7dHdoff/xxQ5Lx1Vdf2dskGW5ubsa3337r0Ldnz56Gp6encfjwYXvb8ePHjcqVKxt33nmnva3wtYqOjnY49qioKMNisRjDhw+3t124cMGoWbOmw+v0ySefGJKMlStXOux/y5YtDu0nT540PD09ja5duzrs5+mnnzYkOTzPhc/fzp07DcMwjLy8PKNGjRpG48aNjT/++MPe74MPPjAkGZMnTy7xuTSM/3vd9u3bZ287efKk4efnZ0gyjhw5YhjGn6+lv7+/MXToUIft09PTDT8/vyLtF4uLizM8PDyMM2fO2Ntyc3MNf39/h/ffxe/pQoWve6GjR48a7u7uxvPPP+/Q7+uvvzYqVKjg0H7xmBs3bjQkGdOnT3fY9r777jMsFovx448/lngchc/3Lbfc4vD+Xbx4sSHJ4fVfsWKF4ebm5vAzYRiGsWjRIkOS8emnnxqGYRhz5841JBmnTp0qcb/z5s0zJBlr1qyxt+Xk5Bg33nijw/vBZrMZ9erVK/Ke/f33343w8HDjrrvuKnEfMA9OLcHl+fj4/K27l2JiYlS9enWHNnd3d/t1MjabTWfOnNGFCxfUokULHThwwN5v3bp1slgsmjJlSpFxi5vaL7Rp0ybddtttatOmjcNxDBs2TEePHtV3333n0H/QoEEO1+3ccccdkv48PXUlRowY4bA8atQoex1/1bZtWzVs2NC+XFBQoG3btqlnz56qU6eOvT04OFgPPPCA9uzZo+zsbIcxhgwZ4nDsLVu2lGEYGjJkiL3N3d1dLVq0cKh/7dq18vPz01133aVff/3V/oiMjJSPj4/9tN727duVl5enUaNGOexnzJgxl30e9u/fr5MnT+rxxx93uHama9euioiIKHJq72KbNm1Sq1atHP5Kr169ugYMGODQ76OPPlJmZqb69+/vcCzu7u5q2bJlsaco/6pv377Kz8/X+vXr7W3btm1TZmam+vbte9njvNj69etls9nUp08fh3qCgoJUr169S9azadMmubu7a/To0Q7tTz75pAzD0ObNm0vctvD5Hj58uMP7d+DAgfLz83Pou3btWjVo0EAREREONXbo0EGS7DUWzhy9++67JZ7S27Rpk4KDg3XffffZ2ypWrKhhw4Y59Pvyyy+VmpqqBx54QKdPn7bvMycnRx07dtTHH39c4j5gHpxagss7d+6catSocdXbh4eHF9u+fPlyvfTSS/r++++Vn59fbP/Dhw8rJCREVatWLdU+f/rppyKnZCSpQYMG9vWNGze2t9eqVcuhX5UqVSSpyLUjJalXr57Dct26deXm5lbkc08ufi5OnTql33//XfXr1y+2VpvNpmPHjqlRo0Yl1lr4C+uvpxEK2/9af2pqqrKyskp8LU+ePCnpz+emuGOqXr26/XkpSeG2xR1PRESE9uzZc9nti3vdLh4vNTVVkuy/hC/m6+t7yf00bdpUERERWr16tT0Arl69WtWqVStxzEtJTU2VYRhFnrNChafsivPTTz8pJCRElStXdmj/63v1UttKRV8rDw8Ph2BcWOOhQ4eK/FFRqPD179u3r15//XU98sgjmjhxojp27KjevXvrvvvus98Z+NNPP+nGG28s8sdESa/Txafw/iorK+uy7yu4NoIMXNrPP/+srKws3XjjjfY2i8VS7EWIBQUFxY5R3PUNb731lgYOHKiePXvqqaeeUo0aNeTu7q74+HgdPny47A7gCrm7uxfbXtxxXomSZovK4s6vkmotrv2v9dtsNtWoUUMrV64sdvuSfsG5osK/4lesWKGgoKAi6ytUuPx/rX379tXzzz+vX3/9VZUrV9Z7772n/v37O2xb0ut48XvdZrPJYrFo8+bNxb4OPj4+l62nvNlsNt18882aM2dOsesLg7C3t7c+/vhj7dy5Ux9++KG2bNmi1atXq0OHDtq2bVuJ77+S9ilJL7zwgsN1b3/lCs8N/h6CDFzaihUrJMnh4scqVaoUe8rlUn85Xuydd95RnTp1tH79eodfFhefQqpbt662bt2qM2fOlGpWJiwsTCkpKUXav//+e/v6spSamuow2/Ljjz/KZrNd9hNcq1evrooVK5ZYq5ubW5GZlqtVt25dbd++Xa1bt75koCp8blJTUx3+qj916tRlZ6gKt01JSSkys5GSknLZ5z0sLMz+V/zF2158LJJUo0YNderU6ZJjlqRv376aOnWq1q1bp8DAQGVnZ6tfv34OfapUqaLMzMwi2178Xq9bt64Mw1B4eLhuuummUtURFham7du36+zZsw6zMlfyXv3ra/XX5zs/P19HjhxR06ZNHWr86quv1LFjx0uelpX+vK2+Y8eO6tixo+bMmaMZM2bon//8p3bu3KlOnTopLCxM33zzjQzDcBirpNfJ19f3ql8nuD6ukYHL2rFjh5577jmFh4c7XKNQt25dff/99zp16pS97auvvirV7ZSFf9X9dcZg37592rt3r0O/mJgYGYahqVOnFhnjUrMl99xzjz7//HOH8XJycrR48WLVrl3b4TqVsrBgwQKH5VdeeUXSn5/Pcynu7u66++679e677zqchsrIyNCqVavUpk2by54muVJ9+vRRQUGBnnvuuSLrLly4YP+F3alTJ3l4eOiVV15xeI7nzZt32X20aNFCNWrU0KJFixxuxd28ebMOHTqkrl27XnL7e+65R0lJSfr888/tbadOnSoyixQdHS1fX1/NmDHD4bTkX7e5nAYNGujmm2/W6tWrtXr1agUHB+vOO+906FO3bl1lZWXpP//5j73txIkT2rBhg0O/3r17y93dXVOnTi3yvjQMQ6dPn77kMRcUFOhf//qXQ/vcuXNlsVgu+R5q0aKFqlevrkWLFjncUbZs2bIiAaxPnz765ZdftGTJkiLj/PHHH8rJyZEknTlzpsj6wtmUwtf0nnvu0fHjx/XOO+/Y+/z+++9avHixw3aRkZGqW7euXnzxRZ07d67IuFfyOsH1MSMDl7B582Z9//33unDhgjIyMrRjxw599NFHCgsL03vvvedw4ebgwYM1Z84cRUdHa8iQITp58qQWLVqkRo0aFbkwtSTdunXT+vXr1atXL3Xt2lVHjhzRokWL1LBhQ4f/8Nq3b6+HHnpI8+fPV2pqqjp37iybzaZPPvlE7du318iRI4sdf+LEifr3v/+tLl26aPTo0apataqWL1+uI0eOaN26dSV+CvDVOnLkiLp3767OnTtr7969euutt/TAAw84/EVckunTp9s/t+Pxxx9XhQoV9Nprryk3N1ezZ88usxrbtm2rRx99VPHx8fryyy919913y8PDQ6mpqVq7dq1efvll3XfffapevbrGjx+v+Ph4devWTffcc48OHjyozZs3q1q1apfch4eHh2bNmqVBgwapbdu26t+/v/3269q1a2vs2LGX3H7ChAlasWKFOnfurCeeeMJ++3VYWJhDmPD19dXChQv10EMPqXnz5urXr5+qV6+utLQ0ffjhh2rdunWRYFCcvn37avLkyfLy8tKQIUOKvC/69eunf/zjH+rVq5dGjx5tv8X7pptucrgovW7dupo+fbri4uJ09OhR9ezZU5UrV9aRI0e0YcMGDRs2TOPHjy+2hnvvvVft27fXP//5Tx09elRNmzbVtm3b9O6772rMmDH2WY2Snu/p06fr0UcfVYcOHdS3b18dOXJECQkJRa6Reeihh7RmzRoNHz5cO3fuVOvWrVVQUKDvv/9ea9as0datW9WiRQtNmzZNH3/8sbp27aqwsDCdPHlSr776qmrWrGm/eH7o0KH617/+pYcffljJyckKDg7WihUrVLFiRYd9urm56fXXX1eXLl3UqFEjDRo0SDfccIN++eUX7dy5U76+vnr//fcv+zrBxTnjVimgUOEtvYUPT09PIygoyLjrrruMl19+2cjOzi52u7feesuoU6eO4enpadxyyy3G1q1bS7z9+oUXXiiyvc1mM2bMmGGEhYUZVqvVaNasmfHBBx8Ue7vrhQsXjBdeeMGIiIgwPD09jerVqxtdunQxkpOT7X0uvv3aMAzj8OHDxn333Wf4+/sbXl5exm233WZ88MEHDn0Kbx9eu3atQ3th7QkJCZd8/gpvw/3uu++M++67z6hcubJRpUoVY+TIkQ63HxvGn7dfjxgxothxDhw4YERHRxs+Pj5GxYoVjfbt2xufffaZQ5+SbpUvrOHi22VjY2ONSpUqFdnX4sWLjcjISMPb29uoXLmycfPNNxsTJkwwjh8/bu9TUFBgTJ061QgODja8vb2Ndu3aGd98802R5/ni268LrV692mjWrJlhtVqNqlWrGgMGDDB+/vnnEp/Hv/rPf/5jtG3b1vDy8jJuuOEG47nnnjOWLl3qcPv1X/cfHR1t+Pn5GV5eXkbdunWN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AQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApkWQAQAApuXUILNw4UI1adJEvr6+8vX1VVRUlDZv3mxff/78eY0YMUIBAQHy8fFRTEyMMjIynFgxAABwJU4NMjVr1tTMmTOVnJys/fv3q0OHDurRo4e+/fZbSdLYsWP1/vvva+3atdq9e7eOHz+u3r17O7NkAADgQio4c+f33nuvw/Lzzz+vhQsXKikpSTVr1tTSpUu1atUqdejQQZKUkJCgBg0aKCkpSa1atXJGyQAAwIW4zDUyBQUFevvtt5WTk6OoqCglJycrPz9fnTp1sveJiIhQrVq1tHfv3hLHyc3NVXZ2tsMDAABcn5weZL7++mv5+PjIarVq+PDh2rBhgxo2bKj09HR5enrK39/foX9gYKDS09NLHC8+Pl5+fn72R2hoaDkfAQAAcBanB5n69evryy+/1L59+/TYY48pNjZW33333VWPFxcXp6ysLPvj2LFjZVgtAABwJU69RkaSPD09deONN0qSIiMj9cUXX+jll19W3759lZeXp8zMTIdZmYyMDAUFBZU4ntVqldVqLe+yAQCAC3D6jMzFbDabcnNzFRkZKQ8PDyUmJtrXpaSkKC0tTVFRUU6sEAAAuAqnzsjExcWpS5cuqlWrls6ePatVq1Zp165d2rp1q/z8/DRkyBCNGzdOVatWla+vr0aNGqWoqCjuWAIAAJKcHGROnjyphx9+WCdOnJCfn5+aNGmirVu36q677pIkzZ07V25uboqJiVFubq6io6P16quvOrNkAADgQpwaZJYuXXrJ9V5eXlqwYIEWLFhwjSoCAABm4nLXyAAAAFwpggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwAADAtggwA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o+ufffZZ3XLLLZfcZuDAgerZs2e51gXAOQgyAK6pU6dO6bHHHlOtWrVktVoVFBSk6Ohoffrpp1c13vjx45WYmFjGVQIwC75rCcA1FRMTo7y8PC1fvlx16tRRRkaGEhMTdfr06asaz8fHRz4+PmVcJQCzYEYGwDWTmZmpTz75RLNmzVL79u0VFham2267TXFxcerevbukP78J+eabb1alSpUUGhqqxx9/XOfOnStxzItPLRUUFGjcuHHy9/dXQECAJkyYoIu/Um7Lli1q06aNvU+3bt10+PDhcjlmAOWLIAPgmimcPdm4caNyc3OL7ePm5qb58+fr22+/1fLly7Vjxw5NmDDhivfx0ksvadmyZXrjjTe0Z88enTlzRhs2bHDok5OTo3Hjxmn//v1KTEyUm5ubevXqJZvN9reOD8C1x7dfA7im1q1bp6FDh+qPP/5Q8+bN1bZtW/Xr109NmjQptv8777yj4cOH69dff5X058W+Y8aMUWZmpqQ/Z2Q2btyoL7/8UpIUEhKisWPH6qmnnpIkXbhwQeHh4YqMjNTGjRuL3cevv/6q6tWr6+uvv1bjxo3L9HgBlC9mZABcUzExMTp+/Ljee+89de7cWbt27VLz5s21bNkySdL27dvVsWNH3XDDDapcubIeeughnT59Wr///vtlx87KytKJEyfUsmVLe1uFChXUokULh36pqanq37+/6tSpI19fX9WuXVuSlJaWVmbHCeDaIMgAuOa8vLx01113adKkSfrss880cOBATZkyRUePHlW3bt3UpEkTrVu3TsnJyVqwYIEkKS8vr8z2f++99+rMmTNasmSJ9u3bp3379pX5PgBcGwQZAE7XsGFD5eTkKDk5WTabTS+99JJatWqlm266ScePH7/icfz8/BQcHGwPJtKfp5aSk5Pty6dPn1ZKSoqeeeYZdezYUQ0aNNBvv/1WpscD4Nrh9msA18zp06d1//33a/DgwWrSpIkqV66s/fv3a/bs2erRo4duvPFG5efn65VXXtG9996rTz/9VIsWLSrVPp544gnNnDlT9erVU0REhObMmWO/nkaSqlSpooCAAC1evFjBwcFKS0vTxIkTy/hIAVwrBBkA14yPj49atmypuXPn6vDhw8rPz1doaKiGDh2qp59+Wt7e3pozZ45mzZqluLg43XnnnYqPj9fDDz98xft48skndeLECcXGxsrNzU2DBw9Wr169lJWVJenPu6LefvttjR49Wo0bN1b9+vU1f/58tWvXrpyOGkB54q4lAABgWlwjAwAATIsgAwAATIsgAwAATIsgAwAATIsgAwAATIsgAwAATIsgAwAATIsgAwAATIsgAwAATIsgAwAATIsgAwAATOv/AQO4rEAnISf9AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(y = 'Tiempo', data=df_vuelos_lisboa, x= 'Salida')\n",
    "plt.title('Duración promedio de vuelo desde')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Esta ruta no suele tener escalas, no tiene más que el promedio de su mismo recorrido."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
