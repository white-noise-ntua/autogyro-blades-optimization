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
    # we offset all R values by 0.07 for simulation needs
    addRROOT = lambda x : x+0.07

    r = list(map(addRROOT,r))
    r = list(map(round_,r))
    chord = list(map(round_,chord))
    twist = list(map(round_,twist))

    for i in range(len(r)):
        f.write(str(r[i]) + '\t' + str(chord[i]) + '\t' + str(twist[i]) + '\t0.00\t0.00\n')
