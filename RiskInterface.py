from abc import ABC, abstractmethod

class RiskInterface:

    @abstractmethod
    def getName(self):
        return self.name

    @abstractmethod
    def getCategory(self):
        return self.category

    @abstractmethod
    def getLossBrutto(self):
        return self.lossBrutto

    @abstractmethod
    def getLossNetto(self):
        pass

    @abstractmethod
    def setLossBrutto(self, value):
        pass

    @abstractmethod
    def setLossNetto(self, value):
        pass

    @abstractmethod
    def setLossMid(self, value):
        pass

    @abstractmethod
    def setLossNMin(self, value):
        pass

    @abstractmethod
    def lossMidCase(self):
        pass

    @abstractmethod
    def lossMinCase(self):
        pass

    @abstractmethod
    def lossRiskReduction(self):
        pass