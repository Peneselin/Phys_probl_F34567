import math

R      = 8.314
T      = 3.0
T_E    = 300.0

x = T_E / T
ex = math.exp(x)

C = 3 * R * x**2 * ex / (ex - 1)**2

print("=" * 50)
print("Задача 18.2")
print("=" * 50)
print(f"T   = {T} К,  T_E = {T_E} К")
print(f"x   = T_E/T = {x:.2f}")
print(f"C   = 3R·x²·eˣ/(eˣ−1)² = {C:.4e} Дж/(моль·К)")
