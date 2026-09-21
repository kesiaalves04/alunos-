import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Gestão Escolar",
    page_icon="🎓",
    layout="wide"
)

ARQUIVO = "alunos.csv"


# =========================
# FUNÇÃO PARA CARREGAR DADOS
# =========================

def carregar_dados():
    if os.path.exists(ARQUIVO):
        return pd.read_csv(ARQUIVO)

    return pd.DataFrame(
        columns=[
            "Aluno",
            "Curso",
            "Semestre",
            "Média",
            "Status",
            "Professor"
        ]
    )


# =========================
# FUNÇÃO PARA SALVAR DADOS
# =========================

def salvar_dados(df):
    df.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


# =========================
# CARREGAR DADOS
# =========================

df = carregar_dados()


# =========================
# SIDEBAR
# =========================

st.sidebar.title("🎓 Gestão Escolar")
st.sidebar.write("Sistema de Gestão de Alunos")

st.sidebar.markdown("---")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Aluno",
        "📚 Alunos Cadastrados"
    ]
)


# =========================
# DASHBOARD
# =========================

if pagina == "🏠 Dashboard":

    st.title("🎓 Gestão Escolar")

    st.subheader("Sistema de Gestão de Alunos")

    st.write(
        "Tenha as informações dos alunos organizadas "
        "em um único lugar."
    )

    st.markdown("---")

    total_alunos = len(df)

    if len(df) > 0:
        media = df["Média"].mean()
        cursos = df["Curso"].nunique()
    else:
        media = 0
        cursos = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎓 Alunos cadastrados",
            total_alunos
        )

    with col2:
        st.metric(
            "⭐ Média geral",
            f"{media:.1f}"
        )

    with col3:
        st.metric(
            "📚 Cursos",
            cursos
        )

    st.markdown("---")

    st.subheader("📋 Alunos cadastrados")

    if len(df) > 0:
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Nenhum aluno cadastrado.")


# =========================
# CADASTRAR ALUNO
# =========================

elif pagina == "➕ Cadastrar Aluno":

    st.title("➕ Cadastrar Aluno")

    st.write(
        "Preencha os dados abaixo para cadastrar um novo aluno."
    )

    nome = st.text_input("Nome do aluno")

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
        value=1
    )

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

    if st.button(
        "💾 Cadastrar aluno",
        use_container_width=True
    ):

        if nome.strip() == "":
            st.error("Digite o nome do aluno.")

        elif professor.strip() == "":
            st.error("Digite o professor responsável.")

        else:

            novo_aluno = pd.DataFrame({
                "Aluno": [nome],
                "Curso": [curso],
                "Semestre": [semestre],
                "Média": [media],
                "Status": [status],
                "Professor": [professor]
            })

            df = pd.concat(
                [df, novo_aluno],
                ignore_index=True
            )

            salvar_dados(df)

            st.success(
                "Aluno cadastrado com sucesso! 🎉"
            )

            st.rerun()


# =========================
# ALUNOS CADASTRADOS
# =========================

elif pagina == "📚 Alunos Cadastrados":

    st.title("📚 Alunos Cadastrados")

    st.write(
        "Consulte os alunos registrados no sistema."
    )

    if len(df) > 0:

        pesquisa = st.text_input(
            "🔎 Pesquisar aluno"
        )

        if pesquisa:

            resultado = df[
                df["Aluno"]
                .astype(str)
                .str.contains(
                    pesquisa,
                    case=False,
                    na=False
                )
            ]

        else:

            resultado = df

        st.dataframe(
            resultado,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.subheader("🗑️ Remover aluno")

        aluno = st.selectbox(
            "Escolha o aluno",
            df["Aluno"].tolist()
        )

        if st.button(
            "🗑️ Remover aluno",
            use_container_width=True
        ):

            df = df[
                df["Aluno"] != aluno
            ]

            salvar_dados(df)

            st.success(
                "Aluno removido com sucesso!"
            )

            st.rerun()

    else:

        st.info(
            "Ainda não existem alunos cadastrados."
        )
