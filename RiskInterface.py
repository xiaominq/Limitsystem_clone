from abc import ABC, abstractmethod

class RiskInterface:

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
    def setLossMin(self, value):
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