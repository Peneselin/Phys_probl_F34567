h = 6.626e-34
c = 3e8
e = 1.6e-19
lam = 380e-9
E = h * c / lam
m = E / c**2
p = h / lam

print("Problem 15.35")
print(f"  lambda = {lam * 1e9:.0f} nm")
print(f"  Energy:   E = h*c/lambda = {E:.4e} J  ({E / e:.2f} eV)")
print(f"  Mass:     m = E/c^2      = {m:.4e} kg")
print(f"  Momentum: p = h/lambda   = {p:.4e} kgВ·m/s")
