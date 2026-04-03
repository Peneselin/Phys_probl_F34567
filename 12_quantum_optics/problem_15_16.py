h = 6.626e-34
e = 1.6e-19
nu0 = 6e14
V0 = 3
A = h * nu0
nu = nu0 + e * V0 / h
A_eV = A / e
nu_eV_equiv = h * nu / e

print("Problem 15.16")
print(f"  Stopping potential V0 = {V0} V")
print(f"  Threshold frequency nu0 = {nu0:.2e} Hz")
print(f"  Work function A = h*nu0 = {A:.4e} J  ({A_eV:.3f} eV)")
print(f"  Light frequency nu = nu0 + e*V0/h = {nu:.4e} Hz")
print(f"  Photon energy E = h*nu = {h * nu:.4e} J  ({nu_eV_equiv:.2f} eV)")
