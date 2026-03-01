# main.py

import streamlit as st

# Infra
from infrastructure.repositories.disciplina_repository_impl import SupabaseDisciplinaRepository

# Application
from application.use_cases.criar_disciplina import CriarDisciplina
from application.use_cases.listar_disciplinas import ListarDisciplinas
from application.use_cases.excluir_disciplina import ExcluirDisciplina

# Presentation
from presentation.pages.disciplinas_page import render_disciplinas_page


def main():

    # ==========================
    # COMPOSITION ROOT
    # ==========================

    repo = SupabaseDisciplinaRepository()

    criar_uc = CriarDisciplina(repo)
    listar_uc = ListarDisciplinas(repo)
    excluir_uc = ExcluirDisciplina(repo)

    # ==========================
    # RENDER PAGE
    # ==========================

    render_disciplinas_page(
        criar_use_case=criar_uc,
        listar_use_case=listar_uc,
        excluir_use_case=excluir_uc,
        atualizar_use_case=atualizar_uc
    )


if __name__ == "__main__":
    main()