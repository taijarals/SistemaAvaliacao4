class Disciplina:
    def __init__(self, id, nome, curso, dia):
        if not nome:
            raise ValueError("Nome é obrigatório")

        self.id = id
        self.nome = nome_disciplina
        self.curso = nome_curso
        self.dia = dia_aula