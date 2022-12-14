from Laptop import Laptop

class GamingLaptop(Laptop):
    def __init__(self, cpu, memory, storage):
        Laptop.__init__(self, cpu, memory, storage, 5)

    def playExtremeGames():
        print("Playing some super cool games.")