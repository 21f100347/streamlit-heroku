import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Credit Card Approval Prediction App

This app predicts the credit card approval probablity
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    number_one = st.number_input("NUMBER_ONE",min_value=0,max_value=9999,step=1)
    number_two = st.number_input("NUMBER_TWO",min_value=0,max_value=9999,step=1)


    data = {'NUMBER_ONE': number_one,
            'NUMBER_TWO': number_two
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Preprocessing

continous_features = ['NUMBER_ONE','NUMBER_TWO']


for col in df.columns:
    if df[col].dtype != 'float64':
        df[col] = df[col].values.astype('float64')


st.subheader('RESULTS')
st.write(df['NUMBER_ONE'][0] -df['NUMBER_TWO'][0] )
