class Shape:
    def __init__(self):
        pass
    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def compute_area(self):
        return self.width * self.height
    
    def compute_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def compute_area(self):
        return self.side**2
    
    def compute_perimeter(self):
        return self.side * 4
    
shape1 = Rectangle(8,4)
shape2 = Square(4)

print("Rectangle area is: ", shape1.compute_area())
print("Rectangle perimeter is: ", shape1.compute_perimeter())
print("\nSquare area is: ", shape2.compute_area())
print("Square perimeter is ", shape2.compute_perimeter())