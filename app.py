import streamlit as st
import pandas as pd

dados = pd.read_csv('df_clean.csv')


st.write('# Simulador de avaliação de crédito') 

st.write('### Idade')
input_idade = float(st.slider('Selecione sua idade', 18,100))

st.write('### Nível de escolaridade')
input_grau_escolaridade = st.selectbox('Qual é o seu grau de escolaridade?', dados['Grau_escolaridade'].unique())

st.write('### Estado Civil')
input_estado_civil = st.selectbox('Qual é o seu estado civil?', dados['Estado_civil'].unique())

st.write('### Família')
membros_familia = float(st.slider('Selecione quantos membros na sua família', 18,20))

st.write('### Carro próprio')
input_carro_proprio = st.radio('Você possui um automóvel?', ['Sim', 'Não'])
input_carro_proprio_dict = {'Sim':1, 'Não': 0}
input_carro_proprio = input_carro_proprio_dict.get(input_carro_proprio)


st.write('### Casa própria')
input_casa_propria = st.radio('Você possui casa própria?', ['Sim', 'Não'])
input_casa_propria_dict = {'Sim':1, 'Não': 0}
input_casa_propria = input_casa_propria_dict.get(input_casa_propria)

st.write('### Tipo de residência')
input_tipo_moradia = st.selectbox ('Qual é o seu tipo de moradia?', dados['Moradia'].unique())

st.write('### Categoria de renda')
input_categoria_renda = st.selectbox ('Qual é a sua categoria de renda?', dados['Categoria_de_renda'].unique())

st.write('### Ocupação')
input_ocupacao = st.selectbox ('Qual é a sua ocupação?', dados['Ocupacao'].unique())

st.write('### Experiência')
input_tempo_experiencia = float(st.slider('Qual é o seu tempo de experiência', 0,30))

st.write('### Rendimentos')
input_rendimentos = float(st.number_input('Digite o seu rendimento anual e pressione Enter para confirmar', 0))
















######################################################################################################################
# Exemplo de publicação de um realtório de Power Bi

# URL do relatório Power BI incorporado (pegar em 'Publicar na Web' no Power BI)
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMWVmYzc0MmMtMDBhNi00NGFlLWJiOTEtY2NiNTgyM2NhMWEwIiwidCI6ImRlOTgwY2Y4LWYwYzctNGFlZC1iNjc2LTJlOTlkNjg2YzAzMyJ9" 

# Tamanho do iframe (ajuste conforme necessário)
iframe_width = 800
iframe_height = 600

# Título do App
st.title("Relatório Power BI no Streamlit")

# Exibir o relatório Power BI usando um iframe
st.components.v1.iframe(power_bi_url, width=iframe_width, height=iframe_height)

#############################################################################################################################





