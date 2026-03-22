import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)

# Movement functions
def move_forward():
    # move forward
    

def move_backward():
    # move backward
    

def turn_left():
    # turn left
    

def turn_right():
    # turn right
    

# Listen for keyboard input
screen.listen()

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.mainloop()
