from turtle import Turtle, Screen
import random

# Screen
screen = Screen()
screen.setup(width=600)
ask_user = screen.textinput(title="Turtle Race", prompt="Choose a color of your choice? \n")
colors = ["red", "orange", "purple", "green", "yellow", "blue"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Font constants:
ALIGNMENT = "Right"
FONT = ("Courier", 15, "bold")

# To make turtle bodies:
for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x=-230, y=y_position[i])
    all_turtles.append(timmy)

# Get the move:
game_on = False
while not game_on:
    for timmy in all_turtles:
        distance = timmy.forward(random.randint(1, 20))

        if timmy.xcor() > 230:
            game_on = True
            winning_color = timmy.pencolor()
            if ask_user == winning_color:
                win = f"You won, the color: {winning_color}"
                timmy.write(win, align=ALIGNMENT, font=FONT)
            else:
                lose = f"You lose, the winning color is {winning_color}"
                timmy.write(lose, align=ALIGNMENT, font=FONT)

screen.exitonclick()
