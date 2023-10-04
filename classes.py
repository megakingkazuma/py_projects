# trying to learn classes in python, check google for syntax in case you forget

class Person:
    # Attributes i guess? for all the instances of this class
    species = "human"

    # you need to put this in making a class, will take values depending on each instances this class is called
    def __init__(self, name, age, gender): # dont forget to add "self" inside the brackets
        self.name = name
        self.age = age
        self.gender = gender

    # this is a function within the class. note that species = "human " will be inherited by all instances of the object we made using the class named Person because we set it up on top and not within a function
    def introduce_self(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am {self.gender}. I am a {self.species} Nice to meet you!")

# created an instance of the class named Person and set the values of name, age, gender
person1 = Person("Josh", 29, "Male")

# called the function introduce_self from the object person1 from the class Person, maybe
person1.introduce_self()