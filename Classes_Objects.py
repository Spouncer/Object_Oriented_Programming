class Solarsystem: # parent class
    number_of_planets = 0

    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    
    def add_map(self, map):
        self.maps.append(map)

    def speak(self):
        print(f"I am {self.name} and my age and size are {self.age} and {self.size}")

class Species(Solarsystem): # child class 1
    def __init__(self, name, age, size, language):
        super().__init__(name, age, size)
        self.languages = [language]
        self.species = []
        Solarsystem.number_of_planets += 1

    def add_species(self, species):
        self.species = self.species.append(species)

    def add_lang(self, language):
        self.languages = self.languages.append(language)

class Planets(Solarsystem): # child class 2
    def __init__(self):
        self.maps = []
        Solarsystem.planet_to_add()
    

    @classmethod
    def planet_to_add(cls):
        cls.number_of_planets += 1

    @staticmethod # doesnt have to be used on an instance
    def average(x, y):
        return (x + y)/2

print(Planets.average(3, 6))

m = Species("maths", 200, 10000, "numbers")
s = Species("science", 300, 100000, "numbers")
p = Species("philosophy", 400, 1000, "words")

milkyway = Solarsystem("milkyway", 14*10**(9), 20*10**9

milkyway.add_map(m)
milkyway.add_map(s)


print(len(m.link))








