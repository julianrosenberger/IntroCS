# Table of Contents
1. [Introduction](#introduction)
2. [Object-oriented programming](#OOP)
    1. [Objects](#everything-in-python-is-an-object)
    2. [Classes](#in-oop-classes-are-the-blueprints-for-objects)
    3. [Encapsulation](#through-encapsulation-we-can-easily-work-with-objects-within-objects)
    4. [Print representation of objects](#in-procedural-programming-we-used-print-statements-to-interact-with-a-program-objects-cannot-be-printed-that-easily)
    5. [Getter and setter methods](#instead-of-accessing-data-attributes-by-using-the--notation-its-best-practice-to-write-getter-and-setter-methods)
3. [Information hiding](#by-nature-python-is-not-great-in-information-hiding-though-in-oop-we-have-the-possibility-to-do-so)
4. [Inheritance](#inheritance-provides-a-convenient-mechanism-for-building-groups-of-related-abstractions)
    1. [super()](#super())
    2. [Add and override attributes in subclasses](#add_attributes)
5. [Polymorphism](#inheritance-allows-us-to-modify-methods-in-children-classes-which-is-one-of-the-most-common-forms-of-polymorphism)
    1. [Dynamic typing](#dynamic-typing)
    2. [Operator overloading](#operator-overloading)
    3. [Method overloading](#method-overloading)
    4. [Method overriding](#method-overriding)


# Introduction <a id="introduction"></a>

## Arrays in C have a huge disadvantage.
- All values stored in an `array` need to be of the same data type

```c
int main (void)
{
    int a[] = {1, 2, 3, 5, 6};
    char word[10] = {'c', 'o', 'd', 'e', '\0'};
}
```

## Lists in Python are more powerful then arrays in C.
- A `list` in Python allows us to store multiple variables of different data types together in one list
- A `dictionary` in Python allows us to store multiple key-value pairs in one data structure

```python
    # gift = ["<content>", <width>, <height>, <color>]

    gift_1 = ["CS50 Rubber Duck", 20.0, 40.0, "green"]
    gift_2 = ["CS50 Stress Ball", 30.0, 20.0, "pink"]
    gift_3 = ["CS50 Sunglasses", 15.0, 10.0, "yellow"]
```

## Data Structures in C allow us to store information in different layouts.
- A `struct` is a collection of variables (can be of different types) under a single name

```c
struct Gift 
{
    char content[50];
    float width;
    float height;
    char color[20];
} gift_1, gift_2, gift_3;

int main (void) 
{
    gift_1.content = "CS50 Rubber Duck";
    gift_1.width = 20.0;
    gift_1.height = 40.0;
    gift_1.color = "green";
    
    gift_2.content = "CS50 Stress Ball";
    gift_2.width = 30.0;
    gift_2.height = 20.0;
    gift_2.color = "pink";

    ...

    return 0;
}
```

# Object-oriented programming <a id="OOP"></a>

## Everything in Python is an object.
- **Every object**
    - has a **type**
    - can **manipulate objects**
    - can **destroy objects**

```python
a = [1, 2, 3, 4, 5]
b = 5
c = "Hello"

print(type(a))
print(type(b))
print(type(c))
```

**Output:**

```
<type 'list'>
<type 'int'>
<type 'str'>
```

## Objects = attributes + methods.

- Python built-in function `dir` allows us to access all attributes and methods of a specific object
- **Objects** are a **data abstraction** that captures
    - an internal representation through **data attributes**
    - an interface for interacting with the object through **methods**

```python
a = [1, 2, 3, 4, 5]
print(dir(a))
```

**Output:**

```
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## In OOP classes are the blueprints for objects.

- `class <name>` starts a class definition
- Code inside `class` is indented
- Use `pass` to create an "empty" class

```python
class Gift():
    # define attributes here
    pass
```

Use `ClassName()` to create an object of class `ClassName`

```python
>>> gift_1 = Gift()
>>> gift_2 = Gift()
```

## Attributes are used specify classes like data structures allowed us to do.

- Let's quickly re-visit the concept of data structures (`struct`) in C

```c
struct Gift 
{
    char content[50];
    float width;
    float height;
    char color[20];
};
```

- Having this in mind, **attributes** allow us to do the **same** with **classes**:
    - Use **constructor** `__init__` to initialize data attributes

```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color
```

## Methods can be easily assigned to Classes and you can work with them as you are used to with functions.

- **method** **definition = function definition** within class
- Use `self` as the **1st argument** in method definition

```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color

    def pack(self, packer):
        print("This gift is packed by " + packer)
```

## Before we use a certain method we need to create an instance of a class (object).

- Data atrributes of an instance are called **instance variables**
- **Ignore** `self` when calling method on an object (Python takes care of that for you)
- `self` is a **placeholder** for particular object used in class definition and is the **first argument of any method**

```python
# create a new object of type Gift and pass in content, width, height and color to __init__
>>> gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")

# use dot operator to access any attribute of gift_1
>>> print(gift_1.color)

# use dot operator to access any method of gift_1
>>> gift_1.pack("Nele")
```

**Output:**

```
This gift is packed by Nele
```
- `gift_1.pack("Nele")` is interpreted as `Gift.pack(gift_1, "Nele")`

```python
# create a new object of type Gift and pass in content, width, height and color to __init__
>>> gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")

# use dot operator to access any method of gift_1
>>> gift_1.pack("Nele")
```
```
This gift is packed by Nele
```

## Now it's time to bring it all together.

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

**Output:**

```
This gift contains a CS50 Rubber Duck and is gifted to David.
```

## Let's re-visit the just learned by having a look at the anatomy of classes.
- **Methods** are function definitions within a class
- Define **data attributes** by assignment
    - Refer to attributes via `self._____`

```python
class MyClass():
    # method definition in class
    # first argument is self
    def my_method1(self, other_arguments...):
        # do things here
    
    def my_method2(self, my_attr):
        # attribute created by assignment 
        self.my_attr = my_attr
        ...
```

- **Constructor** `__init__` is called every time an object is created

```python
class Gift:
    def __init__(self, content):
        self.content = content            # <--- Create the .name attribute and set it to name parameter
        print("The __init__ method was called")

gift_1 = Gift("CS50 Rubber Duck") # <--- __init__ is implicitly called
```

**Output:**

```python
The __init__ method was called
```

## Through encapsulation, we can easily work with objects within objects.
- **Encapsulation** means bundling together **data attributes** and **methods** to operate on them
- This allows us to effectively combine objects

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

## In procedural programming, we used print-statements to interact with a program. Objects cannot be printed that easily.
### Default print representation

- By default, the `print` representation of objects is very uninformative

```python
class Gift():
    ...

gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
print(gift_1)
```

**Output:**

```
<__main__.Gift object at 0x10337ccd0>
```

### Define custom method to print objects
- Using a custom method, allows us to make the `print` representation more informative
- define `show` to print object of class `Gift`

```python
class Gift():
    ...
    def show(self):
        print(self.content, self.width, self.height, self.color)

gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
gift_1.show()
```

**Output:**

```
CS50 Rubber Duck 20.0 40.0 green
```

## Instead of accessing data attributes by using the "`.`" notation, it’s best practice to write getter and setter methods.

- Here we define `get_width` and `set_width` to access and change the width of an object of class `Gift`
- 
```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        ...
    def get_width(self):
        return self.width
    def set_width(self, width):
        self.width = width
```

## By nature Python is not great in information hiding. Though in OOP we have the possibility to do so.
- **Private:** indicated by a double underscore `self.__attribute`
    - Private attributes **cannot** be accessed from outside a class.
- **Protected:** Indicated by a single underscore `self._attribute`
    - Protected attributes **should not** be accessed from outside a class, other than subclasses
    - Note that Python only sets this as **convention**, so it’s more an indicator
- **Public:** Indicated by the absence of an underscore: `self.attribute`
    - Public attributes are **always** **accessible**

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
print(gift_1.get_content())
```

**Output:**

```
20.0
40.0
20.0
CS50 Rubber Duck
```

# Core Concepts of OOP
## Inheritance provides a convenient mechanism for building groups of related abstractions.

- Remember that **classes** are used to implement data abstractions
- **Inheritance** allows you to create a type hierarchy in which each type inherits types from above it in the hierarchy
- The class `object` is at the top of hierarchy
  This makes sense, since in Python everything that exists at runtime is an object
  Because Animal inherits all the properties of objects, programs can bind a variable to an `Animal`, append an `Animal` to a `list`, etc.

### Parent class
- Everything is an `object` in Python, so `Animal` inherits all the properties of objects
- class `object` implements basic operations in Python, like binding variables, etc.

```python
class Animal():
  def __init__(self, age, name):
    self.age = age
    self.name = name
  def make_noise(self):
    print("I don't know, which noise I make")
```

### Children classes
- **Parent class** is `Animal`
    - Call Animal **constructor**
    - Call Animal’s `set_name` method
    - **Add** new data attribute `color` to Cat which is a string containing the cat’s color
- **Override** Animal’s `make_noise` method

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

### <a id="super()"></a> You might have noticed that we called the constructor of our superclass by using `super().__init__()` instead of `Animal.__init__()`.
- In a class hierarchy with single inheritance, super can be used to refer to parent class without naming it explicitly
- This makes the code more maintainable
- `self` is not needed when working with `super()`
- `super().__init__(age, name)` equals to `Animal.__init__(self, age, name)`

```python
class Cat(Animal):
  def __init__(self, age, name, color):
    super().__init__(age, name)
    self.color = color
  def make_noise(self):
    print("Meow")
```


### <a id="add_attributes"></a> In addition to what subclasses inherit they can add new attributes and override attributes of superclasses.
**Add new attributes**
- Cat added the instance variables `color` and `catID`
- The **instance** **variable** `self.catID` is initialized using a **class** **variable** `tag`, that belongs to the class `Cat` rather than to instances of the class

**Override attributes of superclass**
- For example, `Cat` has overridden `__init__` and `make_noise`


```python
class Cat(Animal):

    tag = 0

    def __init__(self, age, name, color):
        super().__init__(age, name)
        self.color = color
        self.catID = Cat.tag
        Cat.tag += 1
    def make_noise(self):
        print("Meow")
```

## Inheritance allows us to modify methods in children classes, which is one of the most common forms of polymorphism.
- Use of a **single type entity** (method, operator or object) to represent **different** **types** in different scenarios

### Dynamic typing
- No need to declare variable during runtime

```python
## variable is assigned to a string
a = "hello"
print(type(a))

## variable is assigned to an integer
a = 5
print(type(a))
```

### Operator overloading
- Python objects allow us to extend the meaning of default operators, e.g. '`+`' or '`*`'

```python
# Python program to show use of
# + operator for different purposes.
print(1 + 2)

# concatenate two strings
print("Intro" + "CS")

# Product two numbers
print(3 * 4)

# Repeat the String
print("IntroCS" * 4)
```

**Output:**

```
str
int
```

### Method overloading
- In Python, Method overloading does not work as in other languages like Java or C++/#
- However, we can set parameters to default values:

```python
def product(a, b, c=1):
    return a * b * c

# without defining c=1 as default parameter, this line would throw an error
print(product(5, 10))
```

### Method overriding
- Method overriding is an ability of every OOP programming language that allows subclasses to override methods of the according superclasses (Inheritance)

```python
class Animal(object):
    def __init__(self):
        self.value = "Inside parent"
    def show(self):
        print(self.value)

class Cat(Animal):
    def __init__(self):
        self.value = "Inside children"
    def show(self):
        print(self.value)
```

**Output:**

```
Inside parent
Inside children
```

### Instead of overriding the show method, we can use the __str__ method to override Python’s default print-statement.
- `str(self.width)`: `__str__`must return a string

```python
class Gift():
    ...
    def __str__(self):
        return 'This gift contains ' + self.content + ' and has a width of ' + str(self.width)

gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
print(gift_1.__str__())
print(gift_1)
```

**Output:**

```
This gift contains CS50 Rubber Duck and has a width of 20.0
This gift contains CS50 Rubber Duck and has a width of 20.0
```

###  Just like `__str__` there are more of those special operators in Python.
- Special methods in OOP allow us to override common methods, which we know already.

```python
__add__(self, other)
__sub__(self, other)
__eq__(self, other)
__lt__(self, other)
__len__(self)
__str__(self)
```

**This maps to:**

```python
self + other
self - other
self == other
self < other
len(self)
print(self)
```