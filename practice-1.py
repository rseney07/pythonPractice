from turtle import *
import math

def poly(t, size = 100, sides = 5, rotation = 0, lineColor = None, fillColor = None):
    psides=sides
    if lineColor != None:
        t.color(lineColor)
    else:
        t.color("black")
    if fillColor != None:
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotation)
    while psides > 0:
        t.fd(size)
        t.lt(360/sides)
        psides -= 1 
    t.rt(rotation)
    t.end_fill()

#5
def para(t, width = 100, height = 100, big_angle = 120, rotation = 0, lineColor = None, fillColor = None):
    t.lt(rotate)
    if lineColor == None:
        t.color("black")
    else:
        t.color(lineColor)
    if fillColor != None:
        t.fillcolor(fillColor)
        t.begin_fill()
    for x in range(2):
        t.fd(width)
        t.lt(big_angle)
        t.fd(height)
        t.lt(180-big_angle)
    t.rt(rotation)
    t.end_fill()
def equilateralTriangle(t, size = 60, rotation = 0, lineColor = None, fillColor = None):
    t.lt(rotation)
    if lineColor == None:
        t.color("black")
    else:
        t.color(lineColor)
    if fillColor != None:
        t.fillcolor(fillColor)
        t.begin_fill()
    for x in range(3):
        t.fd(size)
        t.lt(120)
    t.end_fill()
    t.rt(rotation)

#go foreward the length of the hypotenuse and rotate left by the arc cosine of the adjacent side over the hypotenuse
def line(t, adjacent, opposite, lineColor):
    hypotenuse = math.sqrt((adjacent ** 2) + (opposite ** 2))
    #print("hypotenuse: ", hypotenuse)
    incline = math.acos(adjacent/hypotenuse)*180/math.pi
    #print(incline)
    t.lt(incline)
    t.fd(hypotenuse)

def star(t, points, size, rotation, lineColor):
    p = 0
    interiorAngle = 180-(points-2)*180/points
    exteriorAngle = 180-(180-2*interiorAngle)
    print(interiorAngle, exteriorAngle)
    t.lt(rotation)
    while p < points:
        t.fd(size)
        t.lt(interiorAngle)
        t.fd(size)
        t.rt(exteriorAngle)

        p+=1
    print ("Star, with Points:", points, "Size:", size, "and Rotation:", rotation)




billy = Turtle()
star(billy, 7, 100, 0, "blue")
done()