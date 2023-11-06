0x0A. Python - Inheritance
inheritance allows to define a class that inherits all the methods and properties from another class
.Parent/Base class - class inherited from
.Child/Derived class - class that inherits from another class

Benfits of inheritance
1.represents the real world
2.provides the reusabilty of code
3.transitive in nature
4.offers a simple, understable model structure
5.less development and maintainance expenses

syntax:
a) Parent/Base class
    class baseclass():
        {body}

b) Derived/Child class
    class deeivedclass(baseclass):
        {body}

Types of inheritance.
1. single inheritance - child inherits from only one parent class
2. multiple inheritance - child class inherits from multiple parent classes
3. multilevel inheritance - we have a child and grandchild relationship
4. hierarchical inheritance - more than one derived class can be created from single base
5. hybrid inheritance - combines more than one form of inheritance

.Built-in functions
...> isinstance() --> checks the type of an object
syntax::
        isinstance(object_name, class_name)
...> issubclass() --> checks whether a specific class is the child class of another class
syntax::
    issubclass(childclass_name, parentclass_name)

*overriding method -- means redefining a method in the subclass when it is already been defined in some other class.
method in subclass would be overriden if there exits another method with the same name, same parameters and same set in superclass.
we cannot override methods in private class methods*
