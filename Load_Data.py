import pandas as pd
import numpy as np

def load_data(data):
    '''Функция приведения в нормальный вид данные'''

    df = pd.read_csv(data, encoding='Windows-1251')
    df[['Количество больничных дней', 'Возраст', 'Пол']] \
        = df['Количество больничных дней,"Возраст","Пол"'].str.split(',', expand=True)
    df.drop('Количество больничных дней,"Возраст","Пол"', axis=1, inplace=True)
    df['Количество больничных дней'] = df['Количество больничных дней'].astype(np.int32)
    df['Возраст'] = df['Возраст'].astype(np.int32)
    return df