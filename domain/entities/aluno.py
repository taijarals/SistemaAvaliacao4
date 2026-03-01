class Aluno:

    def __init__(self, id, nome, status, disciplinas=None):
        self.id = id
        self.nome = nome
        self.status = status
        self.disciplinas = disciplinas or []