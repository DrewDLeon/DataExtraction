import os
from dotenv import load_dotenv
import pyodbc
import pandas as pd
import mysql.connector as mysql
from sqlalchemy import create_engine, URL
from sqlalchemy.types import *
from clases import params, api_url, api_credentials
import requests

load_dotenv()

def select_pantallas():
    query = f'''
        SELECT id_pantalla, api_pantalla
        FROM tbl_pantallas
    '''

    database = params()

    db = mysql.connect(
        user = database.user,
        password = database.password,
        database = database.database,
        host = database.host,
        port = database.port
    )

    dataCursor = db.cursor()
    db_query = pd.read_sql_query(
        query, db
    )

    df = pd.DataFrame(db_query)
    db.close()
    dataCursor.close()

    return df


def panel_data(id_api, fecha_inicio, fecha_fin):
    #CREDENTIALS
    credentials = api_credentials()
    access_token = credentials.token
    customer_hash = credentials.customer_hash

    #URL
    urls = api_url()
    panel_data_url = urls.data
    panel_data_url += f'{id_api}?{fecha_inicio}&{fecha_fin}'

    response = requests.request(
        'GET',
        panel_data_url,
        headers = {
            "api-token":access_token,
            "customer-hash":customer_hash
        }
    )
    data = response.json()

    df = pd.json_normalize(data['body']['data'])

    # Colocamos la fecha en formato datetime
    df['event_date'] = pd.to_datetime(df['event_date'])

    df = df.groupby(['event_date'])['total'].sum().reset_index()

    return df

    
def db_insertion(df):
    db = params()
    df.rename(columns={'event_date':'fechayhora'},inplace=True)
    df.rename(columns={'total':'total_impactos'},inplace=True)

    # NOS ASEGURAMOS QUE LOS TIPOS DE DATOS ESTEN CORRECTOS
    df['total_impactos'] = df['total_impactos'].astype(float)
    df['id_pantalla'] = df['id_pantalla'].astype(int)

    engine = create_engine(f'mysql+mysqlconnector://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}')

    df_schema = {
    "id_impacto":INT,
    "id_pantalla":INT,
    "fechayhora":DATETIME,
    "total_impactos":FLOAT
    }

    df.to_sql(
        'tbl_impactos',
        con=engine,
        if_exists='append',
        index=False,
        dtype=df_schema
    )