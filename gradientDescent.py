from cost import cost
from scipy import signal
import numpy as np

chordEpsilon = 0.04/100
twistEpsilon = 0.6

epsilon = np.array([
        chordEpsilon,
        chordEpsilon,
        chordEpsilon,
        chordEpsilon,
        twistEpsilon,
        twistEpsilon,
        twistEpsilon
        ])

def gradientDescent(x,currentCost,steps):
    newX, newCost = x, currentCost
    for i in range(steps):
        newX, newCost = gradientStep(newX,newCost)
        print("Step {} is done. The new cost is {}\n{}".format(i+1,newCost,newX))
    return newX,newCost

def gradientStep(x,currentCost):
    # x = [y1, y2, y3, y4, t1, t2, t3]
    x = np.array(x)
    step = 10*epsilon
    grad = computeGradient(x,currentCost)

    normalizedGrad = np.divide(grad,abs(grad))

    newX = proj(x - np.multiply(step,grad))

    newCost = cost(newX)

    return newX, newCost

def computeGradient(x,currentCost):
    newCosts = np.zeros(7)

    for i in range(7):
        newCosts[i] = cost(x+np.multiply(epsilon,signal.unit_impulse(7,i)))

    gradient = np.divide(newCosts-currentCost,epsilon)

    return gradient

chordLowLimit = 0.2
chordHiLimit = 0.6
twistLowLimit = -20
twistHiLimit = 40

def proj(x):
    for i in range(7):
        if i < 4:
            # chord coordinate
            if x[i] < chordLowLimit:
                x[i] = chordLowLimit
            elif x[i] > chordHiLimit:
                x[i] = chordHiLimit
        else:
            # twist coordinate
            if x[i] < twistLowLimit:
                x[i] = twistLowLimit
            elif x[i] > twistHiLimit:
                x[i] = twistHiLimit
    return x


if __name__ == '__main__':
    currCost = cost([0.5,0.45,0.35,0.25,12,12,12])
    newX, newCost = gradientDescent([0.5,0.45,0.35,0.25,12,12,12],currCost,5)
    print(newX)
    print(currCost)
    print(newCost)
