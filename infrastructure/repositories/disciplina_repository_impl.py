from infrastructure.database.supabase_connection import get_supabase
from domain.entities.disciplina import Disciplina


class SupabaseDisciplinaRepository:

    def __init__(self):
        self.supabase = get_supabase()
        self.table = "disciplinas"

    def salvar(self, disciplina: Disciplina):
        self.supabase.table(self.table).insert({
            "nome": disciplina.nome,
            "curso": disciplina.curso,
            "dia": disciplina.dia
        }).execute()

    def listar(self):
        response = self.supabase.table(self.table).select("*").execute()

        disciplinas = []
        for item in response.data:
            disciplinas.append(
                Disciplina(
                    id=item["id"],
                    nome=item["nome"],
                    curso=item["curso"],
                    dia=item["dia"]
                )
            )
        return disciplinas

    def buscar_por_id(self, disciplina_id):
        response = self.supabase.table(self.table)\
            .select("*")\
            .eq("id", disciplina_id)\
            .single()\
            .execute()

        if not response.data:
            return None

        item = response.data

        return Disciplina(
            id=item["id"],
            nome=item["nome"],
            curso=item["curso"],
            dia=item["dia"]
        )

    def excluir(self, disciplina_id):
        self.supabase.table(self.table)\
            .delete()\
            .eq("id", disciplina_id)\
            .execute()

    def atualizar(self, disciplina: Disciplina):
        self.supabase.table(self.table)\
            .update({
                "nome": disciplina.nome,
                "curso": disciplina.curso,
                "dia": disciplina.dia
            })\
            .eq("id", disciplina.id)\
            .execute()