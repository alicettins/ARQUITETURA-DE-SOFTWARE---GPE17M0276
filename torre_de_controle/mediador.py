from abc import ABC, abstractmethod

class Mediador(ABC):
    
    def notificar(self, remetente: object, evento: str) -> None:
        pass

class TorreDeControle(Mediador):
    def __init__(self):
        self.aeronaves = []
        self.radar = Radar(self)
    
    def adicionar_aeronave(self, aeronave):
        self.aeronaves.append(aeronave)
    
    def notificar(self, remetente: object, evento: str) -> None:
        if evento == "decolar":
            self._informar_aeronaves(f"{remetente.identificador} está decolando", remetente)
            self.radar.enviar_sinal(f"{remetente.identificador} está decolando")
        elif evento == "pousar":
            self._informar_aeronaves(f"{remetente.identificador} está pousando", remetente)
            self.radar.enviar_sinal(f"{remetente.identificador} está pousando")
    
    def _informar_aeronaves(self, mensagem: str, remetente: object) -> None:
        for aeronave in self.aeronaves:
            if aeronave != remetente:
                aeronave.receber_informacao(mensagem)

class Radar:
    def __init__(self, mediador: Mediador):
        self.mediador = mediador
    
    def enviar_sinal(self, mensagem: str) -> None:
        print(f"Radar envia sinal: {mensagem}")
