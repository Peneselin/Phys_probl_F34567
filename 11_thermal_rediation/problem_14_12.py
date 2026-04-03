import math

sigma = 5.67e-8
b = 2.898e-3
P = 10e3
lam_max = 700e-9
T = b / lam_max
A = P / (sigma * T**4)

print("Problem 14.12")
print(f"  lambda_max = {lam_max * 1e9:.0f} nm")
print(f"  T = b / lambda_max = {T:.1f} K")
print(f"  P = {P / 1e3:.0f} kW")
print(f"  A = P / (sigma * T^4) = {A:.4e} mВІ  ({A * 1e4:.2f} cmВІ)")
