class Person:
    species = "human"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce_self(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am {self.gender}. I am a {self.species} Nice to meet you!")