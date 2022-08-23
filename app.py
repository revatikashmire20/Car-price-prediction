import numpy as np
import pandas as pd
import streamlit as st
import pickle
import sklearn

model = pickle.load(open("random_forest_regression_model.pkl", "rb"))

Seller_Type = ['Dealer', 'Individual']
Transmission = ['Manual', 'Automatic']
Fuel_type = ['Petrol', 'Diesel', 'CNG']
owner = [0, 1, 3]

st.title("Car price prediction")
col1, col2, col3 = st.columns(3)

with col1:
    seller_type = st.selectbox("Select the seller type", Seller_Type)
with col2:
    transmission = st.selectbox("Select the transmission",Transmission)
with col3:
    fuel_type = st.selectbox("Select the fuel type",Fuel_type)

col4, col5 = st.columns(2)

with col4:
    owener = st.selectbox("Select the owner",owner)
with col5:
    year = st.number_input("No of year car purchased year")

col6, col7,= st.columns(2)


with col6:
    present_price = st.number_input("enter the present price")
with col7:
    Kms_Driven = st.number_input("enter the kms driven")

if seller_type == "Dealer":
    seller_type = 1
else:
    seller_type =0

if seller_type == "Individual":
    seller_type_individual = 0
else:
    seller_type_individual = 1

if transmission == "Manual":
    transmission_manual = 1
else:
    transmission_manual = 0

if transmission == "Automatic":
    transmission_automatic = 0
else:
    transmission_automatic = 1

if fuel_type == "Petrol":
    fuel_type_petrol = 1
else:
    fuel_type_petrol = 0

if fuel_type == "Diesel":
    fuel_type_diesel = 1
else:
    fuel_type_diesel = 0

if fuel_type == "CNG":
    fuel_type_CNG = 1
else:
    fuel_type_CNG = 0

input = {"present_price":[present_price],"Kms_Driven":[Kms_Driven],"Owner" : [owener], "no_year":[year],"Fuel_Type_Diesel":[fuel_type_diesel],"Fuel_Type_Petrol":[fuel_type_petrol], "Seller_Type_Individual": [seller_type_individual], "Transmission_Manual":[transmission_manual] }


if st.button("Calculate the price"):
    df = pd.DataFrame(input)
    st.table(df)
    prediction =model.predict(df)
    st.header(prediction)