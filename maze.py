import turtle
from levels import level_1

wn = turtle.Screen()
wn.bgcolor('#1c2f2f')
wn.title('Maze Game')
wn.setup(width=700, height=700)
wn.tracer(0)

wn.register_shape("player-left.gif")
wn.register_shape("player-right.gif")
wn.register_shape("jungle.gif")
wn.register_shape("gold.gif")


# classes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('#362020')
        # self.shape('square')
        self.shape("jungle.gif")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("player-right.gif")
        self.gold = 0

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
            self.shape("player-left.gif")

    def move_right(self):
        new_x_cor = self.xcor() + 24
        new_y_cor = self.ycor()
        check = self.check_player_wall_collision(new_x_cor, new_y_cor)
        if check:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-right.gif")

    def check_player_wall_collision(self, next_x, next_y):
        if (next_x, next_y) not in walls:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape('gold.gif')
        self.color('#D4AF37')
        self.gold = 100
        self.goto(x, y)

    def hide_treasure(self):
        self.setposition(2000, 2000)
        self.hideturtle()


# game status
levelsList = []
walls = []
treasures = []

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

            if character == 'T':
                treasures.append(Treasure(screen_x, screen_y))


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
    # check player and treasure collision
    for treasure in treasures:
        if treasure.distance(player) < 24:
            player.gold += treasure.gold
            print("Player's gold: {}".format(player.gold))
            treasure.hide_treasure()
            treasures.remove(treasure)

    # update screen
    wn.update()
