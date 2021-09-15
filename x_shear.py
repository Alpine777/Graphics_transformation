import turtle
import numpy as np

Shear = turtle.Turtle()
Shear.speed(0)
x= [0, 100, 0]
y= [0, 0, 100]
M =[0, 0, 0]

select= int(input(("Press 1 for shearing about x axis,"
         "Press 2 for shearing about y axis")))

for i in range(3):
    M[i]= np.array([[x[i]],
      [y[i]],
      [1]])

if select== 1:
    shx= int(input("shear factor for x"))
    M4= np.array([[1, shx, 0],
     [0, 1,  0],
     [0, 0,  1]])

else:
    shy = int(input("shear factor for y"))
    M4 = np.array([[1, 0, 0],
                   [shy, 1, 0],
                   [0, 0, 1]])

P1 = np.dot(M4,M[0])
P2 = np.dot(M4,M[1])
P3 = np.dot(M4,M[2])

Shear.penup()
Shear.goto(x[0],y[0])
Shear.pendown()
Shear.goto(x[1],y[1])
Shear.goto(x[2],y[2])
Shear.goto(x[0],y[0])
Shear.penup()

one_d = []
one_dd = []
one_ddd = []

for i in range(2):
    one_d.append(P1[i][0])
    one_dd.append(P2[i][0])
    one_ddd.append(P3[i][0])

x1, y1= one_d[0], one_d[1]
x2, y2= one_dd[0], one_dd[1]
x3, y3= one_ddd[0], one_ddd[1]

def shear():
    Shear.goto(x1, y1)
    Shear.pendown()
    Shear.goto(x2, y2)
    Shear.goto(x3, y3)
    Shear.goto(x1, y1)

shear()
turtle.done()








