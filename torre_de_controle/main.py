from mediador import TorreDeControle
from componentes import Aeronave

if __name__ == "__main__":
    torre_de_controle = TorreDeControle()
    
    aeronave1 = Aeronave("Aeronave 1", torre_de_controle)
    aeronave2 = Aeronave("Aeronave 2", torre_de_controle)
    
    aeronave1.decolar()
    aeronave2.pousar()
