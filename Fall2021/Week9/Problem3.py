import time

def TimeChecking(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        return f"working time of Greeting function {time.time() - start_time}"
    return wrapper

class Person:

    def __init__(self, name: str, last_name: str, age: int, gender: str, student: bool, password: str):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password

    @TimeChecking
    def Greeting(self, second_person):
        print(f"Welcome dear {second_person.name}")

    def Goodbye(self):
        print("Goddbye everyone!")

    def Favourite_num(self, num1: int):
        return f"My favourite number is {num1}"

    def Read_file(self, filename: str):
        try:
            f = open(f"{filename}.txt", "r")
            return f.read()
        except FileNotFoundError as e:
            print(e)

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

