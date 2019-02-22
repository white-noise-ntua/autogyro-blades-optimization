from subprocess import PIPE, Popen

f = open("geomb.inp","r")
lines = [ _ for _ in f ]
#data = [list(map(float,x.split())) for x in lines[3:-1]]
intro = lines[:3]


def runSimulation():
    command = "timeout 5s wine aero_static.exe || [ $? -eq 124 ] && echo TIMEOUT_ERROR"
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()

    if out.decode("utf-8")=="TIMEOUT_ERROR\n":
        print("error")
        return -1

    terminalAngularVelocity = float(str(out.decode("utf-8")).split('\n')[-4].split()[5])

    return terminalAngularVelocity

if __name__ == '__main__':
    runSimulation()
