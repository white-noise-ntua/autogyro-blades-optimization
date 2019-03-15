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

def gradientStep(x,currentCost):
    # x = [y1, y2, y3, y4, t1, t2, t3]
    x = np.array(x)
    step = np.array([0.1,0.1,0.1,0.1,70,70,70])
    grad = computeGradient(x,currentCost)

    newX = x - np.multiply(step,grad)

    newCost = cost(newX)

    return newX, newCost

def computeGradient(x,currentCost):
    newCosts = np.zeros(7)

    for i in range(7):
        newCosts[i] = cost(x+np.multiply(epsilon,signal.unit_impulse(7,i)))

    gradient = np.divide(newCosts-currentCost,epsilon)

    return gradient

if __name__ == '__main__':
    currCost = cost([0.5,0.45,0.35,0.25,12,12,12])
    newX, newCost = gradientStep([0.5,0.45,0.35,0.25,12,12,12],currCost)
    print(newX)
    print(currCost)
    print(newCost)
