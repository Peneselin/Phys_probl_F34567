import math

T_min = 260
T_max = 520
eta = 1 - T_min * math.log(T_max / T_min) / (T_max - T_min)

print("Problem 7.15")
print(f"  T_min = {T_min} K,  T_max = {T_max} K")
print(f"  Cycle: 1в†’2 isochoric, 2в†’3 adiabatic, 3в†’1 isothermal")
print(f"  eta = 1 - T_min * ln(T_max/T_min) / (T_max - T_min)")
print(f"  eta = {eta:.4f}  ({eta * 100:.2f} %)")
