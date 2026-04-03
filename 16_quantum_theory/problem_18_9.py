import math

R = 8.314
theta_D = 350
T = 20
C_V = (12 * math.pi**4 / 5) * R * (T / theta_D) ** 3
print("Problem 18.9")
print(f"  theta_D = {theta_D} K,  T = {T} K")
print(f"  T/theta_D = {T / theta_D:.4f}  (<<1, Debye T^3 law applies)")
print(f"  C_V = (12*pi^4/5)*R*(T/theta_D)^3")
print(f"  C_V = {C_V:.4f} J/(molВ·K)")
