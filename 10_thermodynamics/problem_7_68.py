R = 8.314
m = 14e-3
M = 28e-3
T = 300
i = 5
nu = m / M
U = (i / 2) * nu * R * T

print("Problem 7.68")
print(f"  Mass m = {m * 1e3:.0f} g,  Molar mass M = {M * 1e3:.0f} g/mol")
print(f"  nu = m/M = {nu:.3f} mol")
print(f"  Degrees of freedom i = {i}")
print(f"  T = {T} K")
print(f"  U = (i/2) * nu * R * T = {U:.1f} J  ({U / 1e3:.3f} kJ)")
