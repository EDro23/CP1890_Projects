from dataclasses import dataclass

@dataclass
class Animal:
    name: str
    species: str

    def speak(self):
        return f"I am a {self.species}, "

@dataclass
class Dog(Animal):
    breed: str

    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} Bork Bork"

@dataclass
class Cat(Animal):
    color: str

    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} Meeeaaoww"

dog = Dog(name="Max", species="Dog", breed="Boxer")
cat = Cat(name="Buddy", species="Cat", color="Orange")

print("Dog:")
print(f"Name: {dog.name}")
print(f"Species: {dog.species}")
print(f"Breed: {dog.breed}")
print("Sound:", end=" ")
print(dog.speak())  # Call the speak method using parentheses

print()

print("Cat:")
print(f"Name: {cat.name}")
print(f"Species: {cat.species}")
print(f"Color: {cat.color}")  # Print cat's color, not breed
print("Sound:", end=" ")
print(cat.speak())  # Call the speak method using parentheses