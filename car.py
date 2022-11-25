class Fordon:
    def __init__ (self, namn:str, ljud:str, färg:str , ålder:int) -> None:
        self.namn = namn
        self.ljud = ljud
        self.färg = färg
        self.ålder = ålder 
    def låta(self):
        for _ in range(3):
            print(self.ljud)

    def ändra_färg(self, ny_färg:str):
        self.färg = ny_färg

class Bil(Fordon):
    def __init__ (self, namn:str, ljud:str, färg:str, ålder: int, bränsle: str, hästkrafter: int, besiktad:bool, utsläpp:int) -> None:
        super().__init__(namn, ljud, färg, ålder)
        self.bränsle = bränsle
        self.hästkraft = hästkrafter
        self.besiktad = besiktad
        self.utsläpp = utsläpp 
    
    def tanka(self, mängd:float):
        pass
    
    def kör(self, sträcka:int) -> float:
        return self.utsläpp*sträcka
    