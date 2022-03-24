# import all from pet
from pet import *

class Ninja:
    list_pet= []
    def __init__(self, first_name, last_name, pet):
        self.first_name = first_name
        self.last_name = last_name
        Ninja.list_pet.append(pet)
        self.pet = pet
        
    def walk(self):
        self.pet.play()
        if type(self.pet) == Dog: # only applies if pet is dog
            print(f"{self.pet.name} like to go for walk")
        return self

    def feed(self):
        self.pet.eat()
        print(f"feeding {self.pet.name} {self.pet.food}")
        return self

    def bathe(self):
        self.pet.noise()
        return self


charlie = Bird("Charlie", "Can fly 2x faster")
snuggle = Dog("Snuggle", "Can snuggle") 
rayno = Ninja( "Rayno", "Jones", charlie)
mary= Ninja("Mary", "Brooks", snuggle)


# rayno
rayno.pet.fly()
rayno.bathe().feed()
rayno.pet.sleep()

# mary
mary.walk()
mary.bathe().feed()
mary.pet.sleep()


"""
OUTPUT:
Charlie's energy level is 30 after flying
tweet...tweet
feeding Charlie seeds
Charlie is bird and likes to sleep, new energy level is 60
Snuggle like to go for walk
woof...woof
feeding Snuggle dog_food
Snuggle is dog and likes to take short naps, new energy level is 105
"""