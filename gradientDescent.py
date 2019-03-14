from cost import cost
import numpy as np

chordEpsilon = 0.04/100
twistEpsilon = 0.6

def gradientStep(x,currentCost):
    # x = [y1, y2, y3, y4, t1, t2, t3]
    x = np.array(x)
    step = np.array([0.1,0.1,0.1,0.1,70,70,70])
    grad = computeGradient(x,currentCost)

    newX = x - np.multiply(step,grad)

    newCost = cost(newX)

    return newX, newCost

def computeGradient(x,currentCost):

    y1, y2, y3, y4, t1, t2, t3 = x

    # -------------------------------------------------------
    newCost = cost([y1+chordEpsilon,y2,y3,y4,t1,t2,t3])
    grad_y1 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    newCost = cost([y1,y2+chordEpsilon,y3,y4,t1,t2,t3])
    grad_y2 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    newCost = cost([y1,y2,y3+chordEpsilon,y4,t1,t2,t3])
    grad_y3 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    newCost = cost([y1,y2,y3,y4+chordEpsilon,t1,t2,t3])
    grad_y4 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    newCost = cost([y1,y2,y3,y4,t1+twistEpsilon,t2,t3])
    grad_t1 =  (newCost - currentCost) / twistEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    newCost = cost([y1,y2,y3,y4,t1,t2+twistEpsilon,t3])
    grad_t2 =  (newCost - currentCost) / twistEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    newCost = cost([y1,y2,y3,y4,t1,t2,t3+twistEpsilon])
    grad_t3 =  (newCost - currentCost) / twistEpsilon
    # -------------------------------------------------------

    gradient = np.array([
                grad_y1,
                grad_y2,
                grad_y3,
                grad_y4,
                grad_t1,
                grad_t2,
                grad_t3
                ])

    return gradient

if __name__ == '__main__':
    currCost = cost([0.5,0.45,0.35,0.25,12,12,12])
    newX, newCost = gradientStep([0.5,0.45,0.35,0.25,12,12,12],currCost)
    print(newX)
    print(currCost)
    print(newCost)
