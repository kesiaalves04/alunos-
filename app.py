import streamlit as st
import pandas as pd
import os


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Gestão de Alunos",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


ARQUIVO = "alunos.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1523050854058-8df90110c9f1"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_ESCOLA = (
    "https://images.unsplash.com/"
    "photo-1523240795612-9a054b0db644"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #EEF4FF 0%,
            #E3ECFF 50%,
            #D7E4FF 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #172554,
            #1E3A8A
        );

    border-right:
        2px solid #60A5FA;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #BFDBFE !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #172554 !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #334155 !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(15,23,42,0.97) 0%,
            rgba(15,23,42,0.84) 45%,
            rgba(15,23,42,0.15) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #60A5FA !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #E0F2FE !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #2563EB;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(37,99,235,0.25);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #172554 !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #475569 !important;

    margin-top: 5px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #172554,
            #1E40AF
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #DBEAFE !important;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.90);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #93C5FD;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}


/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {

    color: #172554 !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {

    background-color: #FFFFFF !important;

    color: #172554 !important;

    -webkit-text-fill-color:
        #172554 !important;

    border:
        2px solid #60A5FA !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {

    border:
        2px solid #2563EB !important;

    box-shadow:
        0 0 0 3px rgba(37,99,235,0.15) !important;
}

input::placeholder,
textarea::placeholder {

    color: #64748B !important;

    opacity: 1 !important;
}


/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {

    background-color: #FFFFFF !important;

    border:
        2px solid #60A5FA !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {

    color: #172554 !important;

    -webkit-text-fill-color:
        #172554 !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {

    color: #172554 !important;

    -webkit-text-fill-color:
        #172554 !important;
}

[data-baseweb="select"] [class*="singleValue"] {

    color: #172554 !important;
}

[data-baseweb="select"] svg {

    fill: #172554 !important;

    color: #172554 !important;
}

[data-baseweb="select"] > div:hover {

    border-color: #2563EB !important;
}


