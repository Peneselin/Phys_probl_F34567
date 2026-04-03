import math

R = 8.314
theta_E = 300
T = 3
x = theta_E / T
ex = math.exp(x)

C_V = 3 * R * x**2 * ex / (ex - 1) ** 2

print("Problem 18.2")
print(f"  theta_E = {theta_E} K,  T = {T} K  =>  theta_E/T = {x:.0f}")
print(f"  C_V = 3R*(theta/T)^2 * exp(theta/T)/(exp(theta/T)-1)^2")
print(f"  C_V = {C_V:.4e} J/(molВ·K)")
print(f"  (This is essentially zero quantum freeze-out at T << theta_E)")
