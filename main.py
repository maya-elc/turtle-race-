import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70,-40,-10 ,20,50,80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                the_result1 = screen.textinput(title="Result!",prompt=f"You've won! the {winning_color}Turtle is the winner!")
            else:
                the_result2 = screen.textinput(title="Result!", prompt=f"You've lost! the {winning_color}Turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()