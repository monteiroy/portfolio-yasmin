import streamlit as st

# ======================== CONFIGURAÇÕES ========================
st.set_page_config(
    page_title="Portfólio Yasmin",
    layout="wide",
)

# Cor do menu lateral (um tom mais escuro do #FFDAB9)
sidebar_color = "#F4C8A4"

# CSS para estilização
st.markdown(
    f"""
    <style>
        /* Cor do sidebar */
        section[data-testid="stSidebar"] {{
            background-color: {sidebar_color} !important;
        }}

        /* Títulos */
        h1, h2, h3, h4 {{
            color: #000000 !important;
        }}

        /* Texto branco */
        .white-text {{
            color: white !important;
        }}

        /* Botões personalizados */
        .stButton>button {{
            background-color: #FFDAB9;
            color: black;
            border-radius: 8px;
            padding: 8px 20px;
            border: none;
        }}
        .stButton>button:hover {{
            background-color: #f7c6a5;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================== MENU LATERAL =========================

st.sidebar.title("🌸 Navegação")
projeto = st.sidebar.selectbox(
    "Escolha um projeto:",
    ["Início", "Dólar", "CEP", "Decisão e Repetição", "Recursividade", "API Externa"],
)


# ======================== PÁGINAS ===============================

# ----------- PÁGINA INICIAL -----------
if projeto == "Início":
    st.title("✨ Portfólio Yasmin")
    st.write("Bem-vindo(a)! Aqui estão alguns dos meus projetos de programação:")
    st.markdown("""
    - 🌿 Estruturas de decisão e repetição  
    - 🌸 Recursividade  
    - 🌙 Consumo de APIs externas  
    - ⭐ Processamentos eficientes  
    """)


# ----------- PROGRAMA DO DÓLAR -----------
elif projeto == "Dólar":
    st.title("💱 Conversor de Dólar")

    valor = st.number_input("Digite um valor em dólar (US$):", min_value=0.0)

    if st.button("Converter"):
        convertido = valor * 5.50
        st.success(f"💰 **Valor em reais: R$ {convertido:,.2f}**")

    # Botão para explicação do código
    if st.button("📘 Ver explicação do código"):
        st.info("""
        Este programa multiplica o valor em dólar por uma taxa fixa (5.50).  
        Ele usa:
        - `number_input` para digitar valores  
        - Uma conta simples `valor * 5.50`  
        - `st.success` para mostrar o resultado formatado com R$  
        """)


# ----------- PROGRAMA DE CEP -----------
elif projeto == "CEP":
    st.title("📮 Consulta de CEP")

    cep = st.text_input("Digite o CEP:")

    if st.button("Buscar CEP"):
        st.write("🔎 *Aqui entraria o código de consulta de API real*")

    if st.button("📘 Ver explicação do código"):
        st.info("""
        O programa usa uma API (ViaCEP) para buscar informações de endereço.  
        - Envia requisição HTTP  
        - Recebe JSON  
        - Exibe rua, bairro e cidade  
        """)


# ----------- DECISÃO E REPETIÇÃO -----------
elif projeto == "Decisão e Repetição":
    st.title("🔁 Estruturas de Decisão e Repetição")

    numero = st.number_input("Digite um número:", value=0)

    if st.button("Processar"):
        if numero % 2 == 0:
            st.success("✨ O número é **par**")
        else:
            st.error("🌙 O número é **ímpar**")

    if st.button("📘 Ver explicação do código"):
        st.info("""
        Este código demonstra:
        - Uso de `if` e `else`  
        - Identificação de número par/ímpar  
        - Entrada numérica com `number_input`  
        """)


# ----------- RECURSIVIDADE -----------
elif projeto == "Recursividade":
    st.title("🌿 Recursividade — Fatorial")

    n = st.number_input("Digite um número para calcular o fatorial:", min_value=0, value=1)

    def fatorial(x):
        return 1 if x <= 1 else x * fatorial(x - 1)

    if st.button("Calcular"):
        st.success(f"🌸 Resultado: **{fatorial(n)}**")

    if st.button("📘 Ver explicação do código"):
        st.info("""
        A função chama ela mesma até chegar ao valor 1.  
        Exemplo:
        f(5) → 5 * 4 * 3 * 2 * 1  
        """)


# ----------- API EXTERNA -----------
elif projeto == "API Externa":
    st.title("🌐 Consumo de API Externa")

    st.write("Aqui seria exibido o retorno de uma API real.")

    if st.button("📘 Ver explicação do código"):
        st.info("""
        - Uso da biblioteca `requests`  
        - A API devolve dados em JSON  
        - O programa transforma e exibe os dados  
        """)
