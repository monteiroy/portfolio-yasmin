import streamlit as st
import requests

st.set_page_config(page_title="Portfólio Yasmin Monteiro", layout="wide")

# Cores delicadas
COR_FUNDO = "#FFF0F5"      # Fundo geral rosa muito claro
COR_AREA = "#FFFFFF"       # Área principal branca
COR_TEXTOS = "#000000"     # Textos pretos

st.markdown(f"""
<style>
html, body, .stApp {{
    background-color: {COR_FUNDO} !important;
}}
section.main {{
    background-color: {COR_AREA} !important;
    padding: 1rem;
    border-radius: 10px;
}}
h1, h2, h3, p, label, span {{
    color: {COR_TEXTOS} !important;
    font-weight: 600;
}}
.sidebar .sidebar-content {{
    background-color: {COR_FUNDO} !important;
}}
.sidebar .sidebar-content span, .sidebar .sidebar-content label {{
    color: {COR_TEXTOS} !important;
    font-weight: 600;
}}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📚 Projetos")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Sobre Mim", "Programa Dólar", "Consultar CEP", "Decisão e Repetição", "Recursividade", "Acesso à API"]
)

if opcao == "Sobre Mim":
    st.title("🎀 Sobre Mim")
    st.write("""
    Me chamo **Yasmin**, e atualmente curso a graduação de **Sistemas de Informação**.
    Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano,
    com muito carinho e dedicação.
    """)

elif opcao == "Programa Dólar":
    st.title("💱 Conversor de Dólar para Real")
    valor = st.number_input("Digite o valor em dólar:", min_value=0.0, step=0.01)
    cotacao = 5.60
    if st.button("Converter"):
        resultado = valor * cotacao
        st.success(f"Valor convertido: R$ {resultado:.2f}")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Este programa converte dólares em reais multiplicando pelo valor fixo da cotação (5.60).")

elif opcao == "Consultar CEP":
    st.title("🏠 Consultar CEP")
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

elif opcao == "Decisão e Repetição":
    st.title("🔁 Decisão e Repetição")
    numero_input = st.number_input("Digite um número para ver pares e ímpares até ele:", min_value=1, step=1)
    if st.button("Executar"):
        st.write("Resultado:")
        for i in range(1, numero_input + 1):
            st.write(f"{i} é {'par' if i % 2 == 0 else 'ímpar'}")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Mostra números pares e ímpares usando laços de repetição e condicionais.")

elif opcao == "Recursividade":
    st.title("🔄 Recursividade")
    numero_rec = st.number_input("Digite um número para calcular o fatorial:", min_value=0, step=1)
    def fatorial(n):
        return 1 if n == 0 else n * fatorial(n-1)
    if st.button("Calcular Fatorial"):
        st.success(f"O fatorial de {numero_rec} é {fatorial(numero_rec)}")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Calcula o fatorial de um número usando recursão.")

elif opcao == "Acesso à API":
    st.title("🌐 Acesso à API")
    nome_input = st.text_input("Digite um nome para consultar:", "Yasmin")
    if st.button("Consultar API"):
        response = requests.get(f"https://api.agify.io?name={nome_input}")
        if response.status_code == 200:
            data = response.json()
            st.subheader("📌 Resultado da API:")
            st.write(f"Nome: {data.get('name')}")
            st.write(f"Idade estimada: {data.get('age')}")
            st.write(f"Contagem de registros: {data.get('count')}")
        else:
            st.error("Falha ao acessar a API")
    with st.expander("📘 Explicação do Projeto"):
        st.write("Consulta a idade estimada de um nome usando a API Agify.")
