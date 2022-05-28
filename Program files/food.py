# we will create food for the snake and that food will change its location once the turtle touches it

from turtle import Turtle
import random


class Food(Turtle):  # Class inheritance concept used...class Food will inherit from class Turtle

    def __init__(self):  # note we ever we create an object of the class first of all this __init__() fun is called
        super().__init__()   # Now Food class has inherited from Turtle class
        self.shape("circle")  # see after inheritance method of Turtle class is used in the Food class
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # By default, turtle size is 20*20 but this will make it 10*10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)  # note we have taken the screen 600 * 600...ie it goes from -300 to 300
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)  # Now our food will go to a random location on the screen




