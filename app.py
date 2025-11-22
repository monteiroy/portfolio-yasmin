import streamlit as st
import requests

# =========================
# CONFIGURAÇÃO DO SITE
# =========================
st.set_page_config(
    page_title="Portfólio",
    layout="wide"
)

# =========================
# ESTILO PERSONALIZADO
# =========================
st.markdown(f"""
    <style>
        body {{
            background-color: #FFDAB9 !important;
        }}
        .main {{
            background-color: #FFDAB9 !important;
        }}
        h1, h2, h3, p, label, span {{
            color: white !important;
        }}
        .stButton>button {{
            background-color: white;
            color: #FFDAB9;
            border-radius: 10px;
            padding: 8px 20px;
            font-weight: bold;
        }}
        .stTextInput>div>div>input {{
            background-color: white !important;
            color: black !important;
        }}
    </style>
""", unsafe_allow_html=True)

# =========================
# CABEÇALHO
# =========================
st.markdown("<h1 style='text-align:center;'>Portfólio de Projetos — Python</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Projetos acadêmicos desenvolvidos em Python</h3>", unsafe_allow_html=True)

st.write("---")

# =========================
# MENU LATERAL
# =========================
menu = st.sidebar.selectbox(
    "Escolha um projeto:",
    ["Início", "Programa do Dólar", "Consulta CEP (API)", "Decisão e Repetição", "Recursividade", "Uso de API Externa"]
)

# =========================
# PÁGINA INICIAL
# =========================
if menu == "Início":
    st.header("Bem-vindo(a) ao meu portfólio!")
    st.write("""
        Aqui você encontra projetos acadêmicos em Python, incluindo:
        - Estruturas de decisão e repetição  
        - Recursividade  
        - Consumo de APIs externas  
        - Processamentos simples e eficientes  
    """)

# =========================
# PROJETO 1 - Programa do Dólar
# =========================
elif menu == "Programa do Dólar":
    st.header("Conversor de Moeda (Dólar → Real)")

    dolar = st.number_input("Digite o valor em dólares:", min_value=0.0)
    cotacao = 5.72

    if st.button("Converter"):
        resultado = dolar * cotacao
        st.success(f"US$ {dolar:.2f} equivalem a R$ {resultado:.2f}")

# =========================
# PROJETO 2 - Consulta CEP (API ViaCEP)
# =========================
elif menu == "Consulta CEP (API)":
    st.header("Consulta de CEP — ViaCEP")

    cep = st.text_input("Digite um CEP (somente números):")

    if st.button("Consultar CEP"):
        if len(cep) == 8:
            url = f"https://viacep.com.br/ws/{cep}/json/"
            resposta = requests.get(url).json()

            if "erro" not in resposta:
                st.write("### Resultado:")
                st.write(resposta)
            else:
                st.error("CEP inválido!")
        else:
            st.error("Digite um CEP com 8 dígitos!")

# =========================
# PROJETO 3 - Decisão e Repetição
# =========================
elif menu == "Decisão e Repetição":
    st.header("Cálculo de Tempo de Atendimentos — Decisão e Repetição")

    qtd = st.number_input("Quantidade de atendimentos:", min_value=1, step=1)
    tempo_por_cliente = 25

    if st.button("Calcular Tempo Total"):
        total = 0
        for i in range(1, qtd + 1):
            st.write(f"Atendimento {i}: {tempo_por_cliente} minutos")
            total += tempo_por_cliente

        horas = total // 60
        minutos = total % 60

        st.success(f"Tempo total: {horas}h {minutos}min")

# =========================
# PROJETO 4 - Recursividade
# =========================
elif menu == "Recursividade":
    st.header("Cálculo Fatorial — Recursividade")

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        return n * fatorial(n - 1)

    numero = st.number_input("Digite um número inteiro:", min_value=0, step=1)

    if st.button("Calcular Fatorial"):
        st.success(f"Resultado: {fatorial(numero)}")

# =========================
# PROJETO 5 - API de Cotação Atual
# =========================
elif menu == "Uso de API Externa":
    st.header("Cotação Atual do Dólar — API AwesomeAPI")

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    if st.button("Obter Cotação Atual"):
        dados = requests.get(url).json()
        cotacao = float(dados["USDBRL"]["bid"])
        st.success(f"Cotação atual do dólar: R$ {cotacao:.2f}")
