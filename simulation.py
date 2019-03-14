from subprocess import PIPE, Popen

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
