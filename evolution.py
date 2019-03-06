from Simulation import runSimulation
from curves import getPropellerArray
from writeInput import writeInput
import numpy as np

def evaluate(params):
    # Run Simulation
    L = 0.257 # propeller's length
    r,c,t = getPropellerArray(params[0],params[1],params[2],params[3],params[4],params[5],params[6],L)
    writeInput(r,c,t)
    rpm, vel = runSimulation()

    #Calculate cost
    return #cost


def runEvolution(numGen = 10, popSize = 10):
    # Init population
    #population = []
    #for _ in range(popSize):
    #    c = (np.random.normal(0, 0.1, 7) , 0.0)
    #    population.append(c)

    population = [(np.random.normal(0, 0.1, 7) , 0.0) for _ in range(popSize)]

    print(population)

    for _ in range(numGen):
        for creature in population:
            creature[1] = evaluate(creature[0])

        # Sort based on creature[1]

        # Print stats

        # Dump part of the population

        # Create offsping based on mutations



    # Save the best creature

    return


if __name__ == '__main__':
    runEvolution()
