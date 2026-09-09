# Dr.PetIA - Triagem Veterinária Inicial

Aplicação web desenvolvida para auxiliar tutores na triagem preliminar de sintomas em animais de estimação, fornecendo direcionamento rápido quanto ao nível de urgência e cuidados iniciais.

## Visão Geral do Projeto
Muitos tutores têm dificuldade em avaliar a gravidade de sintomas repentinos em seus pets. O Dr.PetIA atua como uma camada inicial de orientação, consolidando informações de espécie, idade, porte e sintomas (digitados ou gravados por voz) para sugerir a conduta mais adequada até o atendimento profissional.

## Tecnologias Utilizadas
- **Python 3.x**: Linguagem principal da aplicação.
- **Streamlit**: Framework para construção da interface de usuário.
- **Google GenAI SDK (`google-genai`)**: Integração com a API do Gemini.
- **Python-Dotenv**: Gerenciamento de variáveis de ambiente (`.env`).
- **CSS3**: Customização visual injetada no Streamlit.

## Como Rodar a Aplicação

1. Clone o repositório:
   ```bash
   git clone https://github.com/r0tazana/DR.PetIA.git
   cd dr-pet-ia