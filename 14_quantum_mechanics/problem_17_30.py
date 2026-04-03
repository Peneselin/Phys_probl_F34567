import math

hbar = 1.0546e-34
m_e = 9.11e-31
e = 1.6e-19
V = 10.0
U0 = 11.0
E = V
kappa = math.sqrt(2 * m_e * (U0 - E) * e) / hbar
rhs = 2 * math.sqrt(E * (U0 - E)) / U0
kL = math.asinh(rhs)
L = kL / kappa

print("Problem *17.30")
print(f"  Electron energy E = {E:.1f} eV")
print(f"  Barrier height U0 = {U0:.1f} eV")
print(f"  U0 - E = {U0 - E:.1f} eV")
print(f"  kappa = sqrt(2*m_e*(U0-E)) / hbar = {kappa:.4e} m^-1")
print()
print(f"  T = 0.5 condition: sinh(kappa*L) = 2*sqrt(E*(U0-E))/U0 = {rhs:.4f}")
print(f"  kappa*L = arcsinh({rhs:.4f}) = {kL:.4f}")
print(f"  L = kappa*L / kappa = {L:.4e} m  ({L * 1e10:.3f} Г…)  ({L * 1e9:.4f} nm)")
