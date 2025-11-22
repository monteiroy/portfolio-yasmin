import streamlit as st

# ==================== CONFIGURAÇÕES ====================
st.set_page_config(page_title="Portfólio Yasmin Monteiro", layout="wide")

# Cores
COR_PRINCIPAL = "#FFDAB9"
COR_LATERAL = "#FFE4E1"
COR_TEXTO = "#000000"  # melhor contraste com fundo claro

# ==================== ESTILO CSS ====================
st.markdown(f"""
<style>
/* Fundo geral */
html, body, .stApp {{
    background-color: {COR_LATERAL} !important;
}}

/* Área lateral */
.sidebar .sidebar-content {{
    background-color: {COR_LATERAL} !important;
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

    with st.expander("📘 Explicação do Código"):
        st.write("O conversor multiplica o valor digitado pela cotação fixa (5.60) e exibe o resultado.")

# ==================== CONSULTAR CEP (Exemplo) ====================
elif opcao == "Consultar CEP":
    st.title("🏠 Consultar CEP")
    cep = st.text_input("Digite o CEP (somente números):")
    if st.button("Buscar"):
        if cep:
            import requests
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if response.status_code == 200:
                data = response.json()
                if "erro" in data:
                    st.error("CEP não encontrado!")
                else:
                    st.write(data)
            else:
                st.error("Erro na requisição da API")
        else:
            st.warning("Digite um CEP válido")

# ==================== DECISÃO E REPETIÇÃO ====================
elif opcao == "Decisão e Repetição":
    st.title("🔁 Estruturas de Decisão e Repetição")
    st.write("Exemplo de loop e condição em Python:")
    for i in range(1, 6):
        if i % 2 == 0:
            st.write(f"{i} é par")
        else:
            st.write(f"{i} é ímpar")

# ==================== RECURSIVIDADE ====================
elif opcao == "Recursividade":
    st.title("🔄 Função Recursiva")
    st.write("Exemplo de cálculo de fatorial usando recursão:")
    
    def fatorial(n):
        return 1 if n == 0 else n * fatorial(n-1)
    
    numero = st.number_input("Digite um número:", min_value=0, step=1)
    if st.button("Calcular Fatorial"):
        st.success(f"O fatorial de {numero} é {fatorial(numero)}")

# ==================== ACESSO À API ====================
elif opcao == "Acesso à API":
    st.title("🌐 Acesso à API")
    st.write("Exemplo de requisição simples a uma API pública")
    
    if st.button("Testar API"):
        response = requests.get("https://api.agify.io?name=Yasmin")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Falha ao acessar a API")
