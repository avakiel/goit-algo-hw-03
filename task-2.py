import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    
    height = size * (3 ** 0.5) / 2
    t.penup()
    t.goto(-size / 2, -height / 3)
    t.pendown()
    t.setheading(0)

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    try:
        order = int(input("Enter the level of recursion: "))
        if order < 0:
            print("The level of recursion cannot be negative. The level 0 is used.")
            order = 0
        draw_koch_snowflake(order)
    except ValueError:
        print("Error: enter an integer. The default level is 3.")
        draw_koch_snowflake(3)
