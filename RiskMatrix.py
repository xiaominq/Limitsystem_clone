

riskPotential = {
    0 : 1,
    1 : 1,
    2 : 1,
    3 : 4,
    4 : 4,
    5 : 8
}

riskProbability = {
    0 : 1,
    1 : 1,
    2 : 1,
    3 : 4,
    4 : 4,
    5 : 8
}

def scaleProb2Value(s:int):
    return riskProbability[s]

def scalePot2Value(s:int):
    return riskPotential[s]