class ExcluirDisciplina:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, disciplina_id):
        disciplina = self.repository.buscar_por_id(disciplina_id)

        if not disciplina:
            raise Exception("Disciplina não encontrada.")

        self.repository.excluir(disciplina_id)