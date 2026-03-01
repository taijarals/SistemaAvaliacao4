from abc import ABC, abstractmethod

class DisciplinaRepository(ABC):

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def salvar(self, disciplina):
        pass

    @abstractmethod
    def excluir(self, id):
        pass

    @abstractmethod
    def contar_desafios(self, id):
        pass