#imports
from dataclasses import field

import RiskMatrix


class Risk:

    def __init__(self, name, category, lossPotentialBrutto, lossPotentialNetto,lossProbabilityBrutto, lossProbabilityNetto,lossPotentialMid, lossPotentialMin,lossProbabilityMid, lossProbabilityMin, riskReduction):
        self.name = name
        self.category = category
        self.lossPotentialBrutto = RiskMatrix.riskPotential(lossPotentialBrutto)
        self.lossPotentialNetto = RiskMatrix.riskPotential(lossPotentialNetto)
        self.lossProbabilityBrutto = RiskMatrix.riskProbability(lossProbabilityBrutto)
        self.lossProbabilityNetto = RiskMatrix.riskProbability(lossProbabilityNetto)
        self.lossPotentialMid = RiskMatrix.riskPotential(lossPotentialMid)
        self.lossProbabilityMid = RiskMatrix.riskProbability(lossProbabilityMid)
        self.lossPotentialMin = RiskMatrix.riskPotential(lossPotentialMin)
        self.lossProbabilityMin = RiskMatrix.riskProbability(lossProbabilityMin)
        self.riskReduction = riskReduction
        self.lossBrutto = self.lossPotentialBrutto/self.lossProbabilityBrutto
        self.lossNetto= self.lossPotentialNetto / self.lossProbabilityNetto
        self.lossMid = self.lossPotentialMid/self.lossProbabilityMid
        self.lossMin = self.lossPotentialMin / self.lossProbabilityMin


    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getLossBrutto(self):
        return self.lossBrutto

    def getLossNetto(self):
        return self.lossBrutto

    def setLossBrutto(self, value):
        self.lossBrutto = value
        return

    def setLossNetto(self, value):
        self.lossBrutto = value
        return

    def setLossMid(self, value):
        self.lossMid = value
        return

    def setLossMin(self, value):
        self.lossMin = value
        return

    def lossMidCase(self):
        return self.lossMid

    def lossMinCase(self):
        return self.lossMin

    def lossRiskReduction(self):
        return (1-self.riskReduction)*self.lossBrutto





