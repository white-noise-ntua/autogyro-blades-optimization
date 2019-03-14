from simulation import runSimulation
from cost import calculateCost
from writeInput import writeInput
from curves import getPropellerArray
import numpy as np

chordEpsilon = 0.04/100
twistEpsilon = 0.6
L = 0.257 # propeller's length

def gradientStep(y1,y2,y3,y4,t1,t2,t3,currentCost):

    # -------------------------------------------------------
    # Computing cost's partial derivative with respect to y1

    #calculate cost at y1+chordEpsilon
    r, c, t = getPropellerArray(y1+chordEpsilon,y2,y3,y4,t1,t2,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

    grad_y1 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------


    # -------------------------------------------------------
    # Computing cost's partial derivative with respect to y2
    r, c, t = getPropellerArray(y1,y2+chordEpsilon,y3,y4,t1,t2,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

    grad_y2 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    # Computing cost's partial derivative with respect to y3
    r, c, t = getPropellerArray(y1,y2,y3+chordEpsilon,y4,t1,t2,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

    grad_y3 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    # Computing cost's partial derivative with respect to y4
    r, c, t = getPropellerArray(y1,y2,y3,y4+chordEpsilon,t1,t2,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

    grad_y4 =  (newCost - currentCost) / chordEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    # Computing cost's partial derivative with respect to t1
    r, c, t = getPropellerArray(y1,y2,y3,y4,t1+twistEpsilon,t2,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

    grad_t1 =  (newCost - currentCost) / twistEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    # Computing cost's partial derivative with respect to t2
    r, c, t = getPropellerArray(y1,y2,y3,y4,t1,t2+twistEpsilon,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

    grad_t2 =  (newCost - currentCost) / twistEpsilon
    # -------------------------------------------------------

    # -------------------------------------------------------
    # Computing cost's partial derivative with respect to t3
    r, c, t = getPropellerArray(y1,y2,y3,y4,t1,t2,t3+twistEpsilon,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

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
    r,c,t = getPropellerArray(0.5,0.45,0.35,0.25,0,0,0,L)
    writeInput(r,c,t)
    w,v = runSimulation()
    gradientStep(0.5,0.45,0.35,0.25,0,0,0,calculateCost(w,v,r,c))
