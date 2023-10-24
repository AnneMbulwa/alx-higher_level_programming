/*0x06. Python - Classes and Objects*/
A class creates a new type where objects are instances of the class.

Objects can store data using ordinary variables that belong to the object.
Variables that belong to an object or class are referred to as fields.
Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class.
This terminology is important because it helps us to differentiate between functions and
variables which are independent and those which belong to a class or object.
Collectively, the fields and methods can be referred to as the attributes of that class.

Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself.
They are called instance variables and class variables respectively.
A class is created using the class keyword. The fields and methods of the class are listed in an indented block

example
class Person:
    pass  # An empty block

p = Person()
print(p)

methods
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()

/*the __init__ function*/
the __init__ method is run as soon as an object of a class is instantiated
 (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object)
 you want to do with your object.

example
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()

