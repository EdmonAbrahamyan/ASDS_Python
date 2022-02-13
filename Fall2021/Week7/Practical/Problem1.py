class Circle:
    def __init__(self, radius:float, color:str):
        self.radius = radius
        self.color = color

    def getDesc(self):
        print(f"A {self.color} circle with radius {self.radius}")

circle = Circle(1.5, "black")
circle.getDesc()