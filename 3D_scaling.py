import turtle
import numpy as np

Scaling = turtle.Turtle()
turtle.speed(0)

x= [0, 0, 50, 50]
y= [0, 50, 150, 0]
z= [0, 0, 50, 100]
M= [0, 0, 0, 0]

sX = float(input("scaling factor for x"))
sY = float(input("scaling factor for y"))
sZ = float(input("scaling factor for z"))

for i in range(4):
    M[i]= np.array([[x[i]],
      [y[i]],
      [z[i]],
      [1]])

M5= np.array([[sX, 0, 0, 0],
     [0, sY,  0, 0],
     [0, 0,  sZ, 0],
     [0, 0, 0, 1]])

P1 = np.dot(M5,M[0])
P2 = np.dot(M5,M[1])
P3 = np.dot(M5,M[2])
P4 = np.dot(M5,M[3])

for j in range(4):
    x[j]= x[j]+(z[j]*np.sqrt(1/2))
    y[j]= y[j]+(z[j]*np.sqrt(1/2))

Scaling.penup()
Scaling.goto(x[0],y[0])
Scaling.pendown()
Scaling.goto(x[1],y[1])
Scaling.goto(x[2],y[2])
Scaling.goto(x[0],y[0])
Scaling.goto(x[3],y[3])
Scaling.goto(x[1],y[1])
Scaling.penup()
Scaling.goto(x[3],y[3])
Scaling.pendown()
Scaling.goto(x[2],y[2])
Scaling.penup()

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

def scale():
    Scaling.clear()
    Scaling.penup()
    Scaling.goto(x[0], y[0])
    Scaling.pendown()
    Scaling.goto(x[1], y[1])
    Scaling.goto(x[2], y[2])
    Scaling.goto(x[0], y[0])
    Scaling.goto(x[3], y[3])
    Scaling.goto(x[1], y[1])
    Scaling.penup()
    Scaling.goto(x[3], y[3])
    Scaling.pendown()
    Scaling.goto(x[2], y[2])

scale()
turtle.done()












