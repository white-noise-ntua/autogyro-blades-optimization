from simulation import runSimulation
from cost import calculateCost
from writeInput import writeInput
from curves import getPropellerArray

chordEpsilon = 0.04/100
twistEpsilon = 0.6
L = 0.257 # propeller's length

def gradientStep(y1,y2,y3,y4,t1,t2,t3,currentCost):

    # Computing cost's partial derivative with respect to y1

    #calculate cost at y1+chordEpsilon
    r, c, t = getPropellerArray(y1+chordEpsilon,y2,y3,y4,t1,t2,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()
    newCost = calculateCost(w,v,r,c)

    grad_y1 =  (newCost - currentCost) / chordEpsilon

    print(currentCost)
    print(newCost)
    print(grad_y1)

if __name__ == '__main__':
    r,c,t = getPropellerArray(0.5,0.45,0.35,0.25,0,0,0,L)
    writeInput(r,c,t)
    w,v = runSimulation()
    gradientStep(0.5,0.45,0.35,0.25,0,0,0,calculateCost(w,v,r,c))
