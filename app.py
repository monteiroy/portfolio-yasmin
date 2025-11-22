import streamlit as st
import requests

# ==================== CONFIGURAÇÕES ====================
st.set_page_config(page_title="Portfólio Yasmin Monteiro", layout="wide")

# Cores
COR_SIDEBAR = "#FFE4E1"  # rosa para sidebar
COR_FUNDO = "#FFFFFF"     # branco para área principal
COR_TEXTO = "#000000"     # preto para textos, melhor contraste

# ==================== ESTILO CSS ====================
st.markdown(f"""
<style>
/* Fundo geral da página principal */
html, body, .stApp {{
    background-color: {COR_FUNDO} !important;
}}

/* Fundo da sidebar */
.sidebar .sidebar-content {{
    background-color: {COR_SIDEBAR} !important;
}}

/* Títulos e textos */
h1, h2, h3, p, label, span {{
    color: {COR_TEXTO} !important;
    font-weight: 600;
}}
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.title("📚 Projetos")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Sobre Mim", "Programa Dólar", "Consultar CEP", "Decisão e Repetição", "Recursividade", "Acesso à API"]
)

# ==================== SOBRE MIM ====================
if opcao == "Sobre Mim":
    st.title("🎀 Sobre Mim")
    st.write("""
    Me chamo **Yasmin**, e atualmente curso a graduação de **Sistemas de Informação**.
    Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano,
    com muito carinho e dedicação.
    """)

# ==================== PROGRAMA DÓLAR ====================
elif opcao == "Programa Dólar":
    st.title("💱 Conversor de Dólar para Real")
    valor = st.number_input("Digite o valor em dólar:", min_value=0.0, step=0.01)
    cotacao = 5.60

    if st.button("Converter"):
        resultado = valor * cotacao
        st.success(f"Valor convertido: **R$ {resultado:.2f}**")

    with st.expander("📘 Explicação do Projeto"):
        st.write("""
        Este programa recebe um valor em dólar digitado pelo usuário,
        multiplica pela cotação fixa de 5.60 e exibe o valor convertido em reais.
        É um exemplo simples de interação com o usuário e cálculo em Python.
        """)

# ==================== CONSULTAR CEP ====================
elif opcao == "Consultar CEP":
    st.title("🏠 Consultar CEP")
    cep = st.text_input("Digite o CEP (somente números):")

    if st.button("Buscar CEP"):
        if cep:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if response.status_code == 200:
                data = response.json()
                if "erro" in data:
                    st.error("CEP não encontrado!")
                else:
                    st.subheader("📌 Resultado:")
                    st.write(f"**CEP:** {data.get('cep','')}")
                    st.write(f"**Logradouro:** {data.get('logradouro','')}")
                    st.write(f"**Complemento:** {data.get('complemento','')}")
                    st.write(f"**Bairro:** {data.get('bairro','')}")
                    st.write(f"**Cidade:** {data.get('localidade','')}")
                    st.write(f"**Estado:** {data.get('uf','')}")
            else:
                st.error("Erro na requisição da API")
        else:
            st.warning("Digite um CEP válido")

    with st.expander("📘 Explicação do Projeto"):
        st.write("""
        Este projeto consulta um CEP digitado pelo usuário utilizando a API pública ViaCEP.
        Retorna informações detalhadas como logradouro, bairro, cidade e estado.
        """)

# ==================== DECISÃO E REPETIÇÃO ====================
el
