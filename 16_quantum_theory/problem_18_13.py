import math

hbar = 1.0546e-34
m_e = 9.11e-31
e_ = 1.6e-19
N_A = 6.022e23
rho = 10.5e3
M = 0.108
n = rho * N_A / M
E_F = (hbar**2 / (2 * m_e)) * (3 * math.pi**2 * n) ** (2 / 3)
E_avg = (3 / 5) * E_F
P = (2 / 3) * n * E_avg

print("Problem 18.13")
print(f"  rho = {rho:.2e} kg/m^3,  M = {M * 1e3:.0f} g/mol")
print(f"  Electron density n = rho*N_A/M = {n:.4e} m^-3")
print(f"  1) Fermi energy E_F = {E_F:.4e} J  ({E_F / e_:.2f} eV)")
print(f"  2) Average energy E_avg = (3/5)*E_F = {E_avg:.4e} J  ({E_avg / e_:.2f} eV)")
print(f"  3) Electron gas pressure P = (2/3)*n*E_avg = {P:.4e} Pa  ({P / 1e9:.2f} GPa)")
