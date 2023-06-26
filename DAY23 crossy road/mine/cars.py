from turtle import Turtle
import random
COLORS = ['red','orange','yellow','blue','gold','maroon','violet','magenta','purple','skyblue','cyan','turquoise','lightgreen','brown','grey']
STARTING_SPEED = 10

class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_SPEED

    def random_spawn(self):
        random_num = random.randint(1,6)
        if random_num == 3:
            new_car = Turtle(shape='square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.pu()
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=10

            