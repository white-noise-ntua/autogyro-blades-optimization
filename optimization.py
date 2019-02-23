from subprocess import PIPE, Popen

L = 0.257 # length of helix

def runSimulation():
    command = "timeout 10s wine aero_static.exe || [ $? -eq 124 ] && echo TIMEOUT_ERROR"
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()

    if out.decode("utf-8")=="TIMEOUT_ERROR\n":
        print("error")
        return -1

    terminalAngularVelocity = float(str(out.decode("utf-8")).split('\n')[-4].split()[5])

    return terminalAngularVelocity


def inputFileIntro(numberOfPoints):
    result = "-- Input geometry blade\n"
    result += str(numberOfPoints)
    result += "    ! NSPANB\n"
    result += "  r     chord    twist    xaer    zaer\n"

    return result


def writeInput(r,chord,twist):
    f = open("geomb.inp","w")

    f.write(inputFileIntro(len(r)))

    for i in range(len(r)):
        f.write(str(r[i]) + '\t' + str(chord[i]) + '\t' + str(twist[i]) + '\t0.00\t0.00\n')


def computeI(r,c):
    samples = len(r)

    f = lambda r,c: c * r**2

    sum1toN_1 = 0
    for i in range(1,samples-1):
        sum1toN_1 += 2*f(r[i],c[i])

    I = L * ( f(r[0], c[0]) + f(r[samples-1], c[samples-1]) + sum1toN_1 ) / (2*samples)

    return I
