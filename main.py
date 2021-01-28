import turtle

t = turtle.Turtle()
radius = 20
t.speed(0)

t.ht()

def draw_circle(): 
  t.pendown()
  t.begin_fill()
  t.color("light blue")
  t.circle(radius)
  t.end_fill()
  t.penup()


def draw_circle_row():
  for i in range(10):
    draw_circle()
    t.forward(2 * radius)

def move_up_a_row():
  t.left(90)
  t.forward(2 * radius)
  t.backward(400)

def make_highlight(startX, startY):
  t.penup()
  t.setposition(startX, startY)
  t.pensize(1)
  t.forward(10)
  t.left(90)
  t.forward(20)
  t.pendown()
  t.color("white")
  t.circle(10, 90)
  t.penup()
  t.setposition(startX, startY)
  t.forward(10)
  t.right(180)

def make_highlight_row(startX, startY):
  for i in range(10):
    offset = 20 * 2 * i 
    make_highlight(startX + offset, startY)

start_pos = -200
t.penup()
for i in range(10):
  offset = i * 20 * 2
  t.setposition(-180, -200 + offset)
  draw_circle_row()
  make_highlight_row(-180, -200 + offset)

# https://docs.python.org/3/library/turtle.html