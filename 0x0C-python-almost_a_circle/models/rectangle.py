#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    """class rectangle body"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width(int):
            height(int):
            x(int):
            y(int):
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves the current width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value(int): value must be an integer
        Raises:
            TypeError
            ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the current height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value(int):
        Raises:
            TypeError
            ValueError
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the current x value of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the class rectangle"""
        return (self.width * self.height)

    def display(self):
        """print and display the # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return;

        [print("") for a in range(self.y)]
        for q in range(self.height):
            [print(" ", end="") for b in range(self.x)]
            [print("#", end="") for z in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Assigning each argument attribute to its argument number"""
        if args and len(args) != 0:
            for k, m in enumerate(args):
                if k == 0:
                    self.id = m
                elif k == 1:
                    self.width = m
                elif k == 2:
                    self.height = m
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
                    else:
                        self.y = n

    def to_dictionary(self):
        """return the dictionary form the attribute of each instance"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            })

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                      self.width, self.height))
