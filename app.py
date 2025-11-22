import streamlit as st
import requests

# Função para exibir o título e a explicação
def exibir_titulo_e_explicacao():
    st.title("Portfólio Yasmin 🎀")
    st.write("Seja bem-vindo ao meu portfólio de projetos desenvolvidos durante meu curso de Sistemas de Informação!")
    st.write("Aqui, você encontrará alguns projetos que fiz com muito carinho e dedicação ao longo deste ano.")

# Função para o projeto de "CEP"
def programa_cep():
    st.header("🔍 Consulta de CEP")
    st.write("Este programa permite consultar informações sobre um CEP informado. É bem simples!")
    cep = st.text_input("Digite um CEP (ex: 01001-000):")
    if cep:
        st.write(f"Você digitou o CEP: {cep}")
        # Aqui você pode adicionar a consulta de CEP (API de consulta de CEP)
        # Exemplo:
        # response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        # st.write(response.json())

# Função para o projeto de "Converter Dólar"
def programa_converter_dolar():
    st.header("💵 Converter Dólar")
    st.write("Este programa converte o valor de dólares para reais com base na cotação atual.")
    valor_dolar = st.number_input("Digite o valor em dólares:", min_value=0.01)
    if valor_dolar:
        cotacao = 5.4  # Cotação fixa para fins de exemplo
        valor_real = valor_dolar * cotacao
        st.write(f"{valor_dolar} USD é igual a {valor_real:.2f} BRL.")

# Função para o programa de "Decisão e Repetição"
def programa_decisao_repeticao():
    st.header("🔢 Tabela de Multiplicação")
    st.write("Este programa gera a tabuada de multiplicação de um número que você escolher.")
    numero = st.number_input("Digite um número para ver a tabuada:", min_value=1, max_value=100)
    if numero:
        tabuada = [numero * i for i in range(1, 11)]
        st.write(f"A tabuada do {numero} é:")
        for i, resultado in enumerate(tabuada, 1):
            st.write(f"{numero} x {i} = {resultado}")

# Função para o programa de "Recursividade"
def programa_recursividade():
    st.header("♻️ Fatorial (Recursivo)")
    st.write("Este programa calcula o fatorial de um número utilizando recursividade.")
    numero = st.number_input("Digite um número para calcular o fatorial:", min_value=0)
    
    def fatorial(n):
        if n == 0:
            return 1
        else:
            return n * fatorial(n-1)
    
    if numero is not None and numero >= 0:
        st.write(f"O fatorial de {numero} é {fatorial(numero)}.")

# Função para o projeto de "Acesso a API"
def programa_acesso_api():
    st.header("🌐 Acesso a API")
    st.write("Este projeto faz uma chamada simples a uma API externa e exibe o resultado.")
    # Exemplo: obtenção do IP público
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    st.write(f"Seu IP público é: {ip_data['ip']}")

# Função para a aba "Sobre mim"
def sobre_mim():
    st.header("🎀 Sobre Mim")
    st.write("Me chamo Yasmin, e atualmente curso a graduação de Sistemas de Informação. Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano, com muito carinho e dedicação.")

# Função principal para definir os projetos
def main():
    # Configurações de layout
    st.set_page_config(page_title="Portfólio da Yasmin", layout="wide")
    
    # Customização do estilo (delicado e clean)
    st.markdown("""
        <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;  /* Fundo neutro claro */
            color: #333;
        }
        .stSidebar {
            background-color: #F9E6F7;  /* Fundo suave e delicado para a barra lateral */
        }
        .stTextInput, .stNumberInput, .stButton {
            border-radius: 12px;
            padding: 10px;
        }
        .stButton > button {
            background-color: #FFC0CB;  /* Rosa suave para os botões */
            color: white;
            border-radius: 12px;
            font-weight: bold;
        }
        .stTextInput > div > input {
            background-color: #FFF0F5;  /* Cor de fundo suave para as entradas */
        }
        .stMarkdown {
            color: #555;
        }
        h1, h2, h3 {
            color: #F1A7C4;  /* Tom suave de rosa para os títulos */
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Barra lateral
    st.sidebar.title("Escolha um Projeto")
    escolha = st.sidebar.radio(
        "Escolha um projeto:",
        ["Sobre Mim", "CEP", "Converter Dólar", "Decisão e Repetição", "Recursividade", "Acesso a API"]
    )
    
    if escolha == "Sobre Mim":
        sobre_mim()
    elif escolha == "CEP":
        programa_cep()
    elif escolha == "Converter Dólar":
        programa_converter_dolar()
    elif escolha == "Decisão e Repetição":
        programa_decisao_repeticao()
    elif escolha == "Recursividade":
        programa_recursividade()
    elif escolha == "Acesso a API":
        programa_acesso_api()

# Chama a função principal para executar o app
if __name__ == "__main__":
    main()
