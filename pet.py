import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

#capitura e executa a leitura da chave no arquivo em  memoria
load_dotenv()

#Estabelece a conecção com a API da OpenAI usando a chave salva posteriormente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))