import streamlit as st
import requests

# Configurações Gerais (simplificado) ====================
st.set_page_config(page_title="Portifolio Yasmin Monteiro", layout="wide")

COR_PRINCIPAL = "#FFDAB9"
COR_LATERAL = "#FFE4E1"
COR_TEXTO = "#FFFFFF"

# Estilo CSS
st.markdown(f"""
<style>
/* Fundo geral */
html, body, .stApp {
    background-color: #FFE4E1 !important;
}

/* Área lateral */
.sidebar .sidebar-content {
    background-color: #FFE4E1 !important;
}

/* Títulos e textos */
h1, h2, h3, p, label, span {
    color: #FFFFFF !important;
    font-weight: 600;
}
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
    st.write(
        """
        Oie, seja muito bem-vindo(a)!

        Me chamo **Yasmin**, e atualmente curso a graduação de **Sistemas de Informação**.
        Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano,
        com muito carinho e dedicação.
        """
    )

# ==================== PROGRAMA DÓLAR ====================
elif opcao == "Programa Dólar":
    st.title("💱 Conversor de Dólar para Real")

    valor = st.number_input("Digite o valor em dólar:")
    cotacao = 5.60

    if st.button("Converter"):
        resultado = valor * cotacao
        st.success(f"Valor convertido: **R$ {resultado:.2f}**")

    with st.expander("📘 Explicação do Código"):
        st.write(
            """
            O conversor simplesmente multiplica o valor digitado pela cotação fixa definida no código.
            Não usa nenhuma API — apenas faz a operação matemática e exibe o resultado.
            """
            O conversor apenas recebe o valor, multiplica pela cotação (5.60) e mostra o resultado.
            """
        )
