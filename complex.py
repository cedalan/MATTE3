import numpy as np
import matplotlib.pyplot as plt
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
        return f"$z = {real} {sign} {abs(imag)}i$"
    
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
    
    def plot_roots(self, roots: List[Complex]) -> None:
        if len(roots) == 0:
            return
        
        r = roots[0].radius
        root_circle_angles = np.linspace(0, 2 * np.pi, 100)

        xs = r * np.cos(root_circle_angles)
        ys = r * np.sin(root_circle_angles)

        plt.figure(figsize=(8, 8))
        plt.scatter(self.real, self.imag, label=self, color="black", zorder=5)
        plt.plot(xs, ys)

        for root in roots:
            plt.scatter(root.real, root.imag, label=root, color="red", zorder=5)
            plt.annotate(f"{root}", xy=(root.real, root.imag), xytext=(10, 10), 
             textcoords='offset points', ha='left', va='bottom',
             arrowprops=dict(arrowstyle='-', color='gray', lw=0.5))

        plt.grid(zorder=0)
        plt.axis('equal')
        plt.xlabel("Real axis")
        plt.ylabel("Imaginary axis")
        plt.legend()
        plt.show()
    
    @classmethod
    def from_polar(cls, radius: float, theta: float, tol: float = 1e-14) -> Complex:
        real = radius * np.cos(theta)
        imag = radius * np.sin(theta)
        if abs(real) < tol:
            real = 0
        if abs(imag) < tol:
            imag = 0

        return cls(real, imag)
    
my_num = Complex(1, 2)
my_num_roots = my_num.calculate_roots(3)

my_num.plot_roots(my_num_roots)