#v1
"""
import turtle
def koch(size,n):
     if n == 0:
          turtle.fd(size)
     else:
          for angle in [0,60,-120,60]:
               turtle.left(angle)
               koch(size/3,n-1)

def main():
     turtle.speed(8)
     turtle.pencolor("blue")
     turtle.penup()
     turtle.fd(-200)
     turtle.pendown()
     for i in range(6):
          koch(100,3)
          turtle.right(60)
          turtle.hideturtle()

main()
"""
#v2
import turtle
import turtle
def koch(size,n):
     if n == 0:
          turtle.fd(size)
     else:
          for angle in [0,60,-120,60]:
               turtle.left(angle)
               koch(size/3,n-1)

def main():
     turtle.setup(600,600)
     turtle.speed(10)
     turtle.pensize(2)
     turtle.pencolor("blue")
     turtle.penup()
     turtle.goto(-200,100)
     turtle.pendown()
     for i in range(3):
          koch(400,3)
          turtle.right(120)
          turtle.hideturtle()

main()
