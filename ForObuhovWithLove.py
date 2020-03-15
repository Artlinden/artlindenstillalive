from math import *
def f(x, y):
 return round(pow(((x-4)*cos(120)+(y-2)*sin(120)),2)+pow(((y-2)*cos(120)-(x-4)*sin(120)),2)/4,7)

def g1(x, y):
    if y ==0:
        return 1000000000
    g = (1 / y)-x*sin(y)
    if g == 0:
        return 0.0000000001
    else:
        return g


def g2(x):
    g =  x
    if g == 0:
        return 0.0000000001
    else:
        return g

def P(x, y, k):
    return k * (1 / g1(x, y) + 1 / g2(x))

def Z(x, y, k):
    return round(f(x, y) + P(x, y, k),7)

def fx(x, y,k):
    d = 0.0001
    return (Z(x + d, y,k) - Z(x, y,k)) / d

def fy(x, y,k):
    d = 0.0001
    return (Z(x, y + d,k) - Z(x, y,k)) / d

def PowSum(f1, f2):
    return pow(f1, 2) + pow(f2, 2)
def cheak(x,y):
    return g1(x,y)<0 or g2(x)<0


x1 = 4.5
y1 = 4

k=1
Z1=0
x2=0
y2=0
Z2=0
C=0.1
Line = []
stop = False
X = (x2,y2)
while abs(x1-X[0]) >0.000001 and abs(y1-X[1]) >0.000001:
    X = (x1,y1)
    h = 0.0001
    Z1 = Z(x1, y1,k)
    Line.append((x1,y1,Z1))
    gradX = fx(x1, y1,k)
    gradY = fy(x1, y1,k)
    print((x1,y1,Z1))
    x2 = x1 - h * gradX
    y2 = y1 - h * gradY
    Z2 = Z(x2, y2,k)
    dA = 2  # Коэфициент умножения H
    if cheak(x2,y2):
        k*=C
        continue
    if Z2 > Z1:
        dA = (1 / 2)
    v = (x2, y2, Z2 + 1)
    while Z2 < v[2]:
        Line.append((x2,y2,Z2))
        v = (x2, y2, Z2)
        h *= dA
        x2 = x1 - h * gradX
        y2 = y1 - h * gradY
        if cheak(x2, y2):
            k *= C
            stop = True
            break
        Z2 = Z(x2, y2,k)
    h /= dA
    x2 = v[0]
    y2 = v[1]
    Z2 = v[2]
    if stop:
        x1 = v[0]
        y1 = v[1]
        continue

    N = 0
    while PowSum(fx(x2, y2,k), fy(x2, y2,k)) >= 0.00001:
        print((x2,y2,Z2))
        N += 1
        x1 = x2
        y1 = y2
        Z1 = Z2
        gradX = fx(x1, y1,k)
        gradY = fy(x1, y1,k)
        x2 = x1 - h * gradX
        y2 = y1 - h * gradY
        Z2 = Z(x2, y2,k)
        if cheak(x2, y2):
            x2 = v[0]
            y2 = v[1]
            break
        dA = 2
        if Z2 > Z1:
            dA = (1 / 2)
        v = (x2, y2, Z2 + 1)  # буфер
        while Z2 < v[2]:
            Line.append((x2,y2,Z2))
            v = (x2, y2, Z2)
            h *= dA
            x2 = x1 - h * gradX
            y2 = y1 - h * gradY
            Z2 = Z(x2, y2,k)
            if cheak(x2, y2):
                stop = True
                x2 = v[0]
                y2 = v[1]
                break
        h /= dA
        if stop:
            x1 = v[0]
            y1 = v[1]
            break
        x2 = v[0]
        y2 = v[1]
        Z2 = v[2]
    print((x2,y2,Z2))
    x1=x2
    y1=y2
    k *= C
Line.append((x1,y1,Z(x1,y1,k/C)))

