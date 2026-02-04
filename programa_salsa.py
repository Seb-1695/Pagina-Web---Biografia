class Salsa:
    #Metodo constructor   
    def __init__(self):
            self.motivacion=True
            self.energia=100
            self.edad=0

    def hacer_patineta(self):
        self.energia=self.energia-1
        if (self.energia=self.energia<=0):
            print("Me canse")

    def hacer_patineta(self):
    

jose=Salsa()

for _ in range(2):
    jose.hacer_patineta()

for _ in range(2):
    jose.hacer_dinos()

for _ in range(2):
    jose.dar_beso()

for _ in range(1):
    jose.descansar()