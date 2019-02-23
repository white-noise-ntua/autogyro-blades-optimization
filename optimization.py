from subprocess import PIPE, Popen


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
    round_ = lambda x: float("{0:.5f}".format(x))

    r = list(map(round_,r))
    chord = list(map(round_,chord))
    twist = list(map(round_,twist))

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


def chordBezier(y1,y2,y3,y4,t,L):
    c = (1-t)**3 * y1 + 3 * (1-t)**2 * t * y2 + 3 * (1-t) * t**2 * y3 + t**3 * y4
    r = (t**3 + (1-t)**2 * t + 2*(1-t) * t**2) * L

    return c,r

def twistBezier(f1,f2,f3,r,L):
    t = r/L

    f = (1-t)**2 * f1 + 2*(1-t)*t*f2 + t**2 * f3

    return f

def getPropellerArray(y1,y2,y3,y4,f1,f2,f3,L):
    radius = []
    chord = []
    twist = []

    for i in range(10):
        t = 1/9 * i
        c,r = chordBezier(y1,y2,y3,y4,t,L)
        radius.append(r)
        chord.append(c)
        twist.append(twistBezier(f1,f2,f3,r,L))

    return radius,chord,twist


if __name__ == '__main__':
    L = 0.257 # propeller's length
    r,c,t = getPropellerArray(0.05,0.045,0.035,0.02,25,25,25,L)
    writeInput(r,c,t)
    print(runSimulation())
