# Sistema de Gerenciamento de Biblioteca usando MVC

# Camada Modelo
class Livro:
    def __init__(self, titulo, autor, numero_registro):
        self.titulo = titulo
        self.autor = autor
        self.numero_registro = numero_registro
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ID: {self.numero_registro})"

# Camada de Persistência 
class BibliotecaPersistencia:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def buscar_livro_por_titulo(self, titulo):
        return [livro for livro in self.livros if livro.titulo.lower() == titulo.lower()]

    def buscar_livro_por_autor(self, autor):
        return [livro for livro in self.livros if livro.autor.lower() == autor.lower()]

    def obter_livro_por_numero_registro(self, numero_registro):
        for livro in self.livros:
            if livro.numero_registro == numero_registro:
                return livro
        return None

# Camada de Aplicação
class BibliotecaAplicacao:
    def __init__(self, persistencia):
        self.persistencia = persistencia

    def adicionar_livro(self, titulo, autor, numero_registro):
        novo_livro = Livro(titulo, autor, numero_registro)
        self.persistencia.adicionar_livro(novo_livro)

    def buscar_livro_por_titulo(self, titulo):
        return self.persistencia.buscar_livro_por_titulo(titulo)

    def buscar_livro_por_autor(self, autor):
        return self.persistencia.buscar_livro_por_autor(autor)

    def emprestar_livro(self, numero_registro):
        livro = self.persistencia.obter_livro_por_numero_registro(numero_registro)
        if livro and livro.disponivel:
            livro.disponivel = False
            return True
        return False

    def devolver_livro(self, numero_registro):
        livro = self.persistencia.obter_livro_por_numero_registro(numero_registro)
        if livro and not livro.disponivel:
            livro.disponivel = True
            return True
        return False

# Camada de Apresentação 
class BibliotecaUI:
    def __init__(self, aplicacao):
        self.aplicacao = aplicacao

    def menu_principal(self):
        while True:
            print("\n--- Menu da Biblioteca ---")
            print("1. ---Adicionar Livro---")
            print("2. ---Buscar Livro por Título---")
            print("3. ---Buscar Livro por Autor---")
            print("4. ---Emprestar Livro---")
            print("5. ---Devolver Livro---")
            print("6. ---Sair---")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.adicionar_livro()
            elif escolha == "2":
                self.buscar_livro_por_titulo()
            elif escolha == "3":
                self.buscar_livro_por_autor()
            elif escolha == "4":
                self.emprestar_livro()
            elif escolha == "5":
                self.devolver_livro()
            elif escolha == "6":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, por favor tente novamente.")

    def adicionar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        numero_registro = input("Número de Registro: ")
        self.aplicacao.adicionar_livro(titulo, autor, numero_registro)
        print("Livro adicionado com sucesso!")

    def buscar_livro_por_titulo(self):
        titulo = input("Título: ")
        livros = self.aplicacao.buscar_livro_por_titulo(titulo)
        if livros:
            for livro in livros:
                print(livro)
        else:
            print("Nenhum livro encontrado com este título.")

    def buscar_livro_por_autor(self):
        autor = input("Autor: ")
        livros = self.aplicacao.buscar_livro_por_autor(autor)
        if livros:
            for livro in livros:
                print(livro)
        else:
            print("Nenhum livro encontrado com este autor.")

    def emprestar_livro(self):
        numero_registro = input("Número de Registro do Livro: ")
        if self.aplicacao.emprestar_livro(numero_registro):
            print("Livro emprestado com sucesso!")
        else:
            print("Livro não disponível ou não encontrado.")

    def devolver_livro(self):
        numero_registro = input("Número de Registro do Livro: ")
        if self.aplicacao.devolver_livro(numero_registro):
            print("Livro devolvido com sucesso!")
        else:
            print("Livro não encontrado ou já está disponível.")

# Função Principal
def main():
    persistencia = BibliotecaPersistencia()
    aplicacao = BibliotecaAplicacao(persistencia)
    ui = BibliotecaUI(aplicacao)
    ui.menu_principal()

if __name__ == "__main__":
    main()
