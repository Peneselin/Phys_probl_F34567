import math

R     = 8.314
T     = 20.0
T_D   = 350.0

C = 12 * math.pi**4 / 5 * R * (T / T_D)**3

print("=" * 50)
print("Задача 18.9")
print("=" * 50)
print(f"T   = {T} К,  Θ_D = {T_D} К")
print(f"T/Θ_D = {T/T_D:.4f}  (T << Θ_D → закон Дебая T³)")
print(f"C = (12π⁴/5)·R·(T/Θ_D)³ = {C:.4f} Дж/(моль·К)")
