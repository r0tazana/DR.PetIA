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
    especie = st.selectbox("Espécie:", ["Cachorro", "Gato","Coelho","Hamster","Peixe","Tartaruga","Calopsita","Papagaio","Outros"])
    idade = st.text_input("Idade Aproximada:", placeholder="Ex: 2 anos")

with col2:
    porte = st.selectbox("Porte de Animal:", ["Pequeno","Médio","Grande"])
    sintomas = st.text_area("Sintomas Observados:", placeholder="apatia e falta de apetite")

st.divider()
#Botão de envio com integração com a api

if st.button("Analisar Sintomas", type="primary"):
    if not sintomas:
        st.warning("Por favor, Descrava um sintoma para podemos iniciar a triagem.")
    else:
        with st.spinner("Analisando sintomas com a IA..."):
            try:
                #Instruções para IA em como ela deve agir e como o triador responsavel
                prompt_sistema = """
                Você é o Dr.PetIA, um assistente virtual especialista em triagem veterinária inicial.
                Sua função é analisar os sintomas informados pelo tutor e fornecer:
                1. Nível de Urgência estimado (Baixo, Médio ou Alto/Emergência).
                2. Possíveis causas comuns (sempre ressaltando que são hipóteses).
                3. Primeiros socorros ou orientações de conforto enquanto aguarda atendimento.
                4. Recomendação clara sobre a necessidade de ir a um hospital veterinário 24h.

                Mantenha um tom empático, direto e responsável. Nunca dê diagnósticos definitivos.
                """
                #Preenchimento das informações do formulario
                prompt_usuario = f"""
                Espécie: {especie}
                Idade: {idade}
                Porte: {porte}
                Sintomas observados: {sintomas}
                """

                #Envio da requisição para o ChatGPT

                resposta = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": prompt_usuario}
                    ],
                    temperature=0.7
                )
                #exibição de resultado na tela pro usuario
                st.success("Análise concluida!")
                st.markdown("### 📋 Avaliação Preliminar:")
                st.write(resposta.choices[0].message.content)

            except Exception as e:
                st.error(f"ERRO ao conectar com API: {e}")