/* =========================================================
MENU DO SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] {
    background-color: #FFFFFF !important;
}

[role="option"] {

    background-color: #FFFFFF !important;

    color: #172554 !important;

    -webkit-text-fill-color:
        #172554 !important;
}

[role="option"]:hover {

    background-color: #DBEAFE !important;

    color: #172554 !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {

    background:
        linear-gradient(
            135deg,
            #2563EB,
            #1D4ED8
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(37,99,235,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    background:
        linear-gradient(
            135deg,
            #1D4ED8,
            #1E40AF
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {

    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #93C5FD;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {

    margin-top: 50px;

    text-align: center;

    color: #475569 !important;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Aluno",
        "Curso",
        "Semestre",
        "Média",
        "Status",
        "Professor"
    ]

    if os.path.exists(ARQUIVO):

        try:
            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# =========================================================
# GARANTIR COLUNAS NECESSÁRIAS
# =========================================================

colunas_necessarias = [
    "Aluno",
    "Curso",
    "Semestre",
    "Média",
    "Status",
    "Professor"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


# =========================================================
# CONVERTER VALORES
# =========================================================

df["Semestre"] = pd.to_numeric(
    df["Semestre"],
    errors="coerce"
).fillna(0)

df["Média"] = pd.to_numeric(
    df["Média"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
🎓 Gestão Escolar
</div>

<div class="logo-subtitle">
SISTEMA DE GESTÃO DE ALUNOS
</div>
""",
unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Aluno",
        "👩‍🎓 Alunos Cadastrados"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "Gestão Escolar • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
    f"""
    <div class="hero-container"
    style="background-image: url('{IMAGEM_HERO}');">

        <div class="hero-overlay"></div>

        <div class="hero-content">

            <div class="hero-number">
            01.
            </div>

            <div class="hero-title">
            Seus alunos.<br>
            Sua organização.
            </div>

            <div class="hero-text">
            Tenha todas as informações dos alunos organizadas
            em um único lugar.<br>
            Cadastre, consulte e acompanhe os estudantes
            de forma simples e eficiente.
            </div>

            <div class="hero-badge">
            🎓 GESTÃO ESCOLAR
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
    )


    st.markdown(
    """
    <div class="page-title">
    📊 Visão geral dos alunos
    </div>

    <div class="page-subtitle">
    Acompanhe os principais dados dos estudantes cadastrados.
    </div>
    """,
    unsafe_allow_html=True
    )


    # =====================================================
    # INDICADORES
    # =====================================================

    total_alunos = len(df)

    media_geral = df["Média"].mean() if not df.empty else 0

    cursos = (
        df["Curso"].nunique()
        if not df.empty
        else 0
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
        f"""
        <div class="info-card">

            <div class="card-icon">
            👩‍🎓
            </div>

            <div class="card-number">
            {total_alunos}
            </div>

            <div class="card-label">
            ALUNOS CADASTRADOS
            </div>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col2:

        st.markdown(
        f"""
        <div class="info-card">

            <div class="card-icon">
            ⭐
            </div>

            <div class="card-number">
            {media_geral:.1f}
            </div>

            <div class="card-label">
            MÉDIA GERAL
            </div>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col3:

        st.markdown(
        f"""
        <div class="info-card">

            <div class="card-icon">
            📚
            </div>

            <div class="card-number">
            {cursos}
            </div>

            <div class="card-label">
            CURSOS CADASTRADOS
            </div>

        </div>
        """,
        unsafe_allow_html=True
        )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
        """
        <div class="dark-card">

            <h2>
            🚀 Organização escolar
            </h2>

            <p>
            O Gestão Escolar permite manter as informações
            dos alunos organizadas em um único lugar.
            </p>

            <p>
            Cadastre, consulte, pesquise e acompanhe
            os estudantes de maneira simples e moderna.
            </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_ESCOLA,
            use_container_width=True
        )


# =========================================================
# CADASTRAR ALUNO
# =========================================================

elif menu == "➕ Cadastrar Aluno":

    st.markdown(
    """
    <div class="page-title">
    ➕ Novo aluno
    </div>

    <div class="page-subtitle">
    Adicione um novo estudante ao sistema.
    </div>
    """,
    unsafe_allow_html=True
    )


    with st.form(
        "cadastro_aluno",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            aluno = st.text_input(
                "👤 Nome do aluno"
            )

            curso = st.selectbox(
                "📚 Curso",
                [
                    "Informática",
                    "Automação",
                    "Eletromecânica",
                    "Administração",
                    "Edificações",
                    "Outro"
                ]
            )

            semestre = st.number_input(
                "📅 Semestre",
                min_value=1,
                max_value=10,
                value=1,
                step=1
            )


        with col2:

            media = st.number_input(
                "⭐ Média",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1
            )

            status = st.selectbox(
                "📌 Status",
                [
                    "Ativo",
                    "Inativo"
                ]
            )

            professor = st.text_input(
                "👨‍🏫 Professor responsável"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR ALUNO"
        )


    if cadastrar:

        if aluno.strip() and professor.strip():

            novo_aluno = pd.DataFrame(
                [{
                    "Aluno": aluno.strip(),
                    "Curso": curso,
                    "Semestre": int(semestre),
                    "Média": float(media),
                    "Status": status,
                    "Professor": professor.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_aluno
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🎓 Aluno cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha o nome do aluno e o professor."
            )


# =========================================================
# ALUNOS CADASTRADOS
# =========================================================

elif menu == "👩‍🎓 Alunos Cadastrados":

    st.markdown(
    """
    <div class="page-title">
    👩‍🎓 Alunos cadastrados
    </div>

    <div class="page-subtitle">
    Consulte e pesquise todos os estudantes cadastrados.
    </div>
    """,
    unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
        """
        <div class="dark-card">

            <h2>
            🎓 Nenhum aluno cadastrado
            </h2>

            <p>
            Ainda não existem alunos cadastrados.
            Cadastre o primeiro aluno para começar.
            </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar aluno",
            placeholder="Digite nome, curso ou professor..."
        )


        if busca:

            mascara = (

                df.astype(str)

                .apply(
                    lambda coluna:

                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )

                .any(axis=1)
            )


            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        # =================================================
        # EXCLUSÃO
        # =================================================

        opcoes_alunos = df.index.tolist()


        aluno_excluir = st.selectbox(
            "🗑️ Selecione um aluno para excluir",

            options=opcoes_alunos,

            format_func=lambda indice:

                f"{df.loc[indice, 'Aluno']} - "
                f"{df.loc[indice, 'Curso']}"
        )


        if st.button(
            "🗑️ EXCLUIR ALUNO"
        ):

            df = df.drop(
                aluno_excluir
            )


            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🎓 Aluno excluído com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

🎓 Gestão Escolar<br>
Sistema de Gestão de Alunos

</div>
""",
unsafe_allow_html=True
)
