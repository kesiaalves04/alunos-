import streamlit as st
import pandas as pd
import os

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Gestão Escolar",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "alunos.csv"


# ============================================================
# ESTILO DA PÁGINA
# ============================================================

st.markdown("""
<style>

    /* Fundo geral */
    .stApp {
        background: #eef3ff;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #172554, #1e3a8a);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Título principal */
    .titulo {
        font-size: 42px;
        font-weight: 800;
        color: #172554;
        margin-bottom: 5px;
    }

    .subtitulo {
        font-size: 17px;
        color: #475569;
        margin-bottom: 25px;
    }

    /* Hero */
    .hero {
        position: relative;
        background: linear-gradient(
            135deg,
            #172554,
            #2563eb
        );
        border-radius: 25px;
        padding: 45px;
        margin-bottom: 30px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    .hero-number {
        font-size: 18px;
        font-weight: bold;
        color: #bfdbfe;
        margin-bottom: 15px;
    }

    .hero-title {
        font-size: 38px;
        font-weight: 800;
        color: white;
        line-height: 1.2;
        margin-bottom: 15px;
    }

    .hero-text {
        font-size: 17px;
        color: #dbeafe;
        line-height: 1.6;
    }

    /* Cards */
    .card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        min-height: 170px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        border: 1px solid #dbeafe;
    }

    .card-icon {
        font-size: 30px;
        margin-bottom: 10px;
    }

    .card-number {
        font-size: 35px;
        font-weight: 800;
        color: #172554;
    }

    .card-label {
        font-size: 13px;
        font-weight: 700;
        color: #64748b;
        margin-top: 5px;
        letter-spacing: 1px;
    }

    /* Caixa de informação */
    .info-box {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin-top: 30px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    }

    .info-title {
        font-size: 23px;
        font-weight: 700;
        color: #172554;
        margin-bottom: 10px;
    }

    /* Rodapé */
    .footer {
        text-align: center;
        color: #64748b;
        padding: 35px 0 15px 0;
        font-size: 14px;
    }

    /* Botões */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNÇÕES
# ============================================================

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
            df = pd.read_csv(ARQUIVO)

            # Garante que todas as colunas existam
            for coluna in colunas:
                if coluna not in df.columns:
                    df[coluna] = ""

            df = df[colunas]

            # Converte média para número
            df["Média"] = pd.to_numeric(
                df["Média"],
                errors="coerce"
            ).fillna(0)

            return df

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(df):
    df.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


# ============================================================
# CARREGAR DADOS
# ============================================================

df = carregar_dados()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center; padding:15px 0 25px 0;">
        <div style="font-size:45px;">🎓</div>
        <div style="font-size:26px; font-weight:800;">
            Gestão Escolar
        </div>
        <div style="font-size:12px; margin-top:8px;">
            SISTEMA DE GESTÃO DE ALUNOS
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### NAVEGAÇÃO")

    menu = st.radio(
        "Escolha uma opção:",
        [
            "🏠 Dashboard",
            "➕ Cadastrar Aluno",
            "🎓 Alunos Cadastrados"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("""
    <div style="text-align:center; padding:10px;">
        <b>Gestão Escolar • 2026</b>
        <br>
        <small>Sistema de gerenciamento de alunos</small>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DASHBOARD
# ============================================================

if menu == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">

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

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="titulo">📊 Visão geral dos alunos</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Acompanhe os principais dados dos estudantes cadastrados.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # CÁLCULOS
    # --------------------------------------------------------

    total_alunos = len(df)

    if total_alunos > 0:
        media_geral = df["Média"].mean()
        total_cursos = df["Curso"].nunique()
    else:
        media_geral = 0
        total_cursos = 0

    # --------------------------------------------------------
    # CARDS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(f"""
        <div class="card">

            <div class="card-icon">
                🎓
            </div>

            <div class="card-number">
                {total_alunos}
            </div>

            <div class="card-label">
                ALUNOS CADASTRADOS
            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="card">

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
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div class="card">

            <div class="card-icon">
                📚
            </div>

            <div class="card-number">
                {total_cursos}
            </div>

            <div class="card-label">
                CURSOS CADASTRADOS
            </div>

        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # TABELA
    # --------------------------------------------------------

    st.markdown("""
    <div class="info-box">

        <div class="info-title">
            📋 Alunos cadastrados
        </div>

    </div>
    """, unsafe_allow_html=True)

    if not df.empty:

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "Nenhum aluno cadastrado ainda."
        )


