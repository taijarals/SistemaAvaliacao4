from domain.repositories.disciplina_repository import DisciplinaRepository
from infrastructure.database.supabase_connection import get_supabase

class SupabaseDisciplinaRepository(DisciplinaRepository):

    def __init__(self):
        self.db = get_supabase()

    def listar(self):
        return self.db.table("disciplinas").select("*").execute().data

    def salvar(self, disciplina):
        self.db.table("disciplinas").insert({
            "nome_disciplina": disciplina.nome,
            "nome_curso": disciplina.curso,
            "dia_aula": disciplina.dia
        }).execute()

    def excluir(self, id):
        self.db.table("disciplinas").delete().eq("id", id).execute()

    def contar_desafios(self, id):
        result = self.db.table("desafios").select("id").eq("fk_disciplina", id).execute()
        return len(result.data)