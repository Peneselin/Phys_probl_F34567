R = 8.314
m = 400e-3
M_Ar = 40e-3
T1 = 300
p1 = 1.00e5
p2 = 1.00e7
i = 3

gamma = (i + 2) / i
nu = m / M_Ar
pressure_ratio = p2 / p1
T2 = T1 * pressure_ratio ** ((gamma - 1) / gamma)
V1_over_V2 = pressure_ratio ** (1 / gamma)
W = -(i / 2) * nu * R * (T2 - T1)

print("Problem 7.103")
print(f"  m = {m * 1e3:.0f} g,  nu = {nu:.2f} mol")
print(f"  gamma = {gamma:.4f}  (monatomic: i = {i})")
print(f"  T1 = {T1} K,  p1 = {p1:.2e} Pa,  p2 = {p2:.2e} Pa")
print(f"  Pressure ratio p2/p1 = {pressure_ratio:.0e}")
print()
print(f"  1) T2 = T1 * (p2/p1)^((gamma-1)/gamma) = {T2:.1f} K")
print(f"  2) V1/V2 = (p2/p1)^(1/gamma) = {V1_over_V2:.2f}")
print(f"  3) W = -(i/2)*nu*R*(T2-T1) = {W:.1f} J  ({W / 1e3:.2f} kJ)")
print(f"     (negative = work done ON the gas during compression)")
