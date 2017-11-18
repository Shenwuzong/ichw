import math
import turtle
sun=turtle.Turtle()
mer=turtle.Turtle()
ven=turtle.Turtle()
ear=turtle.Turtle()
mar=turtle.Turtle()
sat=turtle.Turtle()
colors=["red","blue","yellow","green","pink","black"]

def huaty(pla,a,siz,co):
    b=a-40
    loca=2*a-b
    pla.shape("circle")
    pla.color(colors[co])
    pla.shapesize(siz,siz,1)
    pla.up()
    pla.goto(loca,0)
    pla.down()

huaty(sun,0,3,0)
huaty(mer,100,0.5,1)
huaty(ven,130,1.0,2)
huaty(ear,150,1.0,3)
huaty(mar,180,0.9,4)
huaty(sat,220,1.5,5)

for i in range(360000):
    sun.setposition(40,0)
    mer.setposition(40+100*math.cos(i/100),60*math.sin(i/100))
    ven.setposition(40+130*math.cos(i/100),90*math.sin(i/100))
    ear.setposition(40+150*math.cos(i/100),110*math.sin(i/100))
    mar.setposition(40+180*math.cos(i/100),140*math.sin(i/100))
    sat.setposition(40+215*math.cos(i/100),175*math.sin(i/100))