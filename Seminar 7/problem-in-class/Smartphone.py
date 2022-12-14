from Computer import Computer

class Smartphone(Computer):
    pass
    def __init__(self, cpu, memory, storage, cellular, phoneNumber):
        Computer.__init__(self, cpu, memory, storage)
        self.__cellular = cellular
        self.__phoneNumber = phoneNumber


    def receivePhoneCall(self):
        print(f"{self.__phoneNumber} is receiving a call.")

    def makePhoneCall(self, to_number):
        print(f"{self.__phoneNumber} will call {to_number}")

    def __str__(self) -> str:
        return super().__str__() + f"Cellular: {self.__cellular}; Phone number: {self.__phoneNumber}"