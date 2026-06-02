import numpy as np

class Complex:
    def __init__(self, a: float, b: float) -> None:
        self.real = a
        self.imag = b
    
    def __repr__(self) -> str:
        return f"Complex({self.real}, {self.imag})"
    
    def __str__(self) -> str:
        real, imag = self.real, self.imag

        if imag == 0:
            return f"z = {real}"
        if real == 0:
            return f"z = {imag}i"
        
        sign = "+" if abs(imag) > 0 else "-"
        return f"z = {real} {sign} {imag}i"
    
    @classmethod
    def from_polar(cls, radius: float, theta: float, tol: float = 1e-14) -> Complex:
        real = radius * np.cos(theta)
        imag = radius * np.sin(theta)
        if real < tol:
            real = 0
        if imag < tol:
            imag = 0
        return cls(real, imag)
