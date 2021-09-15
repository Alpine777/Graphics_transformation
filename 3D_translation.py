import turtle
import numpy as np

Translate = turtle.Turtle()
Translate.speed(0)

x= [0, 0, 50, 50]
y= [0, 50, 150, 0]
z= [0, 0, 50, 100]
M= [0, 0, 0, 0]

tX = int(input("translation factor for x"))
tY = int(input("translation factor for y"))
tZ = int(input("translation factor for z"))

for i in range(4):
    M[i]= np.array([[x[i]],
      [y[i]],
      [z[i]],
      [1]])

M5= np.array([[1, 0, 0, tX],
     [0, 1,  0, tY],
     [0, 0,  1, tZ],
     [0, 0, 0, 1]])

P1 = np.dot(M5,M[0])
P2 = np.dot(M5,M[1])
P3 = np.dot(M5,M[2])
P4 = np.dot(M5,M[3])

for j in range(4):
    x[j]= x[j]+(z[j]*np.sqrt(1/2))
    y[j]= y[j]+(z[j]*np.sqrt(1/2))

Translate.penup()
Translate.goto(x[0],y[0])
Translate.pendown()
Translate.goto(x[1],y[1])
Translate.goto(x[2],y[2])
Translate.goto(x[0],y[0])
Translate.goto(x[3],y[3])
Translate.goto(x[1],y[1])
Translate.penup()
Translate.goto(x[3],y[3])
Translate.pendown()
Translate.goto(x[2],y[2])
Translate.penup()

one_d = []
one_dd = []
one_ddd = []
one = []

for k in range(3):
    one_d.append(P1[k][0])
    one_dd.append(P2[k][0])
    one_ddd.append(P3[k][0])
    one.append(P4[k][0])

x[0], y[0], z[0]= one_d[0], one_d[1], one_d[2]
x[1], y[1], z[1]= one_dd[0], one_dd[1], one_dd[2]
x[2], y[2], z[2]= one_ddd[0], one_ddd[1], one_ddd[2]
x[3], y[3], z[3]= one[0], one[1], one[2]

for l in range(4):
    x[l]= x[l]+(z[l]*np.sqrt(1/2))
    y[l]= y[l]+(z[l]*np.sqrt(1/2))

def translate():
    Translate.penup()
    Translate.goto(x[0], y[0])
    Translate.pendown()
    Translate.goto(x[1], y[1])
    Translate.goto(x[2], y[2])
    Translate.goto(x[0], y[0])
    Translate.goto(x[3], y[3])
    Translate.goto(x[1], y[1])
    Translate.penup()
    Translate.goto(x[3], y[3])
    Translate.pendown()
    Translate.goto(x[2], y[2])

translate()
turtle.done()





