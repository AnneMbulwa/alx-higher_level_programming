#!/usr/bin/python3
"""creating a class rectangle"""


class Rectangle:
    """class body
    Attributes:
       number_of_instances(int): number of instances
       print_symbol(char): prints the symbol # 
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width(int): new width
            height(int): new height
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves current width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the current height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the current area of rectagle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print() and str() should print the rectangle with the character #:"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for a in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if a != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Returns the string representation of the Rectangle so to
        create a new instance using eval()"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """Print the message Bye rectangle...
        when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
