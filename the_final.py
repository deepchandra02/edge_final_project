import turtle
import time
from datetime import datetime
import random
import tkinter
import pygame
from pygame import mixer
from tkinter import*
pygame.mixer.init()
mixer.music.load("Crazy frog soundtrack.mp3")
pygame.mixer.music.play(-1)

real_val = 0.1


def new_game():
    session = real_val
    delay = real_val
    
    # Score
    score = 0
    high_score = 0
    
    
    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0) # Turns off the screen updates
    
    
    #gaming boundaries
    
    g1 = turtle.Turtle()
    g1.shape("square")
    g1.color("black")
    g1.penup()
    g1.goto(320,320)
    g1.direction = "stop"
    
    g2 = turtle.Turtle()
    g2.shape("square")
    g2.color("black")
    g2.penup()
    g2.goto(-320,320)
    g2.direction = "stop"
    
    g3 = turtle.Turtle()
    g3.shape("square")
    g3.color("black")
    g3.penup()
    g3.goto(320,-320)
    g3.direction = "stop"
    
    g4 = turtle.Turtle()
    g4.shape("square")
    g4.color("black")
    g4.penup()
    g4.goto(-320,-320)
    g4.direction = "stop"
    
    
    
    
    # Snake head
    
    
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("grey")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
    
    eye1 = turtle.Turtle()
    eye1.shape("square")
    eye1.color("white")
    eye1.shapesize(0.2)
    eye1.penup()
    eye1.goto(-5,5)
    eye1.direction = "stop"
    
    
    eye2 = turtle.Turtle()
    eye2.shape("square")
    eye2.color("white")
    eye2.shapesize(0.2)
    eye2.penup()
    eye2.goto(5,5)
    eye2.direction = "stop"
    
    b1= turtle.Turtle()
    b1.shape("square")
    b1.color("black")
    b1.shapesize(0.1)
    b1.penup()
    b1.goto(-5,5)
    b1.direction = "stop"
    
    
    b2 = turtle.Turtle()
    b2.shape("square")
    b2.color("black")
    b2.shapesize(0.1)
    b2.penup()
    b2.goto(5,5)
    b2.direction = "stop"
    
    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)
    
    segments = []
    
    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
    
    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"
    
            eye1.direction = "up"
            eye2.direction = "up"
            b1.direction = "up"
            b2.direction = "up"
    
    def go_down():
        if head.direction != "up":
            head.direction = "down"
    
            eye1.direction = "down"
            eye2.direction = "down"
            b1.direction = "down"
            b2.direction = "down"
    
    def go_left():
        if head.direction != "right":
            head.direction = "left"
    
            eye1.direction = "left"
            eye2.direction = "left"
            b1.direction = "left"
            b2.direction = "left"
    
    def go_right():
        if head.direction != "left":
            head.direction = "right"
    
            eye1.direction = "right"
            eye2.direction = "right"
            b1.direction = "right"
            b2.direction = "right"
    
    def move():
        if head.direction == "up":
    
            y = head.ycor()
            y2 = eye1.ycor()
            y3 = eye2.ycor()
            y4 = b1.ycor()
            y5 = b2.ycor()
    
            head.sety(y + 20)
            eye1.sety(y2 + 20)
            eye2.sety(y3 + 20)
            b1.sety(y4 + 20)
            b2.sety(y5 + 20)
    
    
    
    
    
        if head.direction == "down":
    
            y = head.ycor()
            y2 = eye1.ycor()
            y3 = eye2.ycor()
            y4 = b1.ycor()
            y5 = b2.ycor()
    
            head.sety(y - 20)
            eye1.sety(y2 - 20)
            eye2.sety(y3 - 20)
            b1.sety(y4 - 20)
            b2.sety(y5 - 20)
    
    
    
    
    
    
    
        if head.direction == "left":
    
    
            x = head.xcor()
            x2 = eye1.xcor()
            x3 = eye2.xcor()
            x4 = b1.xcor()
            x5 = b2.xcor()
            
    
            head.setx(x - 20)
            eye1.setx(x2 - 20)
            eye2.setx(x3 - 20)
            b1.setx(x4 - 20)
            b2.setx(x5 - 20)
            
    
    
        if head.direction == "right":
    
    
    
            x = head.xcor()
            x2 = eye1.xcor()
            x3 = eye2.xcor()
            x4 = b1.xcor()
            x5 = b2.xcor()
        
            
        
            head.setx(x + 20)
            eye1.setx(x2 + 20)
            eye2.setx(x3 + 20)
            b1.setx(x4 + 20)
            b2.setx(x5 + 20)
            
    
    
    
    
    
    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    
    # Main game loop
    while True:
        wn.update()
    
        # Check for a collision with the border
        if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
            time.sleep(1)
            head.goto(0,0)
    
            eye1.goto(-5,5)
            eye2.goto(5,5)
            b1.goto(-5,5)
            b2.goto(5,5)
    
            head.direction = "stop"
    
            eye1.direction = "stop"
            eye2.direction = "stop"
            b1.direction = "stop"
            b2.direction = "stop"
    
    
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
    
            # Clear the segments list
            segments.clear()
    
            # Reset the score
            store_score(score,session)
            score = 0
    
            # Reset speed to the same as in beginning of game
            delay = session
    
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    
        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x,y)
    
            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)
    
            # Shorten the delay
            delay -= 0.005
    
            # Increase the score
            score += 10
    
            if score > high_score:
                high_score = score
    
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
    
        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)
    
        move()
    
        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
    
                eye1.goto(-5,5)
                eye2.goto(5,5)
                b1.goto(-5,5)
                b2.goto(5,5)
    
                head.direction = "stop"
    
                eye1.direction = "stop"
                eye2.direction = "stop"
                b1.direction = "stop"
                b2.direction = "stop"
    
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
    
                # Clear the segments list
                segments.clear()
    
                # Reset the score
                store_score(score,session)
                score = 0
    
                # Reset speed to the same as in beginning of game
                delay = session
    
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
        time.sleep(delay)
    
    wn.mainloop()
    turtle.Terminator()
           
