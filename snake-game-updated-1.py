import turtle
import random
import time

# basic settings
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(width=700, height=700)
screen.tracer(0)

# game cover
border = turtle.Turtle()
border.color("black")
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()

for side in range(2):
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
border.hideturtle()

# score
score = 0
delay = 0.1

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score : 0", align="center", font=("Courier", 24, "bold"))

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# movement functions
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"
def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"
def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"
def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# restart button
restart_btn = turtle.Turtle()
restart_btn.hideturtle()
restart_btn.penup()
restart_btn.shape("square")
restart_btn.color("black")
restart_btn.shapesize(stretch_wid=1, stretch_len=6)

def show_restart_button():
    restart_btn.goto(0, -50)
    restart_btn.write("Restart", align="center", font=("Courier", 18, "bold"))
    restart_btn.showturtle()
    screen.onclick(on_click_restart)

def on_click_restart(x, y):
    if -60 < x < 60 and -65 < y < -35:
        screen.onclick(None)
        restart_game()

# restart the game
def restart_game():
    global score, delay, old_fruit
    score = 0
    delay = 0.1
    scoring.clear()
    scoring.goto(0, 300)
    scoring.write("Score : 0", align="center", font=("Courier", 24, "bold"))
    snake.goto(0, 0)
    snake.direction = "stop"
    for f in old_fruit:
     f.goto(-0, -0)
    old_fruit.clear()
    fruit.goto(30, 30)
    screen.bgcolor("green")
    restart_btn.clear()
    restart_btn.hideturtle()
    game_loop()

# controls for moving the snake
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# the main loop for the game
def game_loop():
    global score, delay

    while True:
        screen.update()

        # the snake collision with fruit
        if snake.distance(fruit) < 20:
            x = random.randint(-290, 270)
            y = random.randint(-240, 240)
            fruit.goto(x, y)
            scoring.clear()
            score += 1
            scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
            delay -= 0.001

            new_fruit = turtle.Turtle()
            new_fruit.speed(0)
            new_fruit.shape("square")
            new_fruit.color("red")
            new_fruit.penup()
            old_fruit.append(new_fruit)

        # the previus fruit movement
        for i in range(len(old_fruit) - 1, 0, -1):
            x = old_fruit[i - 1].xcor()
            y = old_fruit[i - 1].ycor()
            old_fruit[i].goto(x, y)
        if len(old_fruit) > 0:
            x = snake.xcor()
            y = snake.ycor()
            old_fruit[0].goto(x, y)

        snake_move()

        # snake collision with the walls
        if (snake.xcor() > 280 or snake.xcor() < -300 or
            snake.ycor() > 240 or snake.ycor() < -240):
            screen.bgcolor("turquoise")
            scoring.clear()
            scoring.goto(0, 50)
            scoring.write("   GAME OVER\nYour Score is {}".format(score),
                          align="center", font=("Courier", 30, "bold"))
            show_restart_button()
            break

        # snake collision with its body
        for segment in old_fruit:
            if segment.distance(snake) < 20:
                screen.bgcolor("turquoise")
                scoring.clear()
                scoring.goto(0, 50)
                scoring.write("   GAME OVER\nYour Score is {}".format(score),
                              align="center", font=("Courier", 30, "bold"))
                show_restart_button()
                return

        time.sleep(delay)

game_loop()
screen.mainloop()

