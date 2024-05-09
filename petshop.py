import random

class Pet:
    def __init__(self, name, animal, breed, age, tame):
        self.name = name
        self.animal = animal
        self.breed = breed
        self.age = age
        self.tame = tame

    def intro(self):
        return f"Hello! I am {self.name}, a {self.age} year old {self.breed} {self.animal}."

    def talking(self):
        if self.tame == True:
            return f"{self.name} the {self.breed} is SPEAKING!!!"
        else:
            return f"{self.name} the {self.breed} is wild!!! {self.name} is going FERAL!!!!!!!!"
    
    def play(self):
        return f"{self.name} the {self.breed} doesn't know how to play with toys :("

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

Oli = Dog("Oli", "Maltese", 4, False)
#Monkey = Pet.from_string(f"Monkey-Dog-Doberman-5-True")
Thumper = Pet("Thumper", "Rabbit", "Lionhead", 2, True)
Barry = Cat("Barry", "British Shorthair", 3, True)
Rocket = Dog("Rocket", "Dachshund", 1, True)

print(Oli.intro() + "\n")

print(Oli.talking())
print(Thumper.talking())
print(Barry.talking())
print(Rocket.talking() + "\n")

print(Oli.play())
print(Thumper.play())
print(Barry.play() + "\n")