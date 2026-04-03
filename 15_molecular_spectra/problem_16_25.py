import math

a0 = 0.0529e-9
r = 1e-3
E_ion = 13.6
e_ = 1.6e-19
n = math.sqrt(r / a0)
En = -E_ion / n**2

print("Problem 16.25")
print(f"  Target radius r = {r * 1e3:.0f} mm")
print(f"  Bohr radius a0 = {a0 * 1e9:.4f} nm")
print(f"  n = sqrt(r/a0) = sqrt({r / a0:.3e}) = {n:.1f}")
print(f"  Energy E_n = -13.6/n^2 = {En:.4e} eV  ({En * e_:.4e} J)")
