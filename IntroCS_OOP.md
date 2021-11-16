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
- **What are attributes?**
  - Data that **belongs** to the class
  
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
- **Use self as the 1st argument in method definition**

```python
class Gift():
    
    def pack (self, packer):
        print("This gift is packed by " + packer)
```

- Ignore self when calling method on an object (Python takes care of that for you)

```python
>>> gift_1 = Gift()
>>> gift_1.pack("Nele")
```
```
This gift is packed by Nele.
```

## Similar to working with structs we need a special syntax to properly implement classes.
- Use special method `__init__` to initialize data attributes