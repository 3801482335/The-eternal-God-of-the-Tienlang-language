from turtle import *
from time import *

def drawPointers():
    tracer(False)
    hour_pointer.reset()
    min_pointer.reset()
    sec_pointer.reset()
    h = localtime().tm_hour
    m = localtime().tm_min
    hour_deg = -360/(12*60)*(60*h+m)+90
    hour_pointer.width(8)
    hour_pointer.color("white")
    hour_pointer.seth(hour_deg)
    hour_pointer.fd(60)
    hour_pointer.hideturtle()
    min_deg = -6*m+90
    min_pointer.width(4)
    min_pointer.color("white")
    min_pointer.seth(min_deg)
    min_pointer.fd(110)
    s = localtime().tm_sec
    sec_deg = -6*s+90
    sec_pointer.width(2)
    sec_pointer.color("white")
    sec_pointer.seth(sec_deg)
    sec_pointer.fd(140)
    tracer(True)
    ontimer(drawPointers,500)

hour_pointer = Turtle()
min_pointer = Turtle()
sec_pointer = Turtle()
color('#ffa500','#ffbb00')
goto(0,-150)

begin_fill()
width(30)
circle(150)
end_fill()

color('#fff')
pu()

for hour in [12,3,6,9]:
    home()
    goto(0,-9)


    seth(-hour*30+90)
    fd(148)
    write(str(hour),False,'center',('Arial',18,'normal'))
hideturtle()
drawPointers()
done()
