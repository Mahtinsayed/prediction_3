import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import base64

st.write("""
# Penguin Prediction App

This app predicts the **Palmer Penguin** species!

Data obtained from the [palmerpenguins library](https://drive.google.com/file/d/13UAb77GVcWiCNYy17ZzQuaX7GVq9I1jy/view?usp=sharing) in R by Allison Horst.
""")

st.sidebar.header('User Input Features')



# Web scraping of S&P 500 data
#
@st.cache
def load_data():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQWPoM1zq7FrW06SYxMIWboclt5FQoRB_rgWFRjzhvY-YN9NlZbm_TaB4Je2e0KulhGX8BmD3inUhI1/pub?gid=775382138&single=true&output=csv'
    html = pd.read_html(url, header = 0)
    df = html[0]
 
return df

df = load_data()

