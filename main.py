import turtle
import time
import random
import pygame

WIDTH = 700
HEIGHT = 700
LIGHT_GREY_COLOR = "#D3D3D3"

COLORS = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Grey", "Brown", "Black", "Cyan"]

def screen_maker():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing!")
    screen.bgcolor(LIGHT_GREY_COLOR)

def race(colors):
    turtles = turtle_maker(colors)
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load("car_race.mp3")

    # Play the audio
    pygame.mixer.music.play(-1) 
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
                
            x,y = racer.pos()
            if y >= (HEIGHT//2) -20:
                return colors[turtles.index(racer)]
        
def turtle_maker(colors):
    turtles = []
    spacingx = WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        turtle_ = turtle.Turtle()
        turtle_.shape("turtle")
        turtle_.color(color)
        turtle_.left(90)
        turtle_.penup()
        positionx = ((-WIDTH//2)+(i+1)*spacingx)
        positiony = ((-HEIGHT//2) + 30)
        turtle_.setposition(positionx,positiony)
        turtle_.pendown()
        turtles.append(turtle_)
    return turtles

def get_racers():
    while True:
        racers = input("Enter Number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Racers should be in range (2-10)")
        else:
            print("Invalid Input! Try again")
                
racers = get_racers()

random.shuffle(COLORS)
colors = COLORS[:racers]   

screen = screen_maker()

winner = race(colors)
print(f"The winner is {winner} Turtle!")
pygame.mixer.music.stop()
time.sleep(5)