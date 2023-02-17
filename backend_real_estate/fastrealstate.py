import numpy as np
from preprocess_realestate import prepare
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

app.state.model = joblib.load("model_realestate_XGB")

@app.get("/")
def home():
    return {"Message": "Welcome to our Real Estate Predictor!"}

#as a reminder now we can run this code in our command line: uvicorn fastrealstate:app --reload

@app.get('/predict')
async def make_prediction(sq_metres, rooms, bathrooms, needs_renewal, is_new, has_ac,
                          fitted_wardrobes, has_lift, is_exterior, has_pool, has_terrace,
                          has_balcony, storage_room, is_accessible, has_parking,
                          Casa , Aticos, district_id_1, district_id_10, district_id_11,
                          district_id_12, district_id_13, district_id_14, district_id_15,
                          district_id_17, district_id_18, district_id_19, district_id_2,
                          district_id_20, district_id_3, district_id_4, district_id_5, district_id_6,
                          district_id_7, district_id_8, district_id_9
                          ):
    """Returns the prediction of a pasted text
    """
    all_elements = [[float(sq_metres), int(rooms), int(bathrooms), bool(needs_renewal), bool(is_new), bool(has_ac),
                          bool(fitted_wardrobes), bool(has_lift), bool(is_exterior), bool(has_pool), bool(has_terrace),
                          bool(has_balcony), bool(storage_room), bool(is_accessible), bool(has_parking),
                          int(Casa) , int(Aticos), int(district_id_1), int(district_id_10), int(district_id_11),
                          int(district_id_12), int(district_id_13), int(district_id_14), int(district_id_15),
                          int(district_id_17), int(district_id_18), int(district_id_19), int(district_id_2),
                          int(district_id_20), int(district_id_3), int(district_id_4), int(district_id_5), int(district_id_6),
                          int(district_id_7), int(district_id_8), int(district_id_9)]]

    df_elements = pd.DataFrame (all_elements, columns = ['sq_metres', 'rooms', 'bathrooms', 'needs_renewal', 'is_new', 'has_ac',
       'fitted_wardrobes', 'has_lift', 'is_exterior', 'has_pool',
       'has_terrace', 'has_balcony', 'storage_room', 'is_accessible',
       'has_parking', 'HouseType 2: Casa o chalet', 'HouseType 5: Áticos',
       'district_id_1', 'district_id_10', 'district_id_11', 'district_id_12',
       'district_id_13', 'district_id_14', 'district_id_15', 'district_id_17',
       'district_id_18', 'district_id_19', 'district_id_2', 'district_id_20',
       'district_id_3', 'district_id_4', 'district_id_5', 'district_id_6',
       'district_id_7', 'district_id_8', 'district_id_9'])

    df_preprocessed = prepare(df_elements)

    prediction =  app.state.model.predict(df_preprocessed)

    price = str(prediction[0])

    return {"price": price}
