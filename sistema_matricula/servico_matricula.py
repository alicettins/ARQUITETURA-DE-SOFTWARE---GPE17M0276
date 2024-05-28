class ServicoMatricula:
    def __init__(self, servico_autenticacao, servico_curso):
        self.servico_autenticacao = servico_autenticacao
        self.servico_curso = servico_curso
        self.matriculas = {}

    def matricular(self, usuario, codigo_curso):
        if not self.servico_autenticacao.esta_logado(usuario):
            return "Usuário não está logado."
        if codigo_curso not in self.servico_curso.obter_cursos():
            return "Curso não encontrado."
        curso = self.servico_curso.obter_cursos()[codigo_curso]
        if curso["vagas_disponiveis"] <= 0:
            return "Não há vagas disponíveis."

        if usuario not in self.matriculas:
            self.matriculas[usuario] = []
        self.matriculas[usuario].append(codigo_curso)
        self.servico_curso.atualizar_vagas_curso(codigo_curso, -1)
        return "Matrícula realizada com sucesso."

    def obter_matriculas(self, usuario):
        if usuario not in self.matriculas:
            return []
        return self.matriculas[usuario]
