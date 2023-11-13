#!/usr/bin/python3
"""create a xlass square tha inherits from class rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square body.
    Args:
    Call the super class with id, x, y, width and height -
    this super call will use the logic of the __init__ of the Rectangle class
    The width and height must be assigned to the value of size
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """width ad height should be aasigned to the same value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            for k, m in enumerate(args):
                if k == 0:
                    self.id = m
                elif k == 1:
                    self.width = m
                elif k == 2:                                                                            self.height = m
                elif k == 3:
                    self.x = m
                else:
                    self.y = m
        else:
            if kwargs and len(kwargs) != 0:
                for w, n in kwargs.items():
                    if w == "id":
                        if n is None:
                            self.__init__(self.width, self.height,
                                          self.x, self.y)
                        else:
                            self.id = n
                    elif w == "width":
                        self.width = n
                    elif w == "height":
                        self.height = n
                    elif w == "x":
                        self.x = n

    def to_dictionary(self):
        """returns the dictonary representation of class square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))
