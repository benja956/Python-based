#V1
"""
import turtle as tt
def drawline(draw):
     tt.pendown() if draw else tt.penup()
     tt.fd(40)
     tt.right(90)
def drawdigit(digit):
     drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
     drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,2,6,8] else drawline(False)
     tt.left(90)
     drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
     drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
     tt.left(180)
     tt.penup()
     tt.fd(25)
def drawdate(date):
     for i in date:
          drawdigit(eval(i))
def main():
     tt.penup()
     tt.fd(-300)
     tt.pensize(5)
     drawdate("20190306")
     tt.hideturtle()
     tt.done()
main()
"""
#V2

import turtle as tt
def drawgap(n):
     tt.penup()
     tt.fd(n)
def drawline(draw):
     drawgap(5)
     tt.pendown() if draw else tt.penup()
     tt.fd(40)
     drawgap(5)
     tt.right(90)
def drawdigit(digit):
     drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
     drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,2,6,8] else drawline(False)
     tt.left(90)
     drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
     drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
     tt.left(180)
     tt.penup()
     tt.fd(25)
def drawdate(date):
     for i in date:
          if i == "n":
               #draw
               tt.write("年",font=("Arial", 18, "normal"))
               drawgap(30)
          elif i == "y":
               #draw
               tt.write("月",font=("Arial", 18, "normal"))
               drawgap(30)
          elif i == "r":
               #draw
               tt.write("日",font=("Arial", 18, "normal"))
               drawgap(30)
          else:
               drawdigit(eval(i))
def main():
     tt.penup()
     tt.fd(-300)
     tt.pensize(5)
     drawdate("2019n03y06r")
     tt.hideturtle()
     tt.done()
main()
