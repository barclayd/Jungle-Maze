import turtle
from levels import level_1

wn = turtle.Screen()
wn.bgcolor('#2F4F4F')
wn.title('Maze Game')
wn.setup(width=700, height=700)


# classes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('#362020')
        self.penup()
        self.speed(0)


# game status
levels = []

# levels
levels.append(level_1)


# functions
def setup_maze(level):
    # for number the given number of rows
    for y in range(len(level)):
        # for number of 'X's in a given row
        for x in range(len(level[y])):
            character = level[y][x]
            # position blocks
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # mark squares in the position of 'X's in the rows
            if character == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()


# class instances
pen = Pen()

# append levels to levels list

setup_maze(level_1)

# main loop
while True:
    pass