import turtle
import numpy as np

Reflect = turtle.Turtle()
Reflect.speed(0)
x= [0, 100, 0]
y= [0, 20, 100]
M =[0, 0, 0]

select= int(input(("Press 1 for reflection about x axis,\n"
         "Press 2 for reflection about y axis,\n"
         "Press 3 for reflection about origin,\n"
         "Press 4 for reflection about x=y")))

for i in range(3):
    M[i]= np.array([[x[i]],
      [y[i]],
      [1]])
if select == 1:
    M4= np.array([[1, 0, 0],
     [0, -1,  0],
     [0, 0,  1]])
elif select== 2:
    M4= np.array([[-1, 0, 0],
     [0, 1,  0],
     [0, 0,  1]])
elif select== 3:
    M4= np.array([[-1, 0, 0],
     [0, -1,  0],
     [0, 0,  1]])
else:
   M4= np.array([[0, 1, 0],
                [1, 0, 0],
              [0, 0, 1]])

P1 = np.dot(M4,M[0])
P2 = np.dot(M4,M[1])
P3 = np.dot(M4,M[2])

Reflect.penup()
Reflect.goto(x[0],y[0])
Reflect.pendown()
Reflect.goto(x[1],y[1])
Reflect.goto(x[2],y[2])
Reflect.goto(x[0],y[0])
Reflect.penup()

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

def reflect():
    Reflect.goto(x1, y1)
    Reflect.pendown()
    Reflect.goto(x2, y2)
    Reflect.goto(x3, y3)
    Reflect.goto(x1, y1)

reflect()
turtle.done()





