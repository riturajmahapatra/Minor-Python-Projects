import turtle
import time
import random

WIDTH, HEIGHT = 500, 550
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def number_of_turtles():
    while True:
        racers = input("Enter the number of racers between (2-10) to race: ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is invalid. Try a numeric value between (2-10).')    
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10.')

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing 1.0')
    return screen  #  Return screen object

def create_turtles(colors_turtles):
    turtles = []
    spacing_X = WIDTH // (len(colors_turtles) + 1)
    for i, color in enumerate(colors_turtles):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.setheading(90)  # turtles faces up
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_X, -HEIGHT // 2 + 40)  # adjusted starting position at the bottom with - height and difference between turtles 
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors_turtles):  #  Pass colors_turtles to the main race
    turtles = create_turtles(colors_turtles)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)  # Move randomly between 1-20 pixels
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 25: # y height at end set to the -25 from top
                return colors_turtles[turtles.index(racer)]

racers = number_of_turtles()
screen = init_turtle()  #Store the screen object

shuffled_colors = COLORS[:]  # shuffled copy created 
random.shuffle(shuffled_colors)
colors_turtles = shuffled_colors[:racers]

winning_turtle = race(colors_turtles)
print(f'The Race was won by {winning_turtle}')

turtle.done()  #Keep the turtle window open