def instruc():
    # instructions text!!
     info ="1.Use your keys “w” for up, “s” for down, “d” for right, and “a” for left.\n2. If you run the snake into the wall or its own tail: you lose.\n3. Eat the red balls to grow longer and gain points.\n4. For faster/slower speeds, go to options.\n\n ENJOY!! :)"
     m = tkinter.messagebox.showinfo("Instructions", info)
        
def options():
    def get_speed(value):
        print(value)
        global real_val
        real_val = value
        
            
    option = tkinter.Tk()
    option.title("Options")
    option.geometry('500x500')
    #speed label
    tkinter.Label(option, text="Speed").grid(column=0,row=0)
    
    #speed options
    tkinter.Button(option, text = "1", command=lambda: get_speed(0.1)).grid(column=0,row=2)
    tkinter.Button(option, text = "2", command=lambda: get_speed(0.090)).grid(column=1,row=2)
    tkinter.Button(option, text = "3", command=lambda: get_speed(0.080)).grid(column=2,row=2)
    tkinter.Button(option, text = "4", command=lambda: get_speed(0.070)).grid(column=3,row=2)
    tkinter.Button(option, text = "5", command=lambda: get_speed(0.060)).grid(column=4,row=2)
    tkinter.Button(option, text = "6", command=lambda: get_speed(0.050)).grid(column=5,row=2)
    tkinter.Button(option, text = "7", command=lambda: get_speed(0.040)).grid(column=6,row=2)
    tkinter.Button(option, text = "8", command=lambda: get_speed(0.030)).grid(column=7,row=2)
    tkinter.Button(option, text = "9", command=lambda: get_speed(0.020)).grid(column=8,row=2)

def store_score(score,v):
    lvl = 0
    if v == 0.1:
        lvl = 1
    elif v == 0.090:
        lvl = 2
    elif v == 0.080:
        lvl = 3
    elif v == 0.070:
        lvl = 4
    elif v == 0.060:
        lvl = 5
    elif v == 0.050:
        lvl = 6
    elif v == 0.040:
        lvl = 7
    elif v == 0.030:
        lvl = 8
    elif v == 0.020:
        lvl = 9        
    
    file = open("score_logs.txt", "a")
    file.write(str(datetime.now()))
    file.write("\t\tScore: "+str(score)+"\t\tSpeed Level: "+str(lvl)+"\n\n")
    file.close()
    
def show_score():
    file = open("score_logs.txt", "r")
    info = file.read()
    tkinter.messagebox.showinfo("Score Records", info)
    file.close()
    
def stop_sound():
    pygame.mixer.music.pause()
    
def play_sound():
    pygame.mixer.music.unpause()  

window = tkinter.Tk()

# window title name
window.title("Snake Game")
window.geometry('1000x1000')

Tops = tkinter.Frame(window,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

lblinfo = tkinter.Label(Tops, font=( 'aria' ,30, 'bold' ),text="Welcome to the Snake Game!!",fg="firebrick3",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

bt1 = tkinter.Button(window, text="New Game", bg="green",font=("Arial Bold",30), fg="white", command = new_game).pack()
bt2 = tkinter.Button(window, text="Scores", bg="green",font=("Arial Bold",30), fg="white", command=show_score).pack()
bt3 = tkinter.Button(window, text="Options", bg="green",font=("Arial Bold",30), fg="white", command=options).pack()
bt4 = tkinter.Button(window, text="Instructions", bg="green", font=("Arial Bold",30),fg="white", command=instruc).pack()
bt5 = tkinter.Button(window, text= "sound on", bg = "yellow",height= 1, width = 8, font=("Arial Bold",15), fg = "black", command= play_sound)
bt6 = tkinter.Button(window, text= "sound off", height= 1, width = 8,bg = "yellow", font=("Arial Bold",15), fg = "black", command= stop_sound)
bt5.pack(side=tkinter.RIGHT)
bt6.pack(side=tkinter.LEFT)

window.mainloop()

pygame.quit()
