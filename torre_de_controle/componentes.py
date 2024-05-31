from mediador import Mediador

class Aeronave:
    def __init__(self, identificador: str, mediador: Mediador):
        self.identificador = identificador
        self.mediador = mediador
        self.mediador.adicionar_aeronave(self)
    
    def decolar(self) -> None:
        print(f"{self.identificador} solicitando decolagem")
        self.mediador.notificar(self, "decolar")
    
    def pousar(self) -> None:
        print(f"{self.identificador} solicitando pouso")
        self.mediador.notificar(self, "pousar")
    
    def receber_informacao(self, mensagem: str) -> None:
        print(f"{self.identificador} recebeu: {mensagem}")
