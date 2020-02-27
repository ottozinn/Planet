class Planet(object):
    
    def __init__(self, name, mass, temp, color):
        self.name = name
        self.mass = mass
        self.temp = temp
        self.color = color

    def __str__(self):
        return f"Name: {self.name}, {self.mass}, {self.temp}, {self.color}"
    
    
    
