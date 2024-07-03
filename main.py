from functions import select_pantallas, panel_data, db_insertion
from datetime import datetime, date, timedelta
import warnings
warnings.filterwarnings('ignore')

df = select_pantallas()

start_date = date(2024, 7, 2)
start_date = 'filters[start_date]=' + str(start_date) + ' 00:00:00'

end_date = date(2024, 7, 3)
end_date = 'filters[end_date]=' + str(end_date) + ' 00:00:00'

for i in range(len(df)):
    id_pantalla = df['id_pantalla'][i]
    id_api = df['api_pantalla'][i]
    print(id_api)
    df_data = panel_data(id_api, start_date, end_date)
    df_data['id_pantalla'] = id_pantalla
    #df_data['api_pantalla'] = id_api #MOSTRAR EL ID_API
    #print(df_data)
    db_df = df_data.copy(deep=True)
    db_insertion(db_df)
    print(f'{len(df_data)} filas han sido insertadas a la BD exitosamente!')

