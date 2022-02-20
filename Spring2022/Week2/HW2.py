from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty, ABCMeta
from typing import Any
import copy
import math


class Builder(ABC):

    @abstractmethod
    def create_id(self, _id):
        pass

    @abstractmethod
    def create_balance(self, _balance):
        pass

    def create_rate(self, _rate):
        pass


class BusinessAccount(Builder):

    def __init__(self):
        self.account = BankAccount()

    def create_id(self, _id):
        self.account.add(_id)

    def create_balance(self, _balance):
        self.account.add(_balance)

    def create_rate(self, _rate):
        self.account.add(_rate)


class PersonalAccount(Builder):

    def __init__(self):
        self.account = BankAccount()

    def create_id(self, _id):
        self.account.add(_id)

    def create_balance(self, _balance):
        self.account.add(_balance)


class BankAccount:

    def __init__(self):
        self.description = []

    def add(self, desc: Any):
        self.description.append(desc)

    def describe(self):
        print(f"Bank account description: {', '.join(self.description)}", end="")


builder = BusinessAccount()

print("Custom account1: ")

builder.create_id('1504 2855 8745 9652')
builder.create_balance('5000000')
builder.create_rate('1.5')
builder.account.describe()

builder = PersonalAccount()

print("\nCustom account2: ")

builder.create_id('1504 0052 8745 9652')
builder.create_balance('145000')
builder.account.describe()


class Shape(metaclass=ABCMeta):

    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Circle(Shape):

    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def draw(self):
        return 'I can draw a circle'

    def calc_area(self):
        return math.pi * self.radius * self.radius


class Square(Shape):

    def __init__(self, side: float):
        super().__init__()
        self.side = side

    def draw(self):
        return 'I can draw a square'

    def calc_area(self):
        return self.side * self.side


class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        super().__init__()
        self.length = length
        self.width = width

    def draw(self):
        return 'I can draw a rectangle'

    def calc_area(self):
        return self.width * self.length


# cache class
class Shape_Cache:
    cache = {}

    @staticmethod
    def get_shape(shape_id):
        shape = Shape_Cache.cache.get(shape_id, None)
        return shape.clone()

    @staticmethod
    def load():
        circle = Circle(radius=2)
        circle.set_id("1")
        Shape_Cache.cache[circle.get_id()] = circle

        square = Square(side=4)
        square.set_id("2")
        Shape_Cache.cache[square.get_id()] = square

        rectangle = Rectangle(length=3, width=5)
        rectangle.set_id("3")
        Shape_Cache.cache[rectangle.get_id()] = rectangle


Shape_Cache.load()

circle = Shape_Cache.get_shape("1")
print(circle.calc_area())

square = Shape_Cache.get_shape("2")
print(square.calc_area())

rectangle = Shape_Cache.get_shape("3")
print(rectangle.calc_area())

circle_2 = Shape_Cache.get_shape("1")
circle_2.radius = 4
circle_2.calc_area()
