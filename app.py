import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Portfólio Yasmin Monteiro", layout="wide")

# Cores
COR_DETALHE = "#FFC0CB"  # Rosa claro para detalhes
COR_AREA = "#FFFFFF"      # Branco para área principal
COR_TEXTOS = "#000000"     # Preto para textos

st.markdown(f"""
<style>
html, body, .stApp {{
    background-color: {COR_AREA} !important;
}}
section.main {{
    background-color: {COR_AREA} !important;
    padding: 1rem;
    border-radius: 10px;
}}
.stButton>button {{
    background-color: {COR_DETALHE} !important;
    color: white !important;
    font-weight: 600;
}}
.sidebar .sidebar-content {{
    background-color: {COR_DETALHE} !important;
    padding: 1rem;
    border-radius: 10px;
}}
.sidebar .sidebar-content span, .sidebar .sidebar-content label {{
    color: white !important;
    font-weight: 600;
}}
.card {{
    background-color: {COR_DETALHE};
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    color: white;
}}
.card h3 {{
    color: white;
}}
.card p {{
    color: white;
}}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📚 Projetos")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Sobre Mim", "Programa Dólar", "Consultar CEP", "Decisão e Repetição", "Recursividade", "Acesso à API", "Outros Projetos"]
)

if opcao == "Sobre Mim":
    st.title("🎀 Sobre Mim")
    st.write("""
    Olá! Me chamo **Yasmin Monteiro**, tenho **19 anos** e atualmente curso a graduação de **Sistemas de Informação**.
    
    Tenho grande interesse na área de **Backend**, desenvolvendo soluções eficientes e escaláveis para aplicações web.
    
    Ao longo do meu curso, participei de projetos variados que envolvem lógica de programação, consumo de APIs e desenvolvimento de funcionalidades interativas.
    
    Aqui neste portfólio, você poderá conhecer alguns dos meus projetos desenvolvidos com dedicação e atenção aos detalhes.
    """)

elif opcao == "Programa Dólar":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💱 Conversor de Dólar para Real")
    valor = st.number_input("Digite o valor em dólar:", min_value=0.0, step=0.01)
    cotacao = 5.60
    if st.button("Converter"):
        resultado = valor * cotacao
        st.success(f"Valor convertido: R$ {resultado:.2f}")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Converte dólares em reais multiplicando pelo valor fixo da cotação (5.60).")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Consultar CEP":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏠 Consultar CEP")
    cep_input = st.text_input("Digite o CEP (somente números):")
    if st.button("Buscar CEP"):
        if cep_input:
            response = requests.get(f"https://viacep.com.br/ws/{cep_input}/json/")
            if response.status_code == 200:
                data = response.json()
                if "erro" in data:
                    st.error("CEP não encontrado!")
                else:
                    st.subheader("📌 Resultado:")
                    st.write(f"CEP: {data.get('cep','')}")
                    st.write(f"Logradouro: {data.get('logradouro','')}")
                    st.write(f"Complemento: {data.get('complemento','')}")
                    st.write(f"Bairro: {data.get('bairro','')}")
                    st.write(f"Cidade: {data.get('localidade','')}")
                    st.write(f"Estado: {data.get('uf','')}")
            else:
                st.error("Erro na requisição da API")
        else:
            st.warning("Digite um CEP válido")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Consulta um CEP usando a API ViaCEP e retorna logradouro, bairro, cidade e estado.")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Decisão e Repetição":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔁 Decisão e Repetição")
    numero_input = st.number_input("Digite um número para ver pares e ímpares até ele:", min_value=1, step=1)
    if st.button("Executar"):
        st.write("Resultado:")
        for i in range(1, numero_input + 1):
            st.write(f"{i} é {'par' if i % 2 == 0 else 'ímpar'}")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Mostra números pares e ímpares usando laços de repetição e condicionais.")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Recursividade":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔄 Recursividade")
    numero_rec = st.number_input("Digite um número para calcular o fatorial:", min_value=0, step=1)
    def fatorial(n):
        return 1 if n == 0 else n * fatorial(n-1)
    if st.button("Calcular Fatorial"):
        st.success(f"O fatorial de {numero_rec} é {fatorial(numero_rec)}")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Calcula o fatorial de um número usando recursão.")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Acesso à API":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌐 Acesso à API")
    st.write("Consulta de idade estimada pelo nome usando a API Agify.")
    nome_input = st.text_input("Digite o nome para consultar:", "")
    
    if st.button("Consultar API"):
        if nome_input.strip() != "":
            try:
                response = requests.get(f"https://api.agify.io?name={nome_input}")
                response.raise_for_status()
                data = response.json()
                df = pd.DataFrame([data])
                st.subheader("📌 Resultado da API:")
                st.table(df.rename(columns={"name": "Nome", "age": "Idade Estimada", "count": "Contagem de Registros"}))
            except requests.RequestException:
                st.error("Falha ao acessar a API")
        else:
            st.warning("Digite um nome válido")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Consulta a idade estimada de um nome usando a API Agify e exibe o resultado em tabela.")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Outros Projetos":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💻 Projeto Figma - Site Desktop para Designer de Sobrancelhas")
    st.write("""
    Este projeto foi desenvolvido para a matéria de **Interação Humano-Computador**.  
    Consiste em um protótipo de site desktop voltado para designers de sobrancelhas.  

    Para visualizar melhor o projeto, clique no botão **Avançar** dentro da tela do Figma.
    """)
    st.markdown("[🔗 Acessar Projeto Figma](https://www.figma.com/proto/m14L5GmZzywpkPvbSaaGBi/Untitled?node-id=1-5&starting-point-node-id=1%3A5)")
    st.markdown('</div>', unsafe_allow_html=True)
