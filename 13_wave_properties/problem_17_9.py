h = 6.626e-34
e = 1.6e-19
r = 10.0e-3
B = 2.00e-3
q = 2 * e
p = q * B * r
lam = h / p
print("Problem 17.9 вЂ“ de Broglie wavelength of an alpha particle in a magnetic field")
print(f"  r = {r * 1e3:.1f} mm,  B = {B * 1e3:.2f} mT")
print(f"  q = 2e = {q:.3e} C")
print(f"  Momentum p = q*B*r = {p:.4e} kgВ·m/s")
print(f"  lambda = h/p = {lam:.4e} m  ({lam * 1e10:.3f} Г…)  ({lam * 1e9:.4f} nm)")
