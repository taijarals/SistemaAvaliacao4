from domain.entities.disciplina import Disciplina

class AtualizarDisciplina:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, disciplina_id, nome, curso, dia):

        disciplina_existente = self.repository.buscar_por_id(disciplina_id)

        if not disciplina_existente:
            raise Exception("Disciplina não encontrada.")

        disciplina_atualizada = Disciplina(
            id=disciplina_id,
            nome=nome,
            curso=curso,
            dia=dia
        )