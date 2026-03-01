from infrastructure.database.supabase_connection import get_supabase
from domain.entities.disciplina import Disciplina


class SupabaseDisciplinaRepository:

    def __init__(self):
        self.supabase = get_supabase()
        self.table = "disciplinas"

    def salvar(self, disciplina: Disciplina):
        self.supabase.table(self.table).insert({
            "nome_disciplina": disciplina.nome,
            "nome_curso": disciplina.curso,
            "dia_aula": disciplina.dia
        }).execute()

    def listar(self):
        response = self.supabase.table(self.table).select("*").execute()

        disciplinas = []
        for item in response.data:
            disciplinas.append(
                Disciplina(
                    id=item["id"],
                    nome=item["nome_disciplina"],
                    curso=item["nome_curso"],
                    dia=item["dia_aula"]
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
            nome=item["nome_disciplina"],
            curso=item["nome_curso"],
            dia=item["dia_aula"]
        )

    def excluir(self, disciplina_id):
        self.supabase.table(self.table)\
            .delete()\
            .eq("id", disciplina_id)\
            .execute()

    def atualizar(self, disciplina: Disciplina):
        self.supabase.table(self.table)\
            .update({
                "nome_disciplina": disciplina.nome,
                "nome_curso": disciplina.curso,
                "dia_aula": disciplina.dia
            })\
            .eq("id", disciplina.id)\
            .execute()