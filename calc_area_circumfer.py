import os
from sys import platform

def clean_screen():
    if platform in ["linux", "linux2", "darwin"]:
        os.system("clear")

    elif platform == "win32":
        os.system("cls")

clean_screen()


class Circle:

    pi = 3.14

    def __init__(self, radius):
        self.circle_radius = radius

    def __str__(self):
        return f'your radius cricle : {self.circle_radius}'


    def calc_diameter(self):
        return f'diameter: {self.circle_radius * 2}'

    
    def claculate_area_circle(self):
        return f'area circle: {(self.circle_radius ** 2) * Circle.pi}'

    def calculate_circumference_circle(self):
        return f'circumference circle: {self.circle_radius * (Circle.pi * 2)}'

circle1 = Circle(10)

print(circle1.calc_diameter())

print(circle1.claculate_area_circle())

print(circle1.calculate_circumference_circle())