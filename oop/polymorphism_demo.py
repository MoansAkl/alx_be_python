# polymorphism_demo.py

import math

# Base class for all shapes
class Shape:
    def area(self):
        """Base method for calculating area. To be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area method.")

# Derived class for rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of a rectangle."""
        return self.length * self.width

# Derived class for circles
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the Circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
