import turtle
from levels import level_1

wn = turtle.Screen()
wn.bgcolor('#2F4F4F')
wn.title('Maze Game')
wn.setup(width=700, height=700)
wn.tracer(0)


# classes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('#362020')
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape('circle')
        self.color('#19212a')

    def move_up(self):
        new_x_cor = self.xcor()
        new_y_cor = self.ycor() + 24
        check = self.check_player_wall_collision(new_x_cor, new_y_cor)
        if check:
            self.setposition(new_x_cor, new_y_cor)

    def move_down(self):
        new_x_cor = self.xcor()
        new_y_cor = self.ycor() - 24
        check = self.check_player_wall_collision(new_x_cor, new_y_cor)
        if check:
            self.setposition(self.xcor(), self.ycor() - 24)

    def move_left(self):
        new_x_cor = self.xcor() - 24
        new_y_cor = self.ycor()
        check = self.check_player_wall_collision(new_x_cor, new_y_cor)
        if check:
            self.setposition(new_x_cor, new_y_cor)

    def move_right(self):
        new_x_cor = self.xcor() + 24
        new_y_cor = self.ycor()
        check = self.check_player_wall_collision(new_x_cor, new_y_cor)
        if check:
            self.setposition(new_x_cor, new_y_cor)

    def check_player_wall_collision(self, next_x, next_y):
        if (next_x, next_y) not in walls:
            return True
        else:
            return False


# game status
levelsList = []
walls = []

# levels
levelsList.append(level_1)


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
                walls.append((screen_x, screen_y))

            if character == 'P':
                player.setposition(screen_x, screen_y)


# class instances
pen = Pen()
player = Player()

# keyboard bindings
wn.listen()
wn.onkeypress(player.move_up, "Up")
wn.onkeypress(player.move_down, "Down")
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")


# append levels to levels list
setup_maze(levelsList[0])

# main loop
while True:
    wn.update()
    pass