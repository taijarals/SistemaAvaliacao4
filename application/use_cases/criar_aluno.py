from domain.entities.aluno import Aluno

class CriarAluno:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, nome, status, disciplinas):

        aluno = Aluno(
            id=None,
            nome=nome,
            status=status,
            disciplinas=disciplinas
        )

        self.repository.salvar(aluno)