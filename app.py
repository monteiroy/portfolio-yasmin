import streamlit as st
import requests

st.set_page_config(page_title="Portfólio Yasmin Monteiro", layout="wide")

COR_FUNDO = "#FFE4E1"
COR_SIDEBAR = "#FFB6C1"
COR_TEXTO_SIDEBAR = "#FFFFFF"
COR_TEXTO_PRINCIPAL = "#000000"

st.markdown(f"""
<style>
html, body, .stApp {{
    background-color: {COR_FUNDO} !important;
}}
.sidebar .sidebar-content {{
    background-color: {COR_SIDEBAR} !important;
}}
.sidebar .sidebar-content, .sidebar .sidebar-content span, .sidebar .sidebar-content label {{
    color: {COR_TEXTO_SIDEBAR} !important;
    font-weight: 600;
}}
h1, h2, h3, p, label, span {{
    color: {COR_TEXTO_PRINCIPAL} !important;
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
        st.success(f"Valor convertido: **R$ {resultado:.2f}**")

    with st.expander("📘 Explicação do Projeto"):
        st.write("""
        Este programa recebe um valor em dólar digitado pelo usuário,
        multiplica pela cotação fixa de 5.60 e exibe o valor convertido em reais.
        """)

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

elif opcao == "Decisão e Repetição":
    st.title("🔁 Estruturas de Decisão e Repetição")
    numero_input = st.number_input("Digite um número para ver pares e ímpares até ele:", min_value=1, step=1)
    
    if st.button("Executar Decisão e Repetição"):
        st.write("Resultado:")
        for i in range(1, numero_input + 1):
            if i % 2 == 0:
                st.write(f"{i} é par")
            else:
                st.write(f"{i} é ímpar")

    with st.expander("📘 Explicação do Projeto"):
        st.write("""
        Este projeto demonstra o uso de **laços de repetição (for)** e **condicionais (if/else)**.
        Ele percorre todos os números de 1 até o valor informado e indica se cada número é par ou ímpar.
        """)

elif opcao == "Recursividade":
    st.title("🔄 Função Recursiva")
    numero_rec = st.number_input("Digite um número para calcular o fatorial:", min_value=0, step=1)

    def fatorial(n):
        return 1 if n == 0 else n * fatorial(n-1)

    if st.button("Calcular Fatorial"):
        st.success(f"O fatorial de {numero_rec} é {fatorial(numero_rec)}")

    with st.expander("📘 Explicação do Projeto"):
        st.write("""
        Este projeto utiliza **recursão** para calcular o fatorial de um número.
        Uma função chama a si mesma até atingir o caso base (0! = 1).
        """)

elif opcao == "Acesso à API":
    st.title("🌐 Acesso à API")
    st.write("Consulta de idade estimada pelo nome utilizando a API Agify.")

    nome_input = st.text_input("Digite um nome para consultar:", "Yasmin")
    if st.button("Consultar API"):
        response = requests.get(f"https://api.agify.io?name={nome_input}")
        if response.status_code == 200:
            data = response.json()
            st.subheader("📌 Resultado da API:")
            st.write(f"**Nome:** {data.get('name')}")
            st.write(f"**Idade estimada:** {data.get('age')}")
            st.write(f"**Contagem de registros:** {data.get('count')}")
        else:
            st.error("Falha ao acessar a API")

    with st.expander("📘 Explicação do Projeto"):
        st.write("""
        Este projeto demonstra como consumir uma **API pública** com Python.
        A API Agify estima a idade de uma pessoa a partir do nome fornecido.
        """)

el
