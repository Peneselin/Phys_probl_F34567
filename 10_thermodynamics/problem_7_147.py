import math

R = 8.314
nu = 1.0
T1 = 580
T2 = 290
V_ratio = 10
gamma = 7 / 5

eta = 1 - T2 / T1
adiabatic_ratio = (T1 / T2) ** (1 / (gamma - 1))
x = V_ratio / adiabatic_ratio
Q1 = nu * R * T1 * math.log(x)
W = eta * Q1

print("Problem 7.147")
print(f"  T1 = {T1} K,  T2 = {T2} K")
print(f"  V_max/V_min = {V_ratio}")
print(f"  gamma = {gamma}  (diatomic)")
print()
print(f"  Adiabatic volume ratio (T1/T2)^(1/(gamma-1)) = {adiabatic_ratio:.3f}")
print(f"  Isothermal expansion ratio x = V2/V1 = {x:.4f}")
print()
print(f"  1) Q1 = nu*R*T1*ln(x) = {Q1:.1f} J  ({Q1 / 1e3:.3f} kJ)")
print(f"  2) W  = eta * Q1      = {W:.1f} J  ({W / 1e3:.3f} kJ)")
print(f"  3) eta = 1 - T2/T1   = {eta:.2f}  ({eta * 100:.1f} %)")
