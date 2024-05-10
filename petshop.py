import random
from time import sleep

class Pet:
    def __init__(self, name, animal, breed, age, tame):
        self.name = name
        self.animal = animal
        self.breed = breed
        self.age = age
        self.tame = tame

    def intro(self):
        return f"\nHello! I am {self.name}, a {self.age} year old {self.breed} {self.animal}."

    def talking(self):
        if self.tame == True:
            return f"{self.name} the {self.breed} is SPEAKING!!!"
        else:
            return f"{self.name} the {self.breed} is wild!!! {self.name} is going FERAL!!!!!!!!"
    
    def play(self):
        return f"{self.name} the {self.breed} doesn't know how to play with toys :(."

    @classmethod
    def from_string(cls, emp_str):
        name, animal, breed, age, tame = emp_str.split("-")
        return cls(name, animal, breed, age, tame)
    
class Dog(Pet):
    def __init__(self, name, breed, age, tame):
        super().__init__(name, "Dog", breed, age, tame)
    
    def talking(self):
        if self.tame == True:
            return f"{self.name} the {self.breed} is barking!!!"
        else:
            return f"{self.name} the {self.breed} is wild!!! {self.name} is GROWLING!!!!!!!!"
        
    def play(self):
        toy_list = ["ball", "frisbee", "stick"]
        num = random.randint(0,2)
        return f"{self.name} the {self.breed} is playing with a {toy_list[num]}."
        
class Cat(Pet):
    def __init__(self, name, breed, age, tame):
        super().__init__(name, "Cat", breed, age, tame)
    
    def talking(self):
        if self.tame == True:
            return f"{self.name} the {self.breed} is meowing!!!"
        else:
            return f"{self.name} the {self.breed} is wild!!! {self.name} is HISSING!!!!!!!!"
    
    def play(self):
        toy_list = ["ball of yarn", "laser pointer", "catnip toy"]
        num = random.randint(0,2)
        return f"{self.name} the {self.breed} is playing with a {toy_list[num]}."

oli = Dog("Oli", "Maltese", 4, False)
thumper = Pet("Thumper", "Rabbit", "Lionhead", 2, True)
barry = Cat("Barry", "British Shorthair", 3, True)
rocket = Dog("Rocket", "Dachshund", 1, True)
pet_list = ["oli", "thumper", "barry", "rocket"]

"""print(Oli.intro() + "\n")

print(Oli.talking())
print(Thumper.talking())
print(Barry.talking())
print(Rocket.talking() + "\n")

print(Oli.play())
print(Thumper.play())
print(Barry.play() + "\n")
"""
print("\n1. Oli\n2. Thumper\n3. Barry\n4. Rocket\n")
sleep(1)
pet_choice = input(f"We have 4 pets today!!! Which pet would you like to see? ---> ")
pet = pet_choice.lower()
while pet not in pet_list:
    pet_choice = (input("Please pick a pet!!! "))
    pet = pet_choice.lower()

"""pet_a = __spec__.Dog(pet)
print(pet.intro() + "\n")

test = oli
print(test.intro() + "\n")
print(type(test))
print(type(pet))"""

if pet == "oli":
    print(oli.intro() + "\n")
    print(oli.talking())
    print(oli.play())
elif pet == "thumper":
    print(thumper.intro() + "\n")
    print(thumper.talking())
    print(thumper.play())
elif pet == "barry":
    print(barry.intro() + "\n")
    print(barry.talking())
    print(barry.play())
elif pet == "rocket":
    print(rocket.intro() + "\n")
    print(rocket.talking())
    print(rocket.play())