from planetarium import Planetarium

p = Planetarium()

planetChoice = '-1'

while(planetChoice != '0'):
    planetChoice = str(input("Which planet (0 to quit)? "))
    p.printOne(planetChoice)
    
