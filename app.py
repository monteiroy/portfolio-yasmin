import streamlit as st
import requests

# ===================== CONFIGURAÇÕES DE ESTILO =====================
PRIMARY_COLOR = "#FFDAB9"  # tom pastel solicitado
PRIMARY_DARK = "#e6c3a3"   # versão mais escura para menu lateral
TEXT_COLOR = "#FFDAB9"     # texto nos títulos

st.set_page_config(page_title="Portfólio — Designer", layout="wide")

# ===================== CSS PERSONALIZADO =====================
st.markdown(f"""
<style>
/* Fundo principal branco */
body {{
    background-color: white !important;
}}

/* Títulos com a cor escolhida */
h1, h2, h3, h4, h5, h6 {{
    color: {TEXT_COLOR} !important;
}}

/* Barra lateral com cor pastel escura */
[data-testid="stSidebar"] {{
    background-color: {PRIMARY_DARK} !important;
}}

/* Texto da barra lateral */
[data-testid="stSidebar"] * {{
    color: white !important;
    font-size: 17px !important;
}}
</style>
""", unsafe_allow_html=True)

# ===================== MENU LATERAL =====================
st.sidebar.title("Menu ✨")
selecionado = st.sidebar.radio(
    "Navegação",
    ["Sobre Mim 🎀", "Programa — Dólar", "Programa — CEP", "Decisão e Repetição", "Recursividade", "Acesso à API"]
)

# ===================== SOBRE MIM =====================
if selecionado == "Sobre Mim 🎀":
    st.title("Sobre Mim 🎀")
    st.write("""
    Oie, seja muito bem-vindo(a)! 🌸
    Meu nome é Yasmin, curso a graduação em Sistemas de Informação e aqui você encontrará
    alguns dos projetos que desenvolvi ao longo deste ano com muito carinho e dedicação.
    Espero que goste e aproveite o conteúdo! ✨
    """)

# ===================== PROGRAMA DÓLAR =====================
elif selecionado == "Programa — Dólar":
    st.title("Conversor de Dólar 💸 (com explicação)")

    valor = st.number_input("Digite o valor em dólares:", min_value=0.0, format="%.2f")
    # Removido campo de cotação
    cotacao = 5.50  # valor fixo sugerido para exemplo

    if st.button("Converter"):
        if cotacao > 0:
            resultado = valor * cotacao
            st.success(f"Valor em reais: R$ {resultado:.2f}")

    with st.expander("📘 Explicação do Código"):
        st.write("""
        Este programa multiplica o valor em dólares pela cotação atual.
        Ele usa uma estrutura simples de decisão: só converte se o usuário clicar no botão.
        """)

# ===================== PROGRAMA CEP =====================
elif selecionado == "Programa — CEP":
    st.title("Consulta de CEP 📍")

    cep = st.text_input("Digite o CEP (somente números):")

    if st.button("Consultar CEP"):
        if len(cep) == 8:
            url = f"https://viacep.com.br/ws/{cep}/json/"
            r = requests.get(url)

            if r.status_code == 200:
                dados = r.json()
                if "erro" not in dados:
                    st.success("Endereço encontrado:")
                    st.write(f"**Rua:** {dados['logradouro']}")
                    st.write(f"**Bairro:** {dados['bairro']}")
                    st.write(f"**Cidade:** {dados['localidade']}")
                    st.write(f"**Estado:** {dados['uf']}")
                else:
                    st.error("CEP não encontrado.")
            else:
                st.error("Erro ao consultar API.")
        else:
            st.warning("Digite um CEP válido com 8 dígitos.")

    with st.expander("📘 Explicação do Código"):
        st.write("""
        Este programa utiliza a API pública ViaCEP para consultar endereços.
        Ele envia uma requisição HTTP e retorna os dados correspondentes.
        """)

# ===================== DECISÃO E REPETIÇÃO =====================
elif selecionado == "Decisão e Repetição":
    st.title("Decisão e Repetição 🔁")

    qtd = st.number_input("Quantas sobrancelhas você irá atender hoje?", min_value=1, step=1)

    if st.button("Calcular Tempo Total"):
        tempo_por_cliente = 25
        total = 0
        for i in range(qtd):
            total += tempo_por_cliente

        horas = total // 60
        minutos = total % 60

        st.success(f"Tempo total estimado: {horas}h {minutos}min")

    with st.expander("📘 Explicação do Código"):
        st.write("""
        Este programa usa um laço **for** e uma estrutura de decisão para calcular tempo total.
        """)

# ===================== RECURSIVIDADE =====================
elif selecionado == "Recursividade":
    st.title("Exemplo de Recursividade 🌀")

    n = st.number_input("Calcular fatorial de:", min_value=1, step=1)

    def fatorial(x):
        if x == 1:
            return 1
        return x * fatorial(x - 1)

    if st.button("Calcular Fatorial"):
        st.success(f"Resultado: {fatorial(n)}")

    with st.expander("📘 Explicação do Código"):
        st.write("""
        A função chama a si mesma até chegar ao caso base.
        Isso é recursividade.
        """)

# ===================== API GENÉRICA =====================
elif selecionado == "Acesso à API":
    st.title("Consulta de API 🌐")
    st.write("Exemplo: pegar um conselho aleatório em português.

Aqui o programa realmente faz uma requisição para uma API que retorna conselhos em português. Quando o usuário clicar no botão, o Streamlit faz a chamada, recebe o conselho e exibe na tela.

```python
import requests
import streamlit as st

st.subheader("✨ Conselho do Dia")

if st.button("Gerar conselho"):
    try:
        resposta = requests.get("https://api.adviceslip.com/advice")

        if resposta.status_code == 200:
            conselho_en = resposta.json()["slip"]["advice"]

            # Tradução automática simples usando MyMemory
            traducao = requests.get(
                f"https://api.mymemory.translated.net/get?q={conselho_en}&langpair=en|pt"
            )
            conselho_pt = traducao.json()["responseData"]["translatedText"]

            st.success(conselho_pt)
        else:
            st.error("Não foi possível obter um conselho agora. Tente novamente mais tarde.")
    except:
        st.error("Erro ao acessar a API.")
```
