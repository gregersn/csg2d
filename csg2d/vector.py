from __future__ import annotations
import math

class Vector():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"<Vector({self.x}, {self.y})>"

    def clone(self) -> Vector:
        return Vector(self.x, self.y)
    
    def negated(self) -> Vector:
        return Vector(-self.x, -self.y)
    
    def plus(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)
    
    def minus(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)
    
    def times(self, a: float) -> Vector:
        return Vector(self.x * a, self.y * a)
    
    def divide_by(self, a: float) -> Vector:
        return Vector(self.x / a, self.y / a)
    
    def dot(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y
    
    def lerp(self, other: Vector, t: float) -> Vector:
        return self.plus(other.minus(self).times(t))
    
    def length(self) -> float:
        return math.sqrt(self.dot(self))
    
    def unit(self) -> Vector:
        return self.divide_by(self.length())
    
    def squared_length_to(self, other: Vector) -> float:
        return (self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y)

    def __eq__(self, o: Vector) -> bool:
        return self.x == o.x and self.y == o.y
