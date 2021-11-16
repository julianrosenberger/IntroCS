# Recap
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


# Objects

- Everything in Python is an Object

```python
a = [1, 2, 3, 4, 5]
b = 5
c = "Hello"

print(type(a))
print(type(b))
print(type(c))
```
Output:
```
<type 'list'>
<type 'int'>
<type 'str'>
```

## Objects = attributes + methods 

- Python built-in function `dir` allows us to access all attributes and methods of a specific object

```python
a = [1, 2, 3, 4, 5]
print(dir(a))
```
Output:
```
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

# Classes

## In OOP classes are the blueprints for objects.

- `class <name>` starts  a class definition
- Code inside `class` is indented
- Use `pass` to create an "empty" class
  
```python
class Gift():
    # define attributes here
    pass
```

[//]: # "Use `ClassName()` to create an object of class `ClassName`"

```python
>>> gift_1 = Gift()
>>> gift_2 = Gift()
```

## Attributes are used specify classes like data structures allowed us to do.

- Let's quickly re-visit the concept of data structures (`struct`) in C.

```c
struct Gift 
{
    char content[50];
    float width;
    float height;
    char color[20];
};
```

- Having this in mind, attributes allow us to do the same with classes:
- Use special method `__init__` to initialize data attributes
  
```python
class Gift():
    def __init__(self, content, width, height, color):
        self.content = content
        self.width = width
        self.height = height
        self.color = color
```

## Methods can be easily assigned to Classes and you can work with them as you are used with functions.

- method definition = function definition within class
- **Use `self` as the 1st argument in method definition**

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
- Ignore `self` when calling method on an object (Python takes care of that for you)
- `self` is a placeholder for particular object used in class definition and is the first argument of any method

```python
# create a new object of type Gift and pass in content, width, height and color to __init__
>>> gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")

# use dot operator to access any attribute of gift_1
>>> print(gift_1.color)

# use dot operator to access any method of gift_1
>>> gift_1.pack("Nele")
```
Output:
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

## Now it's time to combine everything and bring it all together.

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


def main():
    gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
    gift_1.gift("David")


if __name__ == "__main__":
    main()

```

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
```

```python
>>> gift_1 = Gift("CS50 Rubber Duck", 20.0, 40.0, "green")
>>> gift_1.gift_to("David")
```
```
This gift contains a CS50 Rubber Duck and is gifted to David.
```

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

```python
```