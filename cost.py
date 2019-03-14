from math import exp
from curves import getPropellerArray
from simulation import runSimulation
from writeInput import writeInput

L = 0.257 # propeller's length

def computeI(r,c):
    # r and c are the radius and chord arrays given to the simulation
    # you can give them by hand or use the return values of 'getPropellerArray'
    samples = len(r)

    f = lambda r,c: c * r**2

    sum1toN_1 = 0
    for i in range(1,samples-1):
        sum1toN_1 += 2*f(r[i],c[i])

    I = L * ( f(r[0], c[0]) + f(r[samples-1], c[samples-1]) + sum1toN_1 ) / (2*samples)

    return I

def calculateCost(omega,vel,r,c):
    # omega is the terminal angular velocity returned by 'runSimulation'
    # vel is the linear terminal velocity returned by 'runSimulation'
    # r and c are the radius and chord arrays given to the simulation

    VelCost = lambda v : exp(-9/(v-12.5)**2)

    I = computeI(r,c)

    BladeCost = 10*(I*omega+VelCost(vel))

    return BladeCost

def cost(x):
    # input: bezier control points in an array
    # output: propeller's cost

    y1,y2,y3,y4,t1,t2,t3 = x
    r, c, t = getPropellerArray(y1,y2,y3,y4,t1,t2,t3,L)
    writeInput(r,c,t)
    w, v = runSimulation()

    return calculateCost(w,v,r,c)
