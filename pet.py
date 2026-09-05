import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

#capitura e executa a leitura da chave no arquivo em  memoria
load_dotenv()

#Estabelece a conecção com a API da OpenAI usando a chave salva posteriormente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Apresentação e estrutura da pag do app

st.title("🐾 Dr.PetIA - Triagem Veterinária")
st.write("Preencha as informações do seu pet para receber uma orientação preliminar.")

st.divider()

#Organização da entrada de dados
col1, col2 =st.columns(2)

with col1:
    espécie = st.selectbox("Espécie:", ["Cachorro", "Gato","Coelho","Hamster","Peixe","Tartaruga","Calopsita","Papagaio","Outros"])
    idade = st.text_input("Idade Aproximada:", placeholder="Ex: 2 anos")

with col2:
    porte = st.selectbox("Porte de Animal:", ["Pequeno","Médio","Grande"])
    sintomas = st.text_area("Sintomas Observados:", placeholder="apatia e falta de apetite")
