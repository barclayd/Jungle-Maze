import turtle
import random
from levels import level_1
from sprites import sprite_images

wn = turtle.Screen()
wn.bgcolor('#1c2f2f')
wn.title('Maze Game')
wn.setup(width=700, height=700)
wn.tracer(0)
grid_block_size = 24

# set up sprites
for sprite in sprite_images:
    wn.register_shape(sprite)


# classes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('#362020')
        self.shape("jungle.gif")
        self.penup()
        self.speed(0)
        self.name = 'Wall'


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.name = 'Player'
        self.shape("player-right.gif")
        self.gold = 0

    def move_up(self):
        new_x_cor = self.xcor()
        new_y_cor = self.ycor() + 24
        check = check_wall_collision(new_x_cor, new_y_cor, walls)
        if check:
            self.setposition(new_x_cor, new_y_cor)

    def move_down(self):
        new_x_cor = self.xcor()
        new_y_cor = self.ycor() - 24
        check = check_wall_collision(new_x_cor, new_y_cor, walls)
        if check:
            self.setposition(self.xcor(), self.ycor() - 24)

    def move_left(self):
        new_x_cor = self.xcor() - 24
        new_y_cor = self.ycor()
        check = check_wall_collision(new_x_cor, new_y_cor, walls)
        if check:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-left.gif")

    def move_right(self):
        new_x_cor = self.xcor() + 24
        new_y_cor = self.ycor()
        check = check_wall_collision(new_x_cor, new_y_cor, walls)
        if check:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-right.gif")

    def hide(self):
        hide_sprite(self)


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.name = 'Treasure'
        self.shape('gold.gif')
        self.color('#D4AF37')
        self.gold = 100
        self.goto(x, y)

    def hide(self):
        hide_sprite(self)


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.gold = 50
        self.name = 'Enemy'
        self.shape('enemy-right.gif')
        self.setposition(x, y)
        self.direction = set_direction()

    def change_direction(self):
        if self.direction == 'up':
            dx = 0
            dy = 24
        elif self.direction == 'down':
            dx = 0
            dy = -24
        elif self.direction == 'left':
            dx = -24
            dy = 0
            self.shape('enemy-left.gif')
        elif self.direction == 'right':
            dx = 24
            dy = 0
            self.shape('enemy-right.gif')

        # check if player is near
        if self.distance(player) < (difficulty * 100):
            if player.xcor() < self.xcor():
                self.direction = 'left'

            elif player.xcor() > self.xcor():
                self.direction = 'right'

            elif player.ycor() < self.ycor():
                self.direction = 'down'

            elif player.ycor() > self.ycor():
                self.direction = 'up'

        # move enemy
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # check for collisions
        check = check_wall_collision(move_to_x, move_to_y, walls)
        if check:
            self.setposition(move_to_x, move_to_y)
        else:
            # choose a different direction
            self.direction = set_direction()

        # reposition enemies after a certain time has passed
        wn.ontimer(self.change_direction, t=random.randint(100, 300))

    def hide(self):
        hide_sprite(self)


# game status
levelsList = []
walls = []
treasures = []
enemies = []
difficulty = 1

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

            if character == 'E':
                enemies.append(Enemy(screen_x, screen_y))


def collision_check(sprite1, sprite2, block_size):
    global difficulty
    if sprite2.distance(sprite1) < block_size:
        if sprite2.name == 'Treasure':
            sprite1.gold += sprite2.gold
            sprite2.hide()
            difficulty += 1
            treasures.remove(sprite2)
        if sprite2.name == 'Enemy':
            sprite1.hide()
            print("Player with {} gold was killed by Enemy. GAME OVER!".format(player.gold))


def start_enemies_moving(t):
    for enemy in enemies:
        wn.ontimer(enemy.change_direction, t=t)


def set_direction():
    return random.choice(['up', 'down', 'left', 'right'])


def hide_sprite(sprite):
    sprite.setposition(2000, 2000)
    sprite.hideturtle()


def check_wall_collision(next_x, next_y, object_list):
    if (next_x, next_y) not in object_list:
        return True
    else:
        return False


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
# set enemies moving after given timer
start_enemies_moving(250)
# main loop
while True:
    # check player and treasure collision
    for treasure in treasures:
        collision_check(player, treasure, grid_block_size)
    # check player and enemy collision
    for enemy in enemies:
        collision_check(player, enemy, grid_block_size)
    # update screen
    wn.update()
