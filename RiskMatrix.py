
riskPotential = {
    0 : 0,
    1 : 0.1,
    2 : 1,
    3 : 10,
    4 : 50,
    5 : 200
}

riskProbability = {
    0 : 200,
    1 : 20,
    2 : 10,
    3 : 5,
    4 : 2,
    5 : 1
}

def scaleProb2Value(s :int):
    return riskProbability[s]

def scalePot2Value(s :int):
    return riskPotential[s]
