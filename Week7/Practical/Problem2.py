class Car:
    def __init__(self, model:str, color:str, max_speed:int):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def compareCar(self, car2):
        if self.max_speed > car2.max_speed:
            return "car1 is better than car2"
        else:
            return "car2 is better than car1"


car1 = Car("Mercedes-benz", "black", 200)
car2 = Car("BMW", "gray", 180)