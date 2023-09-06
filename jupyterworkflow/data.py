import pandas as pd
import os
from urllib.request import urlretrieve

URL="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_data(filename='Fremont.csv', url=URL):
    if not os.path.exists(filename):
        urlretrieve(url, filename)
    
    data = pd.read_csv(filename, index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%
        Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    
    data.columns = ['Total', 'West', 'East']
    return data
    