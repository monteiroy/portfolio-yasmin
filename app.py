import streamlit as st
import requests

# ==========================
# CONFIGURAÇÃO DO SITE
# ==========================

st.set_page_config(page_title="Portfólio Yasmin Monteiro", layout="wide")

SIDEBAR_COLOR = "#f7c7a5"  # #FFDAB9 mais escuro
MAIN_COLOR = "#FFDAB9"

st.markdown(
    f"""
    <style>
        .sidebar .sidebar-content {{
            background-color: {SIDEBAR_COLOR} !important;
        }}
        body {{
            background-color: white !important;
        }}
        .main-title {{
            color: {MAIN_COLOR};
            font-weight: 700;
            font-size: 36px;
        }}
        .section-title {{
            color: {MAIN_COLOR};
            font-size: 28px;
            font-weight: 700;
        }}
        .text-colored {{
            color: {MAIN_COLOR};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# BARRA LATERAL
# ==========================

st.sidebar.title("Projetos")

opcao = st.sidebar.radio(
    "Selecione uma opção:",
    ["Sobre Mim 🎀", "Programa Dólar", "Consultar CEP", "Decisão e Repetição", "Recursividade", "Acesso à API"],
)

# ==========================
# SOBRE MIM
# ==========================

if opcao == "Sobre Mim 🎀":
    st.markdown('<h1 class="main-title">Sobre Mim 🎀</h1>', unsafe_allow_html=True)

    st.write("""
    Oie, seja muito bem-vindo(a)!  
    Me chamo **Yasmin**, e atualmente curso a graduação de **Sistemas de Informação**.  

    Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo do ano, 
    com muito carinho, dedicação e aprendizado. 🌸  
    """)

# ==========================
# PROGRAMA DÓLAR
# ==========================

elif opcao == "Programa Dólar":
    st.markdown('<h1 class="main-title">Conversor de Dólar 💱</h1>', unsafe_allow_html=True)

    valor = st.number_input("Digite o valor em dólar (US$):", min_value=0.0, format="%.2f")

    if st.button("Converter"):
        cotacao = 5.75
        resultado = valor * cotacao
        st.success(f"O valor convertido é **R$ {resultado:.2f}**")

    if st.button("Ver explicação do código"):
        st.info("""
        O programa pega um valor em dólar informado pelo usuário,
        multiplica pela cotação fixa definida no código,
        e exibe o resultado convertido em reais.
        """)

# ==========================
# CONSULTAR CEP
# ==========================

elif opcao == "Consultar CEP":
    st.markdown('<h1 class="main-title">Consultar CEP 📍</h1>', unsafe_allow_html=True)

    cep = st.text_input("Digite o CEP (somente números):")

    if st.button("Consultar"):
        if len(cep) == 8 and cep.isdigit():
            url = f"https://viacep.com.br/ws/{cep}/json/"
            resposta = requests.get(url).json()

            if "erro" not in resposta:
                st.success("Endereço encontrado:")
                st.write(f"**Rua:** {resposta['logradouro']}")
                st.write(f"**Bairro:** {resposta['bairro']}")
                st.write(f"**Cidade:** {resposta['localidade']}")
                st.write(f"**Estado:** {resposta['uf']}")
            else:
                st.error("CEP não encontrado.")
        else:
            st.error("Digite um CEP válido.")

    if st.button("Ver explicação do código"):
        st.info("""
        O programa usa a API ViaCEP para consultar o endereço.
        O usuário informa o CEP e o sistema faz uma requisição HTTP para retornar:
        rua, bairro, cidade e estado.
        """)

# ==========================
# DECISÃO E REPETIÇÃO
# ==========================

elif opcao == "Decisão e Repetição":
    st.markdown('<h1 class="section-title">Exemplo: Decisão e Repetição 🔁</h1>', unsafe_allow_html=True)

    numero = st.number_input("Digite um número:", min_value=0, step=1)

    if st.button("Mostrar contagem"):
        st.write("Contando até o número escolhido:")
        for i in range(numero + 1):
            st.write(i)

    if st.button("Ver explicação do código"):
        st.info("""
        Este programa demonstra estruturas básicas de decisão (if)
        e repetição (for). Ele conta de 0 até o número informado pelo usuário.
        """)

# ==========================
# RECURSIVIDADE
# ==========================

elif opcao == "Recursividade":
    st.markdown('<h1 class="section-title">Exemplo de Recursividade 🧩</h1>', unsafe_allow_html=True)

    def fatorial(n):
        if n == 0:
            return 1
        return n * fatorial(n - 1)

    num = st.number_input("Digite um número para calcular o fatorial:", min_value=0, step=1)

    if st.button("Calcular fatorial"):
        st.success(f"O fatorial de {num} é **{fatorial(num)}**")

    if st.button("Ver explicação do código"):
        st.info("""
        A função usa recursividade: ela chama ela mesma até chegar em 0.
        """)

# ==========================
# ACESSO À API
# ==========================

elif opcao == "Acesso à API":
    st.markdown('<h1 class="section-title">Acesso à API ✨</h1>', unsafe_allow_html=True)

    st.write("Clique no botão para receber um conselho aleatório em português:")

    if st.button("Gerar conselho"):
        try:
            # API de conselhos
            resposta = requests.get("https://api.adviceslip.com/advice")
            conselho_en = resposta.json()["slip"]["advice"]

            # Traduzir para português
            traducao = requests.get(
                f"https://api.mymemory.translated.net/get?q={conselho_en}&langpair=en|pt"
            )
            conselho_pt = traducao.json()["responseData"]["translatedText"]

            st.success(conselho_pt)

        except:
            st.error("Erro ao acessar a API.")

    if st.button("Ver explicação do código"):
        st.info("""
        O programa acessa uma API pública que retorna conselhos.
        Como a API original está em inglês, o programa traduz automaticamente
        o texto para português usando a API MyMemory.
        """)

