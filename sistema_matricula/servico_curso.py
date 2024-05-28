class ServicoCurso:
    def __init__(self):
        self.cursos = {
            "UC101010": {"nome": "ENGENHARIA DE SOFTWARE", "vagas_disponiveis": 30},
            "ARQ_SOFT_101": {"nome": "ARQUITETURA DE SOFTWARE ", "vagas_disponiveis": 25}
        }

    def obter_cursos(self):
        return self.cursos

    def atualizar_vagas_curso(self, codigo_curso, vagas):
        if codigo_curso in self.cursos:
            self.cursos[codigo_curso]["vagas_disponiveis"] += vagas
            return True
        return False
