class ServicoAutenticacao:
    def __init__(self):
        self.usuarios = {"aluno1": "senha123", "admin": "senhadministrador"}
        self.usuarios_logados = []

    def login(self, usuario, senha):
        if usuario in self.usuarios and self.usuarios[usuario] == senha:
            self.usuarios_logados.append(usuario)
            return True
        return False

    def esta_logado(self, usuario):
        return usuario in self.usuarios_logados
