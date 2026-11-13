#Snake game
import random
import time
import turtle

# Game configuration
delay = 0.1
score = 0
high_score = 0

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off automatic screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Score: 0  High Score: 0", align="center", font=("Courier", 20, "normal")
)


# Movement functions
def go_up():
  if head.direction != "down":
    head.direction = "up"


def go_down():
  if head.direction != "up":
    head.direction = "down"


def go_left():
  if head.direction != "right":
    head.direction = "left"


def go_right():
  if head.direction != "left":
    head.direction = "right"


def move():
  if head.direction == "up":
    head.sety(head.ycor() + 20)
  if head.direction == "down":
    head.sety(head.ycor() - 20)
  if head.direction == "left":
    head.setx(head.xcor() - 20)
  if head.direction == "right":
    head.setx(head.xcor() + 20)


def reset_game():
  global score, delay
  time.sleep(1)
  head.goto(0, 0)
  head.direction = "stop"

  for segment in segments:
    segment.goto(1000, 1000)
  segments.clear()

  score = 0
  delay = 0.1
  pen.clear()
  pen.write(
      f"Score: {score}  High Score: {high_score}",
      align="center",
      font=("Courier", 20, "normal"),
  )


# Keyboard bindings
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Main game loop
while True:
  win.update()

  # Check for collision with the border
  if (
      head.xcor() > 290
      or head.xcor() < -290
      or head.ycor() > 290
      or head.ycor() < -290
  ):
    reset_game()

  # Check for collision with food
  if head.distance(food) < 20:
    # Move food to a random grid-aligned spot
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)

    # Add a new segment to the snake
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("lightgreen")
    new_segment.penup()
    segments.append(new_segment)

    # Speed up the game slightly and update score
    delay = max(0.05, delay - 0.002)
    score += 10
    if score > high_score:
      high_score = score

    pen.clear()
    pen.write(
        f"Score: {score}  High Score: {high_score}",
        align="center",
        font=("Courier", 20, "normal"),
    )

  # Move the end segments first in reverse order
  for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)

  # Move segment 0 to where the head is
  if len(segments) > 0:
    segments[0].goto(head.xcor(), head.ycor())

  move()

  # Check for head collision with body segments
  for segment in segments:
    if segment.distance(head) < 20:
      reset_game()
      break

  time.sleep(delay)
