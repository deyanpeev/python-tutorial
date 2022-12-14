class Computer:
    def __init__(self, cpu, memory, storage):
        self.__cpu = cpu
        self.__memory = memory
        self.__storage = storage

    @property
    def _memory(self):
        return self.__memory

    @_memory.setter
    def _memory(self, value):
        self.__memory = value
    
    def __str__(self) -> str:
        return f"CPUs: {self.__cpu}; Memory: {self.__memory}; Storage: {self.__storage}; "
