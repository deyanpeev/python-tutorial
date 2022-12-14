from Laptop import Laptop
from Smartphone import Smartphone
from GamingLaptop import GamingLaptop

def main():
    print('starting main')
    bad_laptop = Laptop(2.4, 16, 512, 0.1)
    glaptop = GamingLaptop(4, 16, 1024)
    sp = Smartphone(1, 2, 8, 'A1', '0883')

    bad_laptop.startPlayingGames('CS')
    glaptop.startPlayingGames('CS')
    sp.makePhoneCall("testing")
    
    print(bad_laptop)

if __name__ == "__main__":
    main()