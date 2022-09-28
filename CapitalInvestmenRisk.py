from abc import ABC
from Risk import RiskInterface


class CapitalInvestmentRisk(RiskInterface, ABC):

    def __init__(self, name, category, loss):
        self.name = name
        self.category = category
        self.loss = loss

    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getLossBrutto(self):
        return self.loss

    def getLossNetto(self):
        return self.loss

    def setLoss(self, value):
        self.loss = value
        return

    def setLossBrutto(self, value):
        self.setLoss(value)
        return

    def setLossNetto(self, value):
        self.setLoss(value)
        return

    def setLossMid(self, value):
        self.setLoss(value)
        return

    def setLossMin(self, value):
        self.setLoss(value)
        return

    def lossMidCase(self):
        return self.loss

    def lossMinCase(self):
        return self.loss

    def lossRiskReduction(self):
        return self.loss
