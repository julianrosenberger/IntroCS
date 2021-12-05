# Classes
## Introduce a class
```python
class Gift():
    # define attributes here
    pass
```
## Create instances of class
```python
gift_1 = Gift()
gift_2 = Gift()
```
## Data attributes
```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color
```
```python
gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
gift_2 = Gift("CS50 Stress Ball", 30.0, 20.0, "pink")
```
## Methods
```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color

    def pack(self, packer):
        print("This gift is packed by " + packer)

    def gift(self, gifted):
        print(f"This gift contains a {self.content} and is gifted to {gifted}.")
```
## Combine everything
```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color

    def pack(self, packer):
        print("This gift is packed by " + packer)

    def gift_to(self, gifted):
        print(f"This gift contains a {self.content} and is gifted to {gifted}.")


def main():
    gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
    gift_1.gift_to("David")


if __name__ == "__main__":
    main()

```
# Encapsulation & Information hiding
```python
class Gift():
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


def main():
    gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0)

    ## Data attributes
    #print(gift_1.__content)
    print(gift_1._width)
    print(gift_1.height)

    ## Methods
    #print(gift_1.__get_height())
    print(gift_1._get_width())
    print(gift_1.get_content())
```
# Use objects within objects
```python
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
    
```
# Inheritance & Polymorphism
## Parent class
```python
class Animal():
  def __init__(self, age, name):
    self.age = age
    self.name = name
  def make_noise(self):
    print("I don't know, which noise I make")
```
## Children classes
```python
class Cat(Animal):
  def __init__(self, age, name, color):
    super().__init__(age, name)
    self.color = color
  def make_noise(self):
    print("Meow")

class Dog(Animal):
  def __init__(self, age, name, color):
    super().__init__(age, name)
  def make_noise(self):
    print("Wuff")

class Fox(Animal):
  def __init__(self, age, name, color):
    super().__init__(age, name)
```
### Class variables
```python
class Cat(Animal):
    tag = 0

    def __init__(self, age, name):
        super().__init__(age, name)
        self.color = color
        self.catID = Cat.tag
        Cat.tag += 1
    def make_noise(self):
        print("Meow")
```
## Method overriding: `__str__` method
```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color
    def __str__(self):
        return 'This gift contains ' + self.content + ' and has the color ' + self.color 


def main():
    gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
    gift_2 = Gift("CS50 Stress Ball", 30.0, 20.0, "pink")

    print(gift_1)

if __name__ == "__main__":
    main()
```