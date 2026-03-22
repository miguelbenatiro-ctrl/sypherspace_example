import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(5)

def draw_square(size):
    for i in range(4):
        # move forward
        

        # turn 90 degrees
        

def draw_triangle(size):
    for i in range(3):
        # move forward
        

        # turn 120 degrees
        

# Ask user what to draw
shape = input("Choose a shape (square/triangle): ")
size = int(input("Enter size (e.g. 100): "))

if shape == "square":
    draw_square(size)

elif shape == "triangle":
    draw_triangle(size)

else:
    print("Invalid shape")

screen.exitonclick()
