# domain/repositories/aluno_repository.py

from abc import ABC, abstractmethod

class AlunoRepository(ABC):

    @abstractmethod
    def salvar(self, aluno):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def excluir(self, aluno_id):
        pass

    @abstractmethod
    def atualizar(self, aluno):
        pass

    @abstractmethod
    def buscar_por_id(self, aluno_id):
        pass