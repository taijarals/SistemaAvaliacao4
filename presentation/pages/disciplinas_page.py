import streamlit as st
from application.use_cases.criar_disciplina import CriarDisciplina
from infrastructure.repositories.disciplina_repository_impl import SupabaseDisciplinaRepository

repo = SupabaseDisciplinaRepository()
criar_use_case = CriarDisciplina(repo)

st.title("Gestão de Disciplinas")

with st.form("form"):
    nome = st.text_input("Nome")
    curso = st.text_input("Curso")
    dia = st.text_input("Dia")

    if st.form_submit_button("Salvar"):
        try:
            criar_use_case.execute(nome, curso, dia)
            st.success("Criada!")
        except Exception as e:
            st.error(str(e))