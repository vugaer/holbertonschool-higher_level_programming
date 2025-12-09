#!/usr/bin/python3

"""Welcome to Vugar's Tutorial!"""


class Rectangle:

    "ts is so tuff"

    def __init__(self, width=0, height=0):
        self.cf(width, "width")
        self.cf(height, "height")
        self.__width = width
        self.__height = height

    def cf(self, smth, wtf):
        if type(smth) is not int:
            raise TypeError('{} must be an integer'.format(wtf))
        if smth < 0:
            raise ValueError('{} must be >= 0'.format(wtf))
        else:
            return smth

    def getWidth(self):
        return self.__width

    def setWidth(self, value):
        self.cf(value, "width")
        self.__width = value

    def getHeight(self):
        return self.__height

    def setHeight(self, value):
        self.cf(value, "height")
        self.__height = value

    width = property(getWidth, setWidth)
    height = property(getHeight, setHeight)

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''
        else:
            for i in range(self.__height):
                print('#' * self.__width)

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'
