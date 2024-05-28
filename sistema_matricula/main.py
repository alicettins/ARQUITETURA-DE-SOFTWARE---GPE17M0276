from servico_autenticacao import ServicoAutenticacao
from servico_curso import ServicoCurso
from servico_matricula import ServicoMatricula

def main():
    servico_autenticacao = ServicoAutenticacao()
    servico_curso = ServicoCurso()
    servico_matricula = ServicoMatricula(servico_autenticacao, servico_curso)

    # Simulando login de usuário
    usuario = "aluno1"
    senha = "senha123"
    if servico_autenticacao.login(usuario, senha):
        print(f"Usuário {usuario} logado com sucesso.")
    else:
        print(f"Falha no login do usuário {usuario}.")

    # Listando cursos disponíveis
    print("Cursos disponíveis:")
    for codigo, detalhes in servico_curso.obter_cursos().items():
        print(f"{codigo}: {detalhes['nome']} (Vagas: {detalhes['vagas_disponiveis']})")

    # Realizando matrícula
    codigo_curso = "ARQ_SOFT_101"
    status_matricula = servico_matricula.matricular(usuario, codigo_curso)
    print(status_matricula)

    # Verificando matrículas do usuário
    print(f"Matrículas do usuário {usuario}: {servico_matricula.obter_matriculas(usuario)}")

if __name__ == "__main__":
    main()
