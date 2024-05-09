class Pet:
    def __init__(self, name, animal, breed, age):
        self.name = name
        self.animal = animal
        self.breed = breed
        self.age = age

    def speak(self):
        if self.animal == "Dog":
            return f"{self.name} is barking!!!"
        elif self.animal == "Cat":
            return f"{self.name} is meowing!!!"
        else:
            return f"{self.name} is SPEAKING!!!"
    
    @classmethod
    def from_string(cls, emp_str):
        name, animal, breed, age = emp_str.split("-")
        return cls(name, animal, breed, age)

new_pet = Pet("Oli", "Dog", "Maltese", 4)
new_pet2 = Pet.from_string("Monkey-Dog-Doberman-5")
