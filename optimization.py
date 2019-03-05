from subprocess import PIPE, Popen
from curves import getPropellerArray
from writeInput import writeInput


def runSimulation():
    command = "timeout 10s ./blades.out || [ $? -eq 124 ] && echo TIMEOUT_ERROR"
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()

    if out.decode("utf-8")=="TIMEOUT_ERROR\n":
        print("error")
        return -1


    lastLine = str(out.decode("utf-8")).split('\n')[-4].split()
    terminalAngularVelocity = float(lastLine[5])
    terminalVelocity = float(lastLine[7])

    return terminalAngularVelocity, terminalVelocity


def computeI(r,c):
    samples = len(r)

    f = lambda r,c: c * r**2

    sum1toN_1 = 0
    for i in range(1,samples-1):
        sum1toN_1 += 2*f(r[i],c[i])

    I = L * ( f(r[0], c[0]) + f(r[samples-1], c[samples-1]) + sum1toN_1 ) / (2*samples)

    return I


if __name__ == '__main__':
    L = 0.257 # propeller's length
    r,c,t = getPropellerArray(0.05,0.045,0.035,0.02,25,25,25,L)
    writeInput(r,c,t)
    print(runSimulation())
