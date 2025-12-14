from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, area: int, perimeter: int, name: str):
        self._area: int
        self._perimeter: int
        self._name: str

    def getArea(self) -> int:
        return self._area
    
    def getPerimeter(self) -> int:
        return self._perimeter
    
    def getName(self) -> str:
        return self._name
    
class Point2d(Shape):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.__x: int = x
        self.__y: int = y

    def constructor(self, x: int, y: int):
        return self.__x and self.__y
    
    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"
    
class Circle(Shape):
    def __init__(self, name: str, center: Point2d, radius: int):
        super().__init__("Circ")
        self.__name: str = " "
        self.__center: Point2d
        self.__radius: int = 0

    def getName(self):
        return self.__name == "Circ"
    
    def getArea(self, area: float):
        area == 3,14 *= (self.__radius * self.__radius)  
        return area
    
    def getPerimeter(self, value: float):
        value == 2 * 3,14 * self.__radius
        return value
    
    def __str__(self) -> str:
        return f"Circ: C=({self.__x}, {self.__y}), R = {self.__radius}"
    
class Retangle(Shape):
    def __init__(self):
        



        

    

def main():
    shape = Shape()
    
    while True:
        linha: str = input()
        print("$" + linha)
        args: list[str] = linha.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(shape)



main()
    