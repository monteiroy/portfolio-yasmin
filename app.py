import streamlit as st
import requests

# =========================== CONFIGURAÇÃO DA PÁGINA ===========================
st.set_page_config(
    page_title="Portifolio Yasmin Monteiro",
    page_icon="🎀",
    layout="wide"
)

# =========================== ESTILO PERSONALIZADO ===========================
st.markdown(
    """
    <style>
        body {
            background-color: #FFFFFF;
        }
        .sidebar .sidebar-content {
            background-color: #FFDAB9 !important;
        }
        .project-box {
            background-color: #FFE4E1;
            padding: 20px;
            border-radius: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================== SIDEBAR ===========================
st.sidebar.title("✨ Menu")
opcao = st.sidebar.radio(
    "Selecione:", 
    [
        "Sobre mim 🎀",
        "Programa Dólar",
        "Consultar CEP",
        "Decisão & Repetição",
        "Recursividade",
        "API – Conselho em Português"
    ]
)

# =========================== SOBRE MIM ===========================
if opcao == "Sobre mim 🎀":
    st.title("🎀 Sobre mim")
    st.markdown(
        """
        Oie, seja muito bem-vindo(a)!  
        
        Me chamo **Yasmin**, e atualmente curso a graduação de **Sistemas de Informação**.  
        Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano,  
        todos feitos com muito carinho para demonstrar minha evolução na área de tecnologia. 💗  
        """
    )

# =========================== PROGRAMA DÓLAR ===========================
elif opcao == "Programa Dólar":
    st.title("💸 Conversor de Dólar")
    st.markdown('<div class="project-box">', unsafe_allow_html=True)

    valor = st.number_input("Digite um valor em reais (R$):", min_value=0.0, step=0.5)

    if st.button("Converter"):
        cotacao = 5.72  # valor fixo para o exercício
        convertido = valor / cotacao
        st.success(f"💱 Valor em dólar: **US$ {convertido:.2f}**")

    # explicação
    if st.button("Ver explicação do código"):
        st.info(
            "Este programa divide o valor inserido pela cotação fixa do dólar (R$ 5,72), "
            "convertendo assim o valor para a moeda americana."
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================== CONSULTAR CEP ===========================
elif opcao == "Consultar CEP":
    st.title("📍 Consultar CEP")
    st.markdown('<div class="project-box">', unsafe_allow_html=True)

    cep = st.text_input("Digite o CEP:")

    if st.button("Consultar"):
        try:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            dados = response.json()

            if "erro" in dados:
                st.error("CEP inválido!")
            else:
                st.success("Endereço encontrado:")
                st.write(f"📌 **Logradouro:** {dados['logradouro']}")
                st.write(f"🏙️ **Bairro:** {dados['bairro']}")
                st.write(f"🏡 **Cidade:** {dados['localidade']}")
                st.write(f"🌎 **Estado:** {dados['uf']}")
        except:
            st.error("Erro ao consultar o CEP.")

    # explicação
    if st.button("Ver explicação do código"):
        st.info(
            "Este programa usa a API pública *ViaCEP* para consultar informações reais "
            "sobre um CEP informado."
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================== DECISÃO E REPETIÇÃO ===========================
elif opcao == "Decisão & Repetição":
    st.title("🔄 Decisão & Repetição")
    st.markdown('<div class="project-box">', unsafe_allow_html=True)

    numero = st.number_input("Digite um número:", step=1)

    if st.button("Verificar"):
        if numero % 2 == 0:
            st.success("O número é **par**!")
        else:
            st.warning("O número é **ímpar**!")

        st.write("Contagem até o número escolhido:")
        for i in range(1, int(numero) + 1):
            st.write(f"• {i}")

    # explicação
    if st.button("Ver explicação do código"):
        st.info(
            "Este programa utiliza estruturas de **decisão (if/else)** para verificar se "
            "o número é par ou ímpar e uma **repetição (for)** para contar até ele."
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================== RECURSIVIDADE ===========================
elif opcao == "Recursividade":
    st.title("🌀 Recursividade – Fatorial")
    st.markdown('<div class="project-box">', unsafe_allow_html=True)

    def fatorial(n):
        return 1 if n <= 1 else n * fatorial(n - 1)

    num = st.number_input("Digite um número para calcular o fatorial:", min_value=0, step=1)

    if st.button("Calcular"):
        st.success(f"Resultado: **{fatorial(num)}**")

    if st.button("Ver explicação do código"):
        st.info(
            "Este programa usa **recursividade**, ou seja, a função se chama novamente "
            "até chegar ao resultado final."
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================== API EM PORTUGUÊS ===========================
elif opcao == "API – Conselho em Português":
    st.title("✨ Conselho do Dia")
    st.markdown('<div class="project-box">', unsafe_allow_html=True)

    if st.button("Gerar conselho"):
        try:
            resposta = requests.get("https://api.adviceslip.com/advice")

            if resposta.status_code == 200:
                conselho_en = resposta.json()["slip"]["advice"]

                # Traduz para português automaticamente
                traducao = requests.get(
                    f"https://api.mymemory.translated.net/get?q={conselho_en}&langpair=en|pt"
                )
                conselho_pt = traducao.json()["responseData"]["translatedText"]

                st.success(conselho_pt)
            else:
                st.error("Erro ao obter conselho. Tente mais tarde.")
        except:
            st.error("Erro ao acessar a API.")

    if st.button("Ver explicação do código"):
        st.info(
            "Este programa acessa uma API que gera conselhos aleatórios em inglês e "
            "usa outra API para traduzir automaticamente para português."
        )

    st.markdown("</div>", unsafe_allow_html=True)
