import math

c = 3e8
E = 10
tau = 0.13e-3
d = 10e-6
R = 0.5
P = E / tau
A = math.pi * (d / 2) ** 2
I = P / A
pressure = (1 + R) * I / c

print("Problem 15.28")
print(f"  Energy E = {E} J,  pulse duration tau = {tau * 1e3:.2f} ms")
print(f"  Spot diameter d = {d * 1e6:.0f} Вµm  => area A = {A:.4e} mВІ")
print(f"  Power P = E/tau = {P:.2f} W")
print(f"  Intensity I = P/A = {I:.3e} W/mВІ")
print(f"  Reflectance R = {R}")
print(f"  Pressure p = (1+R)*I/c = {pressure:.3e} Pa  ({pressure / 1e6:.3f} MPa)")
