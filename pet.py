import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

#capitura e executa a leitura da chave no arquivo em  memoria
load_dotenv()
st.set_page_config(page_title="Dr.PetIA", page_icon="🐾")

#Estabelece a conecção com a API dO GEMINI usando a chave salva posteriormente
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# Customização Visual com CSS
st.markdown("""
    <style>
    /* Fundo em gradiente: verde-claro acolhedor no topo suavizando para a base */
    .stApp {
        background: linear-gradient(180deg, #dcfce7 0%, #f0fdf4 100%) !important;
    }

    /* Título principal e subtítulo */
    h1 {
        color: #065f46 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
    }

    /* Rótulos dos campos em verde escuro com boa leitura */
    label, div[data-testid="stWidgetLabel"] p {
        color: #047857 !important;
        font-weight: bold !important;
    }

    /* Caixas de input com fundo suave e texto escuro visível */
    input, textarea, div[role="combobox"] {
        color: #0f172a !important;
        background-color: #ffffff !important;
    }

    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div, 
    textarea {
        background-color: #ffffff !important;
        border: 1px solid #a7f3d0 !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.03) !important;
    }

    /* Botão Principal */
    div.stButton > button {
        background-color: #059669 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: bold !important;
        box-shadow: 0 4px 6px rgba(5, 150, 105, 0.2) !important;
    }

    div.stButton > button:hover {
        background-color: #047857 !important;
    }
    </style>
""", unsafe_allow_html=True)
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
    sintomas = st.text_area("Sintomas Observados:", placeholder="🔎Conte os sinais e sintomas que você observou.")
    audio_input = st.audio_input("Ou grave um audio descrevendo os sintomas")

st.divider()
#Botão de envio com integração com a api

# Botão de Envio
if st.button("Analisar Sintomas", type="primary"):
    if not sintomas:
        st.warning("Por favor, descreva os sintomas do pet para continuar.")
    else:
        with st.spinner("Analisando sintomas com o Gemini..."):
            try:
                # O "f" antes das aspas faz a interpolação das variáveis do formulário
                prompt_completo = f"""
                Você é o Dr.PetIA, um assistente virtual especialista em triagem veterinária inicial.
                Sua função é analisar os sintomas informados pelo tutor e fornecer:
                1. Nível de Urgência estimado (Baixo, Médio ou Alto/Emergência).
                2. Possíveis causas comuns (sempre ressaltando que são hipóteses).
                3. Primeiros socorros ou orientações de conforto enquanto aguarda atendimento.
                4. Recomendação clara sobre a necessidade de ir a um hospital veterinário 24h.

                Mantenha um tom empático, direto e responsável. Nunca dê diagnósticos definitivos.
                ---
                DADOS DO PET:
                - Espécie: {especie}
                - Idade: {idade}
                - Porte: {porte}
                - Sintomas observados: {sintomas}
                """
                # Chamada direta para o modelo Gemini 2.5 Flash
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt_completo,
                )
                #exibição de resultado na tela pro usuario
                st.success("Análise concluida!")
                st.markdown("### 📋 Avaliação Preliminar:")
                st.write(response.text)

            except Exception as e:
                st.error(f"ERRO ao conectar com API: {e}")