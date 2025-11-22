import streamlit as st

# ======================
# CONFIGURAÇÃO DO APP
# ======================
st.set_page_config(
    page_title="Portfólio – Yasmin",
    layout="wide"
)

# ======================
# ESTILO DA PÁGINA
# ======================
st.markdown(
    f"""
    <style>
        body {{
            background-color: #FFDAB9 !important;
        }}

        .stApp {{
            background-color: #FFDAB9;
        }}

        h1, h2, h3, h4, h5, h6, p, li, span, label {{
            color: white !important;
        }}

        .css-10trblm, .css-1v0mbdj {{
            color: white !important;
        }}

        .sidebar .sidebar-content {{
            background-color: #f5c6a5 !important;
        }}

        .stSelectbox label {{
            color: white !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# SIDEBAR
# ======================
st.sidebar.title("Escolha um projeto:")

opcao = st.sidebar.selectbox(
    "",
    ["Início", "Dólar (conversão)", "Consulta CEP", "Decisão e Repetição", "Recursividade", "Acesso a API"]
)


# ======================
# CONTEÚDOS DAS PÁGINAS
# ======================

# INICIO
if opcao == "Início":
    st.title("Bem-vindo ao meu Portfólio 👋")
    st.subheader("Aqui você encontra alguns dos meus projetos desenvolvidos em Python.")
    
    st.markdown("""
    ### 🔸 Projetos disponíveis:
    - Estruturas de decisão e repetição  
    - Recursividade  
    - Consumo de APIs externas  
    - Processamentos simples e eficientes  
    """)

# DÓLAR
elif opcao == "Dólar (conversão)":
    st.title("💲 Conversor de Dólar")

    valor = st.number_input("Digite o valor em reais (R$):", min_value=0.0, step=0.5)

    cotacao = 5.65  # exemplo
    convertido = valor / cotacao

    st.write(f"Com R$ {valor:.2f}, você compra **US$ {convertido:.2f}**")

# CEP
elif opcao == "Consulta CEP":
    st.title("📍 Consulta CEP via API")

    cep = st.text_input("Digite o CEP:")

    if st.button("Consultar"):
        import requests

        try:
            r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            dados = r.json()

            if "erro" in dados:
                st.error("CEP não encontrado.")
            else:
                st.write("### Resultado:")
                st.json(dados)

        except:
            st.error("Erro ao consultar API.")

# DECISÃO E REPETIÇÃO
elif opcao == "Decisão e Repetição":
    st.title("🔁 Estruturas de Decisão e Repetição")

    st.markdown("""
    Este projeto demonstra:
    - Uso de condicionais (`if`, `elif`, `else`)
    - Laços (`for`, `while`)
    """)

    numero = st.number_input("Digite um número:", step=1)

    st.write(f"Tabuada do {numero}:")
    for i in range(1, 11):
        st.write(f"{numero} x {i} = {numero * i}")

# RECURSIVIDADE
elif opcao == "Recursividade":
    st.title("🌀 Recursividade")

    st.markdown("Exemplo: cálculo fatorial usando função recursiva.")
    
    def fatorial(n):
        if n == 0:
            return 1
        return n * fatorial(n - 1)

    n = st.number_input("Número para calcular fatorial:", min_value=0, step=1)

    if st.button("Calcular"):
        st.write(f"Fatorial de {n} é **{fatorial(n)}**")

# ACESSO A API
elif opcao == "Acesso a API":
    st.title("🌐 Acesso a API Externa")

    st.markdown("Exemplo: consulta ao preço atual do Bitcoin.")

    import requests

    try:
        preco = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        valor = preco["bpi"]["USD"]["rate"]

        st.write(f"Preço atual do Bitcoin: **US$ {valor}**")

    except:
        st.error("Erro ao acessar API.")

