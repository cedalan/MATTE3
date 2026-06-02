import numpy as np
from typing import List

class Complex:
    def __init__(self, a: float, b: float, decimal_rounding: int = 3) -> None:
        self.real = a
        self.imag = b
        self.radius, self.theta = self._to_polar()

        self.decimal_rounding = decimal_rounding
    
    def __repr__(self) -> str:
        return f"Complex({self.real}, {self.imag})"
    
    def __str__(self) -> str:
        real, imag = self.real, self.imag

        if imag == 0:
            return f"z = {real}"
        if real == 0:
            return f"z = {imag}i"
        
        sign = "+" if imag > 0 else "-"

        real = np.round(real, self.decimal_rounding)
        imag = np.round(imag, self.decimal_rounding)
        return f"z = {real} {sign} {abs(imag)}i"
    
    def _to_polar(self):
        radius = np.sqrt(self.real**2 + self.imag**2)
        theta = np.arctan2(self.imag, self.real)
        return radius, theta
    
    def calculate_roots(self, degree: int) -> List[Complex]:
        root_radius = np.power(self.radius, 1 / degree)
        principal_theta = self.theta / degree
        
        roots = []
        for k in range(degree):
            theta = principal_theta + 2 * k * np.pi / degree
            roots.append(Complex.from_polar(root_radius, theta))
        return roots
    
    @classmethod
    def from_polar(cls, radius: float, theta: float, tol: float = 1e-14) -> Complex:
        real = radius * np.cos(theta)
        imag = radius * np.sin(theta)
        if abs(real) < tol:
            real = 0
        if abs(imag) < tol:
            imag = 0

        return cls(real, imag)