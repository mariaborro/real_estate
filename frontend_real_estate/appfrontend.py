import streamlit as st
import requests

st.set_page_config(page_title="Real Estate Price Predictor", layout="wide")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.title('Welcome to our Real Estate Price Predictor!')

st.write("Now you can calculate how much your dream house would cost!!")

st.info("made by Maria Borrell with a XGBRegressor model")

st.subheader("Input the desired features below")

building_type = st.selectbox("building type", ["appartment", "attic", "house"])

if building_type == "appartment":
    Casa = 0
    Aticos = 0

if building_type == "attic":
    Casa = 0
    Aticos = 1

if building_type == "house":
    Casa = 1
    Aticos = 0

district = st.selectbox("district", ["Arganzuela", #1
                                          "Barajas", #2
                                          "Carabanchel", #3
                                          "Centro", #4
                                          "Chamartin", #5
                                          "Chamberi", #6
                                          "Ciudad Lineal", #7
                                          "Fuencarral", #8
                                          "Hortaleza", #9
                                          "Latina", #10
                                          "Moncloa", #11
                                          "Moratalaz", #12
                                          "Puente de Vallecas", #13
                                          "Retiro", #14
                                          "Salamanca", #15
                                          "Tetuan", #17
                                          "Usera", #18
                                          "Vicalvaro", #19
                                          "Villa de Vallecas", #20
                                          "Villaverde", #21
                                          "Other"])

district_id_1 = 0
district_id_2 = 0
district_id_3 = 0
district_id_4 = 0
district_id_5 = 0
district_id_6 = 0
district_id_7 = 0
district_id_8 = 0
district_id_9 = 0
district_id_10 = 0
district_id_11 = 0
district_id_12 = 0
district_id_13 = 0
district_id_14 = 0
district_id_15 = 0
district_id_17 = 0
district_id_18 = 0
district_id_19 = 0
district_id_20 = 0

if district == "Arganzuela":
    district_id_1 = 1

if district == "Barajas":
    district_id_2 = 1

if district == "Carabanchel":
    district_id_3 = 1

if district == "Centro":
    district_id_4 = 1

if district == "Chamartin":
    district_id_5 = 1

if district == "Chamberi":
    district_id_6 = 1

if district == "Ciudad Lineal":
    district_id_7 = 1

if district == "Fuencarral":
    district_id_8 = 1

if district == "Hortaleza":
    district_id_9 = 1

if district == "Latina":
    district_id_10 = 1

if district == "Moncloa":
    district_id_11 = 1

if district == "Moratalaz":
    district_id_12 = 1

if district == "Puente de Vallecas":
    district_id_13 = 1

if district == "Retiro":
    district_id_14 = 1

if district == "Salamanca":
    district_id_15 = 1

if district == "Tetuan":
    district_id_17 = 1

if district == "Usera":
    district_id_18 = 1

if district == "Vicalvaro":
    district_id_19 = 1

if district == "Villa de Vallecas":
    district_id_20 = 1

sq_metres = st.text_input("square meters:")

rooms = st.select_slider("number of rooms:", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

bathrooms = st.select_slider("number of bathrooms:", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

needs_renewal = st.selectbox("needs renovation", ["no", "yes"])

if needs_renewal == "no":
    needs_renewal = "False"
else:
    needs_renewal = "True"

is_new = st.selectbox("is new", ["no", "yes"])

if is_new == "no":
    is_new = "False"
else:
    is_new = "True"

has_ac = st.selectbox("has AC", ["no", "yes"])

if has_ac == "no":
    has_ac = "False"
else:
    has_ac = "True"

fitted_wardrobes = st.selectbox("has fitted wardrobes", ["no", "yes"])

if fitted_wardrobes == "no":
    fitted_wardrobes = "False"
else:
    fitted_wardrobes = "True"

has_lift = st.selectbox("has lift", ["no", "yes"])

if has_lift == "no":
    has_lift = "False"
else:
    has_lift = "True"

is_exterior = st.selectbox("is exterior", ["no", "yes"])

if is_exterior == "no":
    is_exterior = "False"
else:
    is_exterior = "True"

has_pool = st.selectbox("has pool", ["no", "yes"])

if has_pool == "no":
    has_pool = "False"
else:
    has_pool = "True"

has_terrace = st.selectbox("has terrace", ["no", "yes"])

if has_terrace == "no":
    has_terrace = "False"
else:
    has_terrace = "True"

has_balcony = st.selectbox("has balcony", ["no", "yes"])

if has_balcony == "no":
    has_balcony = "False"
else:
    has_balcony = "True"

storage_room = st.selectbox("has storage room", ["no", "yes"])

if storage_room == "no":
    storage_room = "False"
else:
    storage_room = "True"

is_accessible = st.selectbox("is accessible", ["no", "yes"])

if is_accessible == "no":
    is_accessible = "False"
else:
    is_accessible = "True"

has_parking = st.selectbox("has parking", ["no", "yes"])

if has_parking == "no":
    has_parking = "False"
else:
    has_parking = "True"

predict_btt = st.button("PREDICT")

url = "http://127.0.0.1:8000/predict"

if predict_btt:
    with st.spinner("Please wait :)"):
        with requests.Session() as session:
            response = session.get(url, params= {"sq_metres": sq_metres, "rooms":rooms, "bathrooms":bathrooms,
                                                 "needs_renewal":needs_renewal, "is_new":is_new,
                                                 "has_ac":has_ac, "fitted_wardrobes":fitted_wardrobes,
                                                 "has_lift":has_lift, "is_exterior":is_exterior,
                                                 "has_pool":has_pool, "has_terrace":has_terrace,
                                                 "has_balcony":has_balcony, "storage_room":storage_room,
                                                 "is_accessible":is_accessible, "has_parking":has_parking,
                                                 "Casa":Casa, "Aticos":Aticos, "district_id_1":district_id_1,
                                                 "district_id_10":district_id_10, "district_id_11":district_id_11,
                                                 "district_id_12":district_id_12, "district_id_13":district_id_13,
                                                 "district_id_14":district_id_14, "district_id_15":district_id_15,
                                                 "district_id_17":district_id_17, "district_id_18":district_id_18,
                                                 "district_id_19":district_id_19, "district_id_2":district_id_2,
                                                 "district_id_20":district_id_20, "district_id_3":district_id_3,
                                                 "district_id_4":district_id_4, "district_id_5":district_id_5,
                                                 "district_id_6":district_id_6, "district_id_7":district_id_7,
                                                 "district_id_8":district_id_8, "district_id_9":district_id_9})
            result = response.json()["price"]
            st.markdown(f"The fair price for a home with these characteristics is: {result} euros!!")
            st.balloons()
            print(response.status_code)
            print(response.content)
            print(response.json())


# as a reminder, after activating uvicorn with uvicorn fastrealstate:app --reload we can run in our command line: streamlit run appfrontend.py