# ============================================================
# CADASTRAR ALUNO
# ============================================================

elif menu == "➕ Cadastrar Aluno":

    st.markdown(
        '<div class="titulo">➕ Cadastrar aluno</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Preencha os dados abaixo para cadastrar um novo estudante.'
        '</div>',
        unsafe_allow_html=True
    )

    with st.form("formulario_aluno"):

        col1, col2 = st.columns(2)

        with col1:

            nome = st.text_input(
                "Nome do aluno"
            )

            curso = st.selectbox(
                "Curso",
                [
                    "Informática",
                    "Automação",
                    "Eletromecânica"
                ]
            )

            semestre = st.number_input(
                "Semestre",
                min_value=1,
                max_value=8,
                value=1,
                step=1
            )

        with col2:

            media = st.number_input(
                "Média",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1
            )

            status = st.selectbox(
                "Status",
                [
                    "Ativo",
                    "Inativo"
                ]
            )

            professor = st.text_input(
                "Professor responsável"
            )

        enviar = st.form_submit_button(
            "💾 Cadastrar aluno",
            use_container_width=True
        )

    if enviar:

        if nome.strip() == "":

            st.error(
                "Digite o nome do aluno."
            )

        elif professor.strip() == "":

            st.error(
                "Digite o nome do professor."
            )

        else:

            novo_aluno = pd.DataFrame(
                {
                    "Aluno": [nome],
                    "Curso": [curso],
                    "Semestre": [semestre],
                    "Média": [media],
                    "Status": [status],
                    "Professor": [professor]
                }
            )

            df = pd.concat(
                [df, novo_aluno],
                ignore_index=True
            )

            salvar_dados(df)

            st.success(
                f"Aluno {nome} cadastrado com sucesso! 🎉"
            )

            st.rerun()


# ============================================================
# ALUNOS CADASTRADOS
# ============================================================

elif menu == "🎓 Alunos Cadastrados":

    st.markdown(
        '<div class="titulo">🎓 Alunos cadastrados</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Consulte, pesquise e remova alunos do sistema.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # PESQUISA
    # --------------------------------------------------------

    pesquisa = st.text_input(
        "🔎 Pesquisar aluno",
        placeholder="Digite o nome do aluno..."
    )

    df_filtrado = df.copy()

    if pesquisa:

        df_filtrado = df[
            df["Aluno"]
            .astype(str)
            .str.contains(
                pesquisa,
                case=False,
                na=False
            )
        ]

    # --------------------------------------------------------
    # MOSTRAR TABELA
    # --------------------------------------------------------

    if not df_filtrado.empty:

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.subheader("🗑️ Remover aluno")

        nomes = df_filtrado["Aluno"].tolist()

        aluno_remover = st.selectbox(
            "Selecione o aluno:",
            nomes
        )

        if st.button(
            "🗑️ Remover aluno",
            use_container_width=True
        ):

            df = df[
                df["Aluno"] != aluno_remover
            ]

            salvar_dados(df)

            st.success(
                f"{aluno_remover} foi removido do sistema."
            )

            st.rerun()

    else:

        st.info(
            "Nenhum aluno encontrado."
        )


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("""
<div class="footer">
    🎓 Gestão Escolar • Sistema de Gestão de Alunos • 2026
</div>
""", unsafe_allow_html=True)
