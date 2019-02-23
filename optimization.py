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

    for i in range(len(r)):
        f.write(str(r[i]) + '\t' + str(chord[i]) + '\t' + str(twist[i]) + '\t0.00\t0.00\n')


if __name__ == '__main__':
    runSimulation()
