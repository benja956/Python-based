#体育比赛竞技分析
import time
from random import random
def printinfo():
     print("这个程序模拟两个选手A,B的某种比赛")
     print("程序运行需要输入AB的能力值（0.01~0.99）和比赛次数")

def getinputs():
     NA = eval(input("请输入选手A的能力值："))
     NB = eval(input("请输入选手B的能力值："))
     N =  eval(input("请输入模拟次数："))
     return NA,NB,N

def printsummary(winsA,winsB):
     N = winsA + winsB
     print("进行比赛{}场".format(N))
     print("选手A获胜{}场,占比{:0.1%}".format(winsA,winsA/N))
     print("选手B获胜{}场,占比{:0.1%}".format(winsB,winsB/N))

def simngames(N,NA,NB):
     winsA,winsB = 0,0
     for i in range(N):
          scoreA,scoreB = simonegame(NA,NB)
          if scoreA>scoreB:
               winsA += 1
          else:
               winsB += 1
     return winsA,winsB
     

def simonegame(NA,NB):
     scoreA,scoreB = 0,0
     serving = "A"
     while not gameover(scoreA,scoreB):
          if serving == "A":
               if random() < NA:
                    scoreA += 1
               else:
                    serving = "B"
          if serving == "B":
               if random() < NB:
                         scoreB += 1
               else:
                    serving = "A"
     return scoreA,scoreB

def gameover(scoreA,scoreB):
     return scoreA == 15 or scoreB == 15

def main():
     printinfo()
    
     NA,NB,N = getinputs()
     print(N)
     winsA,winsB = simngames(N,NA,NB)
     printsummary(winsA,winsB)

main()
     
