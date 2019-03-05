def chordBezier(y1,y2,y3,y4,t,L):
    c = (1-t)**3 * y1 + 3 * (1-t)**2 * t * y2 + 3 * (1-t) * t**2 * y3 + t**3 * y4
    r = (t**3 + (1-t)**2 * t + 2*(1-t) * t**2) * L

    return c,r

def twistBezier(f1,f2,f3,r,L):
    t = r/L

    f = (1-t)**2 * f1 + 2*(1-t)*t*f2 + t**2 * f3

    return f

def getPropellerArray(y1,y2,y3,y4,f1,f2,f3,L):
    radius = []
    chord = []
    twist = []

    for i in range(20):
        t = 1/19 * i
        c,r = chordBezier(y1,y2,y3,y4,t,L)
        radius.append(r)
        chord.append(c)
        twist.append(twistBezier(f1,f2,f3,r,L))

    return radius,chord,twist
