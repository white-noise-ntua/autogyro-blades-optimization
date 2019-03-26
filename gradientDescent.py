from cost import cost
from scipy import signal
import numpy as np

chordEpsilon = 0.01/100
twistEpsilon = 1/200

epsilon = np.array([
        chordEpsilon,
        chordEpsilon,
        chordEpsilon,
        chordEpsilon,
        twistEpsilon,
        twistEpsilon,
        twistEpsilon
        ])

def gradientDescent(x,currentCost,startingOmega,startingVel,steps):
    outputFile = open("tests.txt","w+")
    outputFile.write("New optimization\n Blade | Cost | Omega | Velocity:\n")

    newX, newCost = x, currentCost
    print("Starting optimization.\nStarting Blade: {}.\nStarting Cost = {}".format(x,currCost))
    outputFile.write("{}\n{}\n{}\n{}\n".format(newX,newCost,startingOmega,startingVel))

    for i in range(steps):
        newX, newCost, omega, velocity = gradientStep(newX,newCost)
        print("Step {} is done.\n".format(i+1))
        print("Cost: {}\nOmega: {}\n Velocity: {}\n".format(newCost,omega,velocity))
        print("New blade: {}\n\n".format(newX))
        outputFile.write("{}\nNew cost: {}\nOmega: {}\nVelocity: {}\n".format(newX,newCost,omega,velocity))

    return newX,newCost

def gradientStep(x,currentCost):
    # x = [y1, y2, y3, y4, t1, t2, t3]
    x = np.array(x)
    step = 10*epsilon

    grad = computeGradient(x,currentCost,'flat')
    print("Grad: ",grad)

    normalizedGrad = np.divide(grad,abs(grad))
    print("Normalized Grad: ",normalizedGrad)

    newX = proj(x - np.multiply(step,normalizedGrad))

    newCost, omega, vel = cost(newX)

    return newX, newCost, omega, vel

def computeGradient(x,currentCost,twistMode):
    newCosts = np.zeros(7)

    if twistMode == 'flat':
        coordinates = 4
        delta = np.array([0,0,0,0,1,1,1])
        twistCost,_,_ = cost(x+np.multiply(epsilon,delta))
        newCosts[4]=newCosts[5]=newCosts[6]=twistCost

    for i in range(coordinates):
        newCosts[i],_,_ = cost(x+np.multiply(epsilon,signal.unit_impulse(7,i)))

    gradient = np.divide(newCosts-currentCost,epsilon)

    return gradient

chordLowLimit = 0.02
chordHiLimit = 0.04
twistLowLimit = 5
twistHiLimit = 30

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
    inputFile = open("startingBlade.txt","r")
    coordinates = 7

    startingBlade = list(map(float,inputFile.readline().split(",")))
    currCost,startingOmega,startingVel = cost(startingBlade)
    newX, newCost = gradientDescent(
                        startingBlade,
                        currCost,
                        startingOmega,
                        startingVel,
                        50
                    )
