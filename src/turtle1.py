import turtle as t
t.colormode(255)
t.pencolor(255,127,127)
t.speed(0)
t.hideturtle()
t.bgcolor(0,0,0)
t.pensize(10)
t.penup()

n=1
k=1
p=1

t.forward(50)
t.pendown()
t.left(90)
while True:
    if n%6 == 0: t.pencolor(255,int(127-n),int(127-n))
    elif n%6 == 1: t.pencolor(255,255,int(127-n))
    elif n%6 == 2: t.pencolor(int(127-n),255,int(127-n))
    elif n%6 == 3: t.pencolor(int(127-n),255,255)
    elif n%6 == 4: t.pencolor(int(127-n),int(127-n),255)
    elif n%6 == 5: t.pencolor(255,int(127-n),255)
    t.bgcolor(int(2*n),int(2*n),int(2*n))
    t.forward(p)
    t.left(107)
    if n >= 127: k=-1
    elif n <= 0 : k=1
    n+=k
    p+=1
    print(n)

