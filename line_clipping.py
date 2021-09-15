import turtle

turtle.delay(20)

x_min, x_max = 10, 150
y_min, y_max = 10, 100

x1, y1 = 0, 120
x2, y2 = 130, 5

l = x_max - x_min
w = y_max - y_min

def window():
    turtle.penup()
    turtle.goto(x_min, y_min)
    turtle.pendown()
    for i in range(2):
        turtle.forward(l)
        turtle.left(90)

        turtle.forward(w)
        turtle.left(90)
window()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)

turtle.clear()

inside = 0
left = 1
right = 2
bottom = 4
top = 8

def computeCode(x, y):
    code = inside
    if x < x_min:  
        code |= left
    elif x > x_max:  
        code |= right
    if y < y_min: 
        code |= bottom
    elif y > y_max:  
        code |= top

    return code

def Clip(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)

    while True:
        if code1 == 0 and code2 == 0:
            break

        elif (code1 & code2) != 0:
            break

        # Line needs clipping
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & top:
                # point is above the clip rectangle
                x = x1 + (x2 - x1) * \
                    (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & bottom:
                # point is below the clip rectangle
                x = x1 + (x2 - x1) * \
                    (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & right:
                # point is to the right of the clip rectangle
                y = y1 + (y2 - y1) * \
                    (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & left:
                # point is to the left of the clip rectangle
                y = y1 + (y2 - y1) * \
                    (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

window()
Clip(x1, y1, x2, y2)
turtle.done()