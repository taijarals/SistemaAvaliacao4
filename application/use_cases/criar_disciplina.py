from domain.entities.disciplina import Disciplina

class CriarDisciplina:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, nome, curso, dia):

        disciplina = Disciplina(
            id=None,
            nome=nome,
            curso=curso,
            dia=dia
        )

        self.repository.salvar(disciplina)