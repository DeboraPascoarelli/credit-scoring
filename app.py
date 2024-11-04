import streamlit as st
import pandas as pd

dados = pd.read_csv('df_clean.csv')


st.write('# Simulador de avaliação de crédito') 

st.write('### Idade')
input_idade = float(st.slider('Selecione sua idade', 18,100))

st.write('### Nível de escolaridade')
input_grau_escolaridade = st.selectbox('Qual é o sue grau de escolaridade?', dados['Grau_escolaridade'].unique())
