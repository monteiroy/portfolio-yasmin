import streamlit as st
import requests

# =========================
# 🎨 ESTILO PERSONALIZADO
# =========================

st.markdown(
    """
    <style>
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #f5c6a6; /* #FFDAB9 um pouco mais escuro */
        }
        /* Títulos */
        h1, h2, h3, h4, h5, h6, p {
            color: white !important;
        } 
        .stButton>button {
            background-color: #FFDAB9;
            color: white;
            border-radius: 10px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #f7b48b;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 🌸 SIDEBAR
# =========================
st.sidebar.title("🌸 Meu Portfólio")
pag = st.sidebar.radio(
    "Selecione um projeto:",
    [
        "🌸 Programa Dólar",
        "📍 Consulta CEP",
        "🔁 Decisão e Repetição",
        "🌀 Recursividade"
    ]
)

# =========================
# 🌸 PROGRAMA 1 – DÓLAR
# =========================
if pag == "🌸 Programa Dólar":
    st.title("🌸 Conversor de Moeda — Real para Dólar")

    valor = st.text_input("Digite o valor em **R$**:")

    if st.button("Converter"):
        try:
            valor = valor.replace("R$", "").replace(",", ".").strip()
            valor_float = float(valor)

            # Cotação API
            r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
            cotacao = float(r.json()["USDBRL"]["bid"])
            resultado = valor_float / cotacao

            st.success(f"💰 Resultado: **US$ {resultado:.2f}**")

        except:
            st.error("Digite um valor válido!")

    if st.button("📘 Ver explicação do código"):
        st.info(
            """
            **Explicação:**
            - O usuário digita um valor em reais.
            - Removemos "R$" e convertemos para número.
            - Usamos uma API real de cotação do dólar.
            - Dividimos o valor pela cotação atual.
            """
        )

# =========================
# 🌸 PROGRAMA 2 – CEP
# =========================
elif pag == "📍 Consulta CEP":
    st.title("📍 Consulta de Endereço via CEP")

    cep = st.text_input("Digite o CEP (somente números):")

    if st.button("Consultar CEP"):
        try:
            resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()

            if "erro" in resposta:
                st.error("CEP não encontrado.")
            else:
                st.success("Endereço encontrado:")
                st.write(f"📍 **Rua:** {resposta['logradouro']}")
                st.write(f"🏙️ **Bairro:** {resposta['bairro']}")
                st.write(f"🏘️ **Cidade:** {resposta['localidade']}")
                st.write(f"🗺️ **Estado:** {resposta['uf']}")

        except:
            st.error("Erro ao consultar o CEP.")

    if st.button("📘 Ver explicação do código"):
        st.info(
            """
            **Explicação:**
            - Recebemos o CEP digitado pelo usuário.
            - Chamamos a API **ViaCEP**.
            - Se o CEP existir, exibimos o endereço completo.
            """
        )

# =========================
# 🌸 PROGRAMA 3 – DECISÃO E REPETIÇÃO
# =========================
elif pag == "🔁 Decisão e Repetição":
    st.title("🔁 Tempo total de atendimentos — Sobrancelhas")

    qtd = st.number_input("Quantas clientes serão atendidas hoje?", min_value=1)

    if st.button("Calcular tempo total"):
        TEMPO = 25  # minutos

        total = 0
        for i in range(int(qtd)):
            total += TEMPO

        horas = total // 60
        minutos = total % 60

        st.success(f"⏱ Tempo total: **{horas}h {minutos}min**")

    if st.button("📘 Ver explicação do código"):
        st.info(
            """
            **Explicação:**
            - Usamos um `for` para repetir o tempo de cada atendimento.
            - Cada atendimento dura 25 minutos.
            - Somamos todos e exibimos o tempo total formatado.
            """
        )

# =========================
# 🌸 PROGRAMA 4 – RECURSIVIDADE
# =========================
elif pag == "🌀 Recursividade":
    st.title("🌀 Fatorial com Recursividade")

    def fatorial(n):
        if n <= 1:
            return 1
        return n * fatorial(n - 1)

    num = st.number_input("Digite um número:", min_value=0, step=1)

    if st.button("Calcular fatorial"):
        st.success(f"Resultado: **{fatorial(int(num))}**")

    if st.button("📘 Ver explicação do código"):
        st.info(
            """
            **Explicação:**
            - A função chama ela mesma (`fatorial(n - 1)`).
            - Quando chega em 1, para.
            - Multiplica todos valores até chegar ao número desejado.
            """
        )
