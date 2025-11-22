import streamlit as st
import requests

# ==================== CONFIGURAÇÕES ====================
st.set_page_config(page_title="Portfólio Yasmin Monteiro", layout="wide")

COR_PRINCIPAL = "#FFDAB9"
COR_SIDEBAR = "#FFE4E1"
COR_TEXTO = "#333333"

# ==================== ESTILO CSS ====================
st.markdown(f"""
<style>
body {{
    background-color: white !important;
}}
.sidebar .sidebar-content {{
    background-color: {COR_SIDEBAR} !important;
}}
.sidebar .sidebar-content h2,
.sidebar .sidebar-content h3,
.sidebar .sidebar-content p,
.sidebar .sidebar-content label {{
    color: {COR_PRINCIPAL} !important;
    font-weight: 600;
}}
h1, h2, h3 {{
    color: {COR_PRINCIPAL};
}}
p, li, .block-container {{
    color: {COR_TEXTO};
}}
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.title("📚 Projetos")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    [
        "Sobre Mim",
        "Programa Dólar",
        "Consultar CEP",
        "Decisão e Repetição",
        "Recursividade",
        "Acesso à API"
    ]
)

# ==================== CONTEÚDOS ====================
if opcao == "Sobre Mim":
    st.title("🎀 Sobre Mim")
    st.write(
        """
        Oie, seja muito bem‑vindo(a)!

        Me chamo **Yasmin**, e atualmente curso a graduação de **Sistemas de Informação**.
        Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano,
        com muito carinho e dedicação.
        """
    )

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
            O conversor multiplica o valor em dólar pela cotação fixa definida no código.
            Ele utiliza entrada numérica do usuário e exibe o resultado formatado.
            """
        )

elif opcao == "Consultar CEP":
    st.title("📍 Consultar CEP")

    cep = st.text_input("Digite o CEP:")

    if st.button("Consultar"):
        try:
            resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            dados = resposta.json()

            if "erro" in dados:
                st.error("CEP inválido!")
            else:
                st.success("Endereço encontrado!")
                st.write(f"**Rua:** {dados['logradouro']}")
                st.write(f"**Bairro:** {dados['bairro']}")
                st.write(f"**Cidade:** {dados['localidade']}")
                st.write(f"**Estado:** {dados['uf']}")
        except Exception:
            st.error("Erro ao consultar o CEP.")

    with st.expander("📘 Explicação do Código"):
        st.write("O programa faz uma requisição para a API ViaCEP e retorna o endereço correspondente.")

elif opcao == "Decisão e Repetição":
    st.title("🔄 Estruturas de Decisão e Repetição")

    numero = st.number_input("Digite um número:")

    if st.button("Verificar"):
        if numero % 2 == 0:
            st.success("O número é PAR.")
        else:
            st.success("O número é ÍMPAR.")

    with st.expander("📘 Explicação do Código"):
        st.write("Aqui são usadas estruturas condicionais para verificar se o número é par ou ímpar.")

elif opcao == "Recursividade":
    st.title("🌀 Recursividade — Fatorial")

    def fatorial(n):
        if n <= 1:
            return 1
        return n * fatorial(n - 1)

    n = st.number_input("Digite um número:", min_value=0, step=1)

    if st.button("Calcular Fatorial"):
        st.success(f"Resultado: **{fatorial(n)}**")

    with st.expander("📘 Explicação do Código"):
        st.write("O cálculo do fatorial é feito chamando a função repetidamente, reduzindo o número até chegar em 1.")

elif opcao == "Acesso à API":
    st.title("🌐 Acesso à API — Conselho Aleatório em Português")

    if st.button("Gerar conselho"):
        try:
            resposta = requests.get("https://api.adviceslip.com/advice")

            if resposta.status_code == 200:
                conselho_en = resposta.json()["slip"]["advice"]
                traducao = requests.get(
                    f"https://api.mymemory.translated.net/get?q={conselho_en}&langpair=en|pt"
                )
                conselho_pt = traducao.json()["responseData"]["translatedText"]
                st.success(conselho_pt)
            else:
                st.error("Não foi possível obter o conselho.")
        except Exception:
            st.error("Erro ao acessar a API.")

    with st.expander("📘 Explicação do Código"):
        st.write("Aqui usamos uma API de conselhos em inglês, traduzindo a resposta automaticamente para o português.")
