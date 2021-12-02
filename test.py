'''class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, age):
        self.age = age
    def set_name(self, name):
        self.name = name
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def __init__(self, name, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.set_name(name)
        self.parent1 = parent1
        self.parent2 = parent2
    def get_parents(self):
        return str(self.parent1) + "," + str(self.parent2)
    def set_parents(self, parent1=None, parent2=None):
        if self.parent1 is None:
            self.parent1 = parent1
        if self.parent2 is None:
            self.parent2 = parent2
    def speak(self):
        print("meow")
    def __str__(self):
        return "Cat: "+str(self.name)+": "+str(self.age)

max = Cat("Max", "7")
print(max)

max.set_parents("Moritz", "Lisa")
print(max.get_parents())'''

def product(a, b, c=1):
    return a * b * c

print(product(5, 10))

