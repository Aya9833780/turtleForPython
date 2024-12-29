from turtle import Turtle, Screen
import random
window = Screen()
window.title("turtle game")
window.setup(600,400)
colors = ("red", "blue", "green")
y_position = (-70,0,70)
turtles = []
user_input = window.textinput("Make your bet", "Guess the winner:\nType a color: Red, Blue or green")
for i in range(3):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_position[i])
    turtles.append(new_turtle)
def race():
    race_on = True
    while race_on:
        for turtle in turtles:
            if turtle.xcor() > 280:
                race_on = False
                wining_color = turtle.pencolor()
                result(wining_color)
            else:
                turtle.forward(random.randint(1,5))
def result(winner):
    result_turtle = Turtle()
    result_turtle.hideturtle()
    if winner == user_input:
        window.bgcolor("pink")
        result_turtle.color("white")
        result_turtle.write("you win !", align="center", font=("Arial", 50, "normal"))
    else:
        window.bgcolor("green")
        result_turtle.write("you lose!", align="center", font=("Ariel", 50, "normal"))


race()





window.exitonclick()