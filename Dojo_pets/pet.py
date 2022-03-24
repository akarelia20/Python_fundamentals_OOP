class Pet:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks
        self.health= 100  # default value
        self.energy = 100  # default value

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy +=5
        self.health += 10
        return self
    
    # play() - increases the pet's health by 5  
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound  
    def noise(self):
        print(self.sound)
        return self

# bird class inherits from pet class
class Bird(Pet):
    def __init__(self, name, tricks):
        # "super" allows access to parent's methods, 
        super().__init__(name, tricks)
        self.food = "seeds"
        self.energy = 50    # defalut for bird class
        self.health= 90     # defalut for bird class
        self.type= "bird"
        self.sound= "tweet...tweet"
    
    def fly(self):
        self.energy -= 20
        print(f"{self.name}'s energy level is {self.energy} after flying")

    def sleep(self):
        self.energy += 25
        print(f"{self.name} is bird and likes to sleep, new energy level is {self.energy}")


# Dog class inherits from pet class
class Dog(Pet):
    def __init__(self, name, tricks):
        # "super" allows access to parent's methods,
        super().__init__(name, tricks)
        self.food = "dog_food"
        self.energy = 90    # defalut for dog class
        self.health= 90     # defalut for dog class
        self.type= "Dog"
        self.sound= "woof...woof"
    
    def sleep(self):
        self.energy += 10
        print(f"{self.name} is dog and likes to take short naps, new energy level is {self.energy}")

