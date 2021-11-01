class Computer:
    def __init__(self, Storage, Memory, Screen_Inch, Speakers, Ports, Battery_Life):
        self.Storage = Storage
        self.Memory = Memory
        self.Screen_Inch = Screen_Inch
        self.Speakers = Speakers
        self.Ports = Ports
        self.Battery_Life = Battery_Life

    def playGame(self):
        print("Now Playing: Beat Saber")

Asus = Computer('2TB', '32GB', '27"', 'AudioTechnica', '12', 'Infinite')
print(Asus.Storage)
print(Asus.Memory)
print(Asus.Screen_Inch)
print(Asus.Speakers)
print(Asus.Ports)
print(Asus.Battery_Life)
Asus.playGame()
print(" ")

class Laptop(Computer):
    def __init__(self, Storage, Memory, Screen_Inch, Speakers, Ports, Battery_Life):
        Computer.__init__(self, Storage, Memory, Screen_Inch, Speakers, Ports, Battery_Life)

Alienware = Computer('1TB', '16GB', '15"', 'Harmon_Kardon', '7', '16')
print(Alienware.Storage)
print(Alienware.Memory)
print(Alienware.Screen_Inch)
print(Alienware.Speakers)
print(Alienware.Ports)
print(Alienware.Battery_Life)
Alienware.playGame()
print(" ")