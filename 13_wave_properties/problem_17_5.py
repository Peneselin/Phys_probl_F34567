import math

h = 6.626e-34
m_p = 1.67e-27
e = 1.6e-19
energies = [
    ("1.00 eV", 1.00 * e),
    ("1.00 keV", 1.00e3 * e),
]

print("Problem 17.5")
print(f"  lambda = h / sqrt(2 * m_p * E)")
print()

for label, E in energies:
    lam = h / math.sqrt(2 * m_p * E)
    print(f"  E = {label}:  lambda = {lam:.4e} m  ({lam * 1e12:.2f} pm)")
