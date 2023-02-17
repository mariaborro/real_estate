import numpy as np
import pandas as pd

data=pd.read_csv('raw_data/houses_Madrid.csv')

def prepare(df):
    nan_is_false=["has_ac","fitted_wardrobes", "has_pool", "has_terrace", "has_balcony", "storage_room", "is_accessible"]
    for column in nan_is_false:
        df[column]=df[column].fillna(False)
    df['has_lift'] = df['has_lift'].fillna(1)
    df['is_new']=df['is_new'].fillna(False)
    return df