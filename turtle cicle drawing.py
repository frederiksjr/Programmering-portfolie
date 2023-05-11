# Play with turtle and random modules
import turtle
import random


sc = turtle.Screen()
t = turtle.Turtle()
sc.setup(800,600)
sc.title("setup")
t.pensize(3)
t.speed(0)

#  Drawing diff circles with random radius in diff positions , Range(-200,200)

for n in range(100):
      color = ["red", "green", "blue", "purple", "yellow", "orange", "black"]
      t.pencolor(random.choice(color))
      t.penup()
      t.goto(random.randint(-200,200), random.randint(-200,200))
      t.pendown()
      t.circle(random.randint(0,20))


sc.exitonclick()