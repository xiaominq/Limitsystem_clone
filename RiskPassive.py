#imports
from dataclasses import field

import RiskMatrix


class RiskPassive:

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

    def setLossPotentialMid(self, value):
        self.lossPotentialMid = value
        return
    def setLossPotentialMin(self, value):
        self.lossPotentialMin = value
        return

    def setLossProbabilityMid(self, value):
        self.lossProbabilityMid = value
        return

    def setLossProbabilityMin(self, value):
        self.lossProbabilityMin = value
        return

    def lossMidCase(self):
        return self.lossPotentialMid/self.lossProbabilityMid

    def lossMinCase(self):
        return self.lossPotentialMin/self.lossProbabilityMin

    def lossRiskReduction(self):
        return (1-self.riskReduction)*self.lossBrutto





