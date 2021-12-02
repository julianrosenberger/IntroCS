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

'''def product(a, b, c=1):
    return a * b * c

print(product(5, 10))
'''

'''class Gift():
    def __init__(self, content, width, height):
        self.__content = content
        self._width = width
        self.height = height
    def __get_height(self):
        return self.height
    def _get_width(self):
        return self._width
    def get_content(self):
        return self.__content
    

gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0)

### Data attributes
## AttributeError: 'Gift' object has no attribute '__content
#print(gift_1.__content)
print(gift_1._width)
print(gift_1.height)

### Methods
## AttributeError: 'Gift' object has no attribute '__getHeight'
#print(gift_1.__get_height())
print(gift_1._get_width())
print(gift_1.get_content())'''

class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color


class ChristmasTree():
    def __init__(self, max_gifts):
        self.max_gifts = max_gifts
        self.gifts = []
    def place_gift(self, gift):
        self.gifts.append(gift)
    def remove_gift(self, gift):
        self.gifts.remove(gift)
    def get_contents(self):
        for gift in self.gifts:
            print(gift.content)


def main():
    # Initialize gifts
    gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
    gift_2 = Gift("CS50 Stress Ball", 30.0, 20.0, "pink")
    # Initalize tree
    tree = ChristmasTree(5)
    tree.place_gift(gift_1)
    tree.place_gift(gift_2)
    tree.get_contents()
    tree.remove_gift(gift_2)
    print("After removal:")
    tree.get_contents()


if __name__ == "__main__":
    main()