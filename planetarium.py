from planet import Planet

class Planetarium(object):
    def __init__(self):
        self.create()                

    def create(self):
        self.planets = []
        self.planets.append(Planet("Earth", '5.97 × 10^24', 14.4, 'blue')) 
        self.planets.append(Planet("Mars", '6.39 × 10^23', -125, 'gray'))
        self.planets.append(Planet("Jupiter", '1.9 × 10^27', -145, 'orange')) 
        self.planets.append(Planet("Venus", '4.867 × 10^24', 462, 'yellow'))
        self.planets.append(Planet("Saturn", '5.683 × 10^26', -178, 'yellow'))
        self.planets.append(Planet("Mercury", '3.285 × 10^23', -173, 'gray'))
        self.planets.append(Planet("Neptune", '1.024 × 10^26', -214, 'blue'))
        self.planets.append(Planet("Uranus", '8.681 × 10^25', 182, 'blue')) 

    def printOne(self, planetChoice):
        length = len(self.planets)
        for i in range(length):
            if(self.planets[i].name == planetChoice):
                print(str(self.planets[i]))
