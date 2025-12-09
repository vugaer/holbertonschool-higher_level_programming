#!/usr/bin/python3

"""Welcome to Vugar's Tutorial!"""


class Rectangle:

    "ts is so tuff"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def getHeight(self):
        return self.__height

    def setHeight(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    width = property(getWidth, setWidth)
    height = property(getHeight, setHeight)
