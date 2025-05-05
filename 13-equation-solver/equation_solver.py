from abc import ABC

class Equation(ABC):
    
    def solve(self):
        pass
    
    def analyze(self):
        pass
    
class LinearEquation(Equation):
    pass


eq = Equation()
lin_eq = LinearEquation()