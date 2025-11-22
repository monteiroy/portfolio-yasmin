import streamlit as st
import requests

# Função para exibir o título e a explicação
def exibir_titulo_e_explicacao():
    st.title("🌸 Portfólio de Projetos 🎀")
    st.write("Seja bem-vindo ao meu portfólio de projetos desenvolvidos durante meu curso de Sistemas de Informação! 💻")
    st.write("Aqui, você encontrará alguns projetos que fiz com muito carinho e dedicação ao longo deste ano. 😊")

# Função para o projeto de "Consultar CEP"
def programa_consultar_cep():
    st.header("🔍 Consultar CEP")
    st.write("Este programa permite consultar informações sobre um CEP informado.")
    
    cep = st.text_input("Digite um CEP (ex: 01001-000):")
    
    if cep:
        st.write(f"Você digitou o CEP: {cep}")
        
        # Realiza a consulta na API viaCEP
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        
        if response.status_code == 200:
            data = response.json()
            if 'erro' not in data:
                st.write(f"**Endereço:** {data['logradouro']}")
                st.write(f"**Bairro:** {data['bairro']}")
                st.write(f"**Cidade:** {data['localidade']}")
                st.write(f"**Estado:** {data['uf']}")
            else:
                st.error("CEP não encontrado!")
        else:
            st.error("Erro ao buscar informações do CEP.")

    # Explicação do código
    if st.button('Explicação'):
        st.write("""
            Este programa usa a API ViaCEP para buscar o endereço completo a partir de um CEP fornecido.
            Ele retorna as informações de logradouro, bairro, cidade e estado.
        """)

# Função para o projeto de "Converter Dólar"
def programa_converter_dolar():
    st.header("💵 Converter Dólar")
    st.write("Este programa converte o valor de dólares para reais com base na cotação atual.")
    
    valor_dolar = st.number_input("Digite o valor em dólares:", min_value=0.01, step=0.01)
    
    if valor_dolar:
        # Exemplo de cotação fixa (a cotação real pode ser obtida com uma API de câmbio)
        cotacao = 5.4  # Cotação de exemplo para fins didáticos
        valor_real = valor_dolar * cotacao
        st.write(f"{valor_dolar} USD é igual a {valor_real:.2f} BRL.")
        
    # Explicação do código
    if st.button('Explicação'):
        st.write("""
            Este programa recebe o valor em dólares e o converte para reais com base em uma cotação fixa.
            Você pode ajustar a cotação para obter valores reais utilizando uma API de câmbio.
        """)

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
    
    # Explicação do código
    if st.button('Explicação'):
        st.write("""
            Este programa usa um loop para calcular e exibir a tabuada de um número informado.
            A tabuada é calculada multiplicando o número por 1 até 10.
        """)

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
    
    # Explicação do código
    if st.button('Explicação'):
        st.write("""
            Este programa utiliza a técnica de recursividade para calcular o fatorial de um número.
            A recursão é um processo no qual a função se chama dentro dela mesma até atingir um caso base.
        """)

# Função para o projeto de "Acesso a API"
def programa_acesso_api():
    st.header("🌐 Acesso a API")
    st.write("Este projeto faz uma chamada simples a uma API externa e exibe o resultado.")
    
    # Obtendo o IP público através da API ipify
    response = requests.get('https://api.ipify.org?format=json')
    
    if response.status_code == 200:
        ip_data = response.json()
        st.write(f"Seu IP público é: {ip_data['ip']}")
    else:
        st.error("Não foi possível obter o IP.")
    
    # Explicação do código
    if st.button('Explicação'):
        st.write("""
            Este programa realiza uma requisição à API ipify, que retorna o IP público do usuário.
            Ele exibe o IP retornado pela API para que o usuário saiba qual é o seu IP público.
        """)

# Função para a aba "Sobre mim"
def sobre_mim():
    st.header("🎀 Sobre Mim")
    st.write("Me chamo Yasmin, e atualmente curso a graduação de Sistemas de Informação. Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano, com muito carinho e dedicação.")

# Função principal para definir os projetos
def main():
    # Configurações de layout
    st.set_page_config(page_title="Portfólio da Yasmin", layout="wide")
    
    # Barra lateral
    st.sidebar.title("Escolha um Projeto")
    escolha = st.sidebar.radio(
        "Escolha um projeto:",
        ["Sobre Mim", "Consultar CEP", "Converter Dólar", "Decisão e Repetição", "Recursividade", "Acesso a API"]
    )
    
    if escolha == "Sobre Mim":
        sobre_mim()
    elif escolha == "Consultar CEP":
        programa_consultar_cep()
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
