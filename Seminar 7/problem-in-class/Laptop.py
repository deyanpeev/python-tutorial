from Computer import Computer

class Laptop(Computer):
    pass
    def __init__(self, cpu, memory, storage, gpu):
        Computer.__init__(self, cpu, memory, storage)
        self.__gpu = gpu

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, value):
        self._memory = value

    def startPlayingGames(self, game):
        if(self.__gpu < 2):
            print("You can't play games on this laptop.")
        else:
            print(f"Playing {game}")

    def startDesigning(self):
        if(self.__gpu < 1):
            print("You can't use this laptop for design.")
        else:
            print("Designing")