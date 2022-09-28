import Risk
from RiskInterface import RiskInterface


class SubDevidedRisk(Risk, RiskInterface):

    def __init__(self, name):
        self.subrisks = list()

    def Add(self, risk:Risk):
        self.subrisks.append()
        return

    def getSubrisks(self):
        return self.subrisks

    def getNameSubrisks(self):
        names = list()
        for sr in self.subrisks:
            names.append(sr.getName())
        return names

    def lossMidCase(self):
        loss = 0
        for sr in self.subrisks:
            loss += self.lossMidCase()
        return loss

    def lossMinCase(self):
        loss = 0
        for sr in self.subrisks:
            loss += self.lossMinCase()
        return loss


    def lossRiskReduction(self):
        loss = 0
        for sr in self.subrisks:
            loss += self.lossRiskReduction()
        return loss
