import requests
import pandas as pd


def extract_api_data(api_url, resource, client_id, client_secret):
    """
    Función para obtener datos en formato JSON de la API de transporte de CABA
    """
    url = api_url + resource
    url += "?client_id=" + client_id + "&client_secret=" + client_secret
    r = requests.get(url)
    return r.json()["data"]


def change_type_column(df, **kwargs):
    """
    Función para convertir el tipo de datos de una columna
    donde cada nombre de los parámetros a pasar será una columna
    del DataFrame y su respectivo valor será el nuevo tipo de dato
    para esa columna.
    Retorna el mismo DataFrame con las columnas con sus nuevos tipos
    de datos
    """
    for col, a_type in kwargs.items():
        df[col] = df[col].astype(a_type)
    return df


def split_column(df, column='num_bikes_available_types'):
    """
    Función para dividir la columna num_bikes_available_types
    y luego eliminarla
    """
    types = list(df[column][0].keys())
    for a_type in types:
        df["num_"+a_type+"_bikes_available"] = df[column].apply(lambda r: r[a_type])
    return df.drop(column, axis=1)


# Extract
api_url = "https://apitransporte.buenosaires.gob.ar/"
status_resource = "ecobici/gbfs/stationStatus"
with open("/home/guido/datadev/ecobici/credenciales.txt", "r") as file:
    client_id = file.readline().rstrip()
    client_secret = file.readline().rstrip()
stations = extract_api_data(api_url, status_resource, client_id, client_secret)

# To dataframe
df_stations = pd.DataFrame(stations["stations"])

# Transform stage
df_stations = change_type_column(df_stations,
                                 station_id='int64',
                                 is_returning='bool',
                                 is_renting='bool',
                                 is_installed='bool')
df_stations = split_column(df_stations)

df_stations_info = pd.read_csv('ecobici_info.csv')
df_stations.set_index('station_id', inplace=True)
df_stations = df_stations_info.join(df_stations, on='station_id', how='inner')


# To csv
df_stations.to_csv('ecobici.csv', index=False, mode='a+')