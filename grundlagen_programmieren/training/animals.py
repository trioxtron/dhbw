import random 

class StaticAnimal():
    def __init__(self):
        self.aggresiveness = random.randint(0,10)
        self.cuteness = random.randint(0,10)
        self.hair_length = random.randint(0,10)

    @staticmethod 
    def produce_offspring(a, b):
        c = StaticAnimal()
        c.aggresiveness = (a.aggresiveness + b.aggresiveness) / 2
        c.cuteness = (a.cuteness + b.cuteness) / 2
        c.hair_length = (a.hair_length + b.hair_length) / 2
        return c

    def __str__(self):
        return f"Aggresiveness: {self.aggresiveness}, Cuteness: {self.cuteness}, Hair Length: {self.hair_length}"

a = StaticAnimal()
b = StaticAnimal()

print(a)
print(b)

c = StaticAnimal.produce_offspring(a, b)
print(c)

print("--------------------------------------------------")

class Animal():
    def __init__(self, age):
        self.__age = age
        self.aggresiveness = random.randint(0,10)
        self.cuteness = random.randint(0,10)
        self.hair_length = random.randint(0,10)

    def produce_offspring(self, b):
        c = Animal(0)
        c.aggresiveness = (self.aggresiveness + b.aggresiveness) / 2
        c.cuteness = (self.cuteness + b.cuteness) / 2
        c.hair_length = (self.hair_length + b.hair_length) / 2
        return c

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        print(f"Setting age from {self.__age} to {age}")
        self.__age = age

    def __str__(self):
        return f"Aggresiveness: {self.aggresiveness}, Cuteness: {self.cuteness}, Hair Length: {self.hair_length}"

if __name__ == "__main__":
    a = Animal(5)
    b = Animal(7)

    try:
        print(a.age)
        a.age = 100
        print(a.age)
    except:
        print("Age is a private variable")

    
    print(a)
    print(b)

    c = Animal.produce_offspring(a, b)
    print(c)
