# presentation/pages/disciplinas_page.py

import streamlit as st

def render_disciplinas_page(
    criar_use_case,
    listar_use_case,
    excluir_use_case
):

    st.title("📘 Gestão de Disciplinas")

    with st.form("form"):
        nome = st.text_input("Nome")
        curso = st.text_input("Curso")
        dia = st.text_input("Dia")

        if st.form_submit_button("Salvar"):
            try:
                criar_use_case.execute(nome, curso, dia)
                st.success("Criada!")
                st.rerun()
            except Exception as e:
                st.error(str(e))

    disciplinas = listar_use_case.execute()

    for disciplina in disciplinas:
        with st.expander(disciplina.nome_disciplina):

            if st.button("Excluir", key=f"del_{disciplina.id}"):
                try:
                    excluir_use_case.execute(disciplina.id)
                    st.success("Excluída!")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))