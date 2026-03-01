# presentation/pages/disciplinas_page.py

import streamlit as st


def render_disciplinas_page(
    criar_use_case,
    listar_use_case,
    excluir_use_case,
    atualizar_use_case
):

    st.title("📘 Gestão de Disciplinas")

    # ==========================
    # CRIAR
    # ==========================

    with st.form("form_criar"):
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

    # ==========================
    # LISTAR
    # ==========================

    disciplinas = listar_use_case.execute()

    for disciplina in disciplinas:

        with st.expander(disciplina.nome):

            st.write("Curso:", disciplina.curso)
            st.write("Dia:", disciplina.dia)

            col1, col2 = st.columns(2)

            # ==========================
            # BOTÃO EDITAR
            # ==========================

            if col1.button("Editar", key=f"edit_{disciplina.id}"):
                st.session_state["edit_id"] = disciplina.id

            # ==========================
            # BOTÃO EXCLUIR
            # ==========================

            if col2.button("Excluir", key=f"del_{disciplina.id}"):
                try:
                    excluir_use_case.execute(disciplina.id)
                    st.success("Excluída!")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))

    # ==========================
    # FORM DE EDIÇÃO
    # ==========================

    if "edit_id" in st.session_state:

        disciplina_edit = next(
            (d for d in disciplinas if d.id == st.session_state["edit_id"]),
            None
        )

        if disciplina_edit:

            st.subheader("✏️ Editar Disciplina")

            novo_nome = st.text_input(
                "Nome",
                value=disciplina_edit.nome,
                key="edit_nome"
            )

            novo_curso = st.text_input(
                "Curso",
                value=disciplina_edit.curso,
                key="edit_curso"
            )

            novo_dia = st.text_input(
                "Dia",
                value=disciplina_edit.dia,
                key="edit_dia"
            )

            col1, col2 = st.columns(2)

            if col1.button("Atualizar"):
                try:
                    atualizar_use_case.execute(
                        disciplina_edit.id,
                        novo_nome,
                        novo_curso,
                        novo_dia
                    )
                    del st.session_state["edit_id"]
                    st.success("Atualizada!")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))

            if col2.button("Cancelar"):
                del st.session_state["edit_id"]
                st.rerun()