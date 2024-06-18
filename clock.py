import turtle
import time

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

        # Create the turtle object
        self.t = turtle.Turtle()
        self.t.speed(0)  # Set drawing speed to maximum
        self.t.hideturtle()  # Hide the turtle

        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=600) 
        self.screen.bgcolor("white") 
        self.screen.tracer(0)

    def draw_clock_face(self):
 
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.circle(100)

 
        for i in range(12):
            self.t.penup()
            self.t.goto(80, 0)
            self.t.pendown()
            self.t.forward(15)
            self.t.right(30)

    def draw_hands(self):
   
        hour_angle = (self.hour + self.minute / 60) * 30
        self.t.penup()
        self.t.goto(0, 0)
        self.t.setheading(hour_angle)
        self.t.pendown()
        self.t.forward(70)

        minute_angle = self.minute * 6
        self.t.penup()
        self.t.goto(0, 0)
        self.t.setheading(minute_angle)
        self.t.pendown()
        self.t.forward(100)

        second_angle = self.second * 6
        self.t.penup()
        self.t.goto(0, 0)
        self.t.setheading(second_angle)
        self.t.pendown()
        self.t.forward(130)

    def update_clock(self):

        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1

        self.screen.clear()

        self.draw_clock_face()
        self.draw_hands()

        self.screen.update()

    def run_clock(self):
        while True:
            self.update_clock()
            time.sleep(1)
clock = Clock(10, 20, 30)
clock.run_clock()
