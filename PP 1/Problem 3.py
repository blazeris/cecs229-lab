class Rectangle:

    def __init__(self):
        self.height = 1
        self.width = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

def printTest(rectangle):
    print("Width: " + str(rectangle.width))
    print("Height: " + str(rectangle.height))
    print("Area: " + str(rectangle.getArea()))
    print("Perimeter: " + str(rectangle.getPerimeter()))

rectangle1 = Rectangle(4, 40)
rectangle2 = Rectangle(3.5, 35.9)


print("Rectangle 1:")
printTest(rectangle1)
print("Rectangle 2:")
printTest(rectangle2)