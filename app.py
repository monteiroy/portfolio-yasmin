# app.py
import streamlit as st
import requests
import urllib.parse

# ------------------ Configuração da página ------------------
st.set_page_config(page_title="Portifolio Yasmin Monteiro", layout="wide")

# ------------------ Cores e estilo ------------------
SIDEBAR_BG = "#FFE4E1"   # cor solicitada para a área de seleção
TITLE_COLOR = "#FFDAB9"  # cor dos títulos no conteúdo principal
SIDEBAR_TEXT = "#FFFFFF" # texto branco na sidebar

st.markdown(
    f"""
    <style>
    /* Força o fundo do app (área principal) branco */
    .stApp .css-18e3th9 {{ background-color: white; }}
    .block-container {{ background-color: white !important; }}

    /* Sidebar (selector) - usa data-testid para maior compatibilidade */
    [data-testid="stSidebar"] {{
        background-color: {SIDEBAR_BG} !important;
    }}
    /* Força texto branco dentro da sidebar */
    [data-testid="stSidebar"] * {{
        color: {SIDEBAR_TEXT} !important;
    }}
    /* Ajustes de legibilidade: links, labels e entradas na sidebar */
    [data-testid="stSidebar"] .stRadio, 
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label {{
        color: {SIDEBAR_TEXT} !important;
    }}

    /* Títulos no conteúdo principal */
    h1, h2, h3 {{
        color: {TITLE_COLOR} !important;
    }}

    /* Mantém texto do corpo escuro para legibilidade no fundo branco */
    .stApp .css-1d391kg, .stApp .stText {{ color: #111111 !important; }}

    /* Remove destaque azul padrão em alguns elementos */
    .st-bf {{ box-shadow: none !important; }}

    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------ Sidebar / Navegação ------------------
st.sidebar.title("📚 Projetos")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Sobre Mim", "Conversor Dólar", "Consultar CEP", "Decisão e Repetição", "Recursividade", "Acesso à API"]
)

# ------------------ Sobre Mim ------------------
if opcao == "Sobre Mim":
    st.title("🎀 Sobre Mim")
    st.write(
        """
Oie, seja muito bem-vindo(a)!

Me chamo **Yasmin**, e atualmente curso a graduação em **Sistemas de Informação**.
Aqui você encontrará alguns dos meus projetos desenvolvidos ao longo deste ano,
com muito carinho e dedicação.
        """
    )

# ------------------ Conversor Dólar ------------------
elif opcao == "Conversor Dólar":
    st.title("💱 Conversor de Dólar para Real")
    st.write("Insira o valor em dólares. O resultado será exibido em reais (R$).")

    # entrada simples: número em dólares
    valor_dolar = st.number_input("Valor (US$):", min_value=0.0, format="%.2f", step=1.0)
    # cotação fixa no código (você pode atualizar conforme quiser)
    COTACAO_PADRAO = 5.60

    if st.button("Converter"):
        resultado = valor_dolar * COTACAO_PADRAO
        st.success(f"Valor convertido: **R$ {resultado:,.2f}**")

    # botão separado para mostrar explicação do código
    if st.button("Mostrar explicação (Conversor)"):
        st.write(
            """
**O que este programa faz:**  
- Recebe um valor em dólares (entrada numérica).  
- Multiplica pela cotação fixa definida em `COTACAO_PADRAO`.  
- Exibe o resultado formatado com `R$`.
            """
        )

# ------------------ Consultar CEP ------------------
elif opcao == "Consultar CEP":
    st.title("📍 Consultar CEP")
    st.write("Digite o CEP (apenas números, 8 dígitos) e clique em *Consultar*.")

    cep = st.text_input("CEP (ex: 01001000):", value="")
    if st.button("Consultar"):
        cep_limpo = "".join([c for c in cep if c.isdigit()])
        if len(cep_limpo) != 8:
            st.warning("Digite um CEP válido com 8 dígitos.")
        else:
            try:
                resp = requests.get(f"https://viacep.com.br/ws/{cep_limpo}/json/", timeout=5)
                if resp.status_code == 200:
                    dados = resp.json()
                    if dados.get("erro"):
                        st.error("CEP não encontrado.")
                    else:
                        st.success("Endereço encontrado:")
                        st.write(f"**Logradouro:** {dados.get('logradouro','-')}")
                        st.write(f"**Complemento:** {dados.get('complemento','-')}")
                        st.write(f"**Bairro:** {dados.get('bairro','-')}")
                        st.write(f"**Localidade:** {dados.get('localidade','-')}")
                        st.write(f"**UF:** {dados.get('uf','-')}")
                else:
                    st.error("Erro ao consultar o serviço ViaCEP.")
            except requests.RequestException:
                st.error("Erro de conexão ao consultar o CEP. Tente novamente.")

    # explicação em expander
    with st.expander("Explicação do Código (Consultar CEP)"):
        st.write(
            """
O programa usa a API pública **ViaCEP**.  
Fluxo:
1. Limpa o CEP (mantém apenas dígitos).  
2. Verifica formato (8 dígitos).  
3. Faz requisição GET para `https://viacep.com.br/ws/{cep}/json/`.  
4. Exibe os campos retornados (logradouro, bairro, cidade, estado).
            """
        )

# ------------------ Decisão e Repetição ------------------
elif opcao == "Decisão e Repetição":
    st.title("🔄 Decisão e Repetição — Tempo de Atendimento")
    st.write("Exemplo prático: calcular tempo total de atendimentos (sobrancelhas).")

    qtd = st.number_input("Quantos atendimentos você fará?", min_value=1, step=1, value=1)
    tempo_minutos = st.number_input("Tempo por atendimento (minutos):", min_value=1, step=1, value=25)

    if st.button("Calcular tempo total"):
        total = qtd * tempo_minutos
        horas = total // 60
        minutos = total % 60
        st.success(f"Tempo total estimado: **{horas}h {minutos}min**")

    if st.button("Mostrar explicação (Decisão e Repetição)"):
        st.write(
            """
Este exemplo usa:
- Entrada numérica (`st.number_input`) para quantidade e tempo por atendimento.
- Operação de repetição implícita (multiplicação) para calcular o total.
- Estruturas de decisão para validar entrada e mostrar resultado quando o usuário clica no botão.
            """
        )

# ------------------ Recursividade ------------------
elif opcao == "Recursividade":
    st.title("🌀 Recursividade — Fatorial")
    n = st.number_input("Calcular fatorial de (n):", min_value=0, step=1, value=5)

    def fatorial(x: int) -> int:
        if x <= 1:
            return 1
        return x * fatorial(x - 1)

    if st.button("Calcular Fatorial"):
        st.success(f"Resultado: **{fatorial(n)}**")

    if st.button("Mostrar explicação (Recursividade)"):
        st.write(
            """
A função `fatorial` chama a si mesma até atingir o caso base (x <= 1).
Cada chamada reduz `x` em 1 até chegar ao valor base.
            """
        )

# ------------------ Acesso à API (Conselho em PT) ------------------
elif opcao == "Acesso à API":
    st.title("🌐 Acesso à API — Conselho em Português")
    st.write("Clique para gerar um conselho traduzido para o português.")

    if st.button("Gerar conselho"):
        try:
            # Obtem conselho (em inglês) da API
            r = requests.get("https://api.adviceslip.com/advice", timeout=5)
            if r.status_code == 200:
                conselho_en = r.json().get("slip", {}).get("advice", "")
                if not conselho_en:
                    st.error("Resposta inesperada da API.")
                else:
                    # traduz com MyMemory (gratuito)
                    q = urllib.parse.quote(conselho_en)
                    tr = requests.get(f"https://api.mymemory.translated.net/get?q={q}&langpair=en|pt", timeout=5)
                    if tr.status_code == 200:
                        conselho_pt = tr.json().get("responseData", {}).get("translatedText", "")
                        st.success(conselho_pt)
                    else:
                        st.info(conselho_en)  # se falhar tradução, mostra inglês
            else:
                st.error("Erro ao obter conselho.")
        except requests.RequestException:
            st.error("Erro de conexão ao acessar a API.")

    if st.button("Mostrar explicação (Acesso à API)"):
        st.write(
            """
Fluxo:
1. Requisição GET para `api.adviceslip.com` (retorna conselho em inglês).  
2. Requisição GET para `api.mymemory.translated.net` (tradução automática para pt).  
3. Exibe o texto traduzido.  
Observação: ambos serviços são gratuitos, com limites; a tradução pode ser simples.
            """
        )

    with st.expander("📘 Explicação do Código"):
        st.write("Aqui são usadas estruturas condicionais para verificar se o número é par ou ímpar.")

# ==================== RECURSIVIDADE ====================
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

# ==================== ACESSO A API ====================
elif opcao == "Acesso à API":
    st.title("🌐 Acesso a API — Conselho Aleatório em Português")

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
        except:
            st.error("Erro ao acessar a API.")

    with st.expander("📘 Explicação do Código"):
        st.write("Aqui usamos uma API de conselhos em inglês, traduzindo a resposta automaticamente para o português.")
