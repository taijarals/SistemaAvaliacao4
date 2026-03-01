from domain.entities.aluno import Aluno

class SupabaseAlunoRepository:

    def __init__(self, supabase):
        self.supabase = supabase

    def salvar(self, aluno):

        # 1. salvar aluno
        response = self.supabase.table("alunos").insert({
            "nome": aluno.nome,
            "status": aluno.status
        }).execute()

        aluno_id = response.data[0]["id"]

        # 2. salvar vínculos
        for disciplina_id in aluno.disciplinas:
            self.supabase.table("aluno_disciplinas").insert({
                "fk_aluno": aluno_id,
                "fk_disciplina": disciplina_id
            }).execute()

    def listar(self):

        response = self.supabase.table("alunos").select("*").execute()

        alunos = []

        for item in response.data:

            # buscar disciplinas do aluno
            vinculos = self.supabase.table("aluno_disciplinas")\
                .select("fk_disciplina")\
                .eq("fk_aluno", item["id"])\
                .execute()

            disciplinas_ids = [v["fk_disciplina"] for v in vinculos.data]

            alunos.append(
                Aluno(
                    id=item["id"],
                    nome=item["nome"],
                    status=item["status"],
                    disciplinas=disciplinas_ids
                )
            )

        return alunos