hbar = 1.0546e-34
m_e = 9.11e-31
e = 1.6e-19
dx = 0.10e-9
dp = hbar / dx
E_min = dp**2 / (2 * m_e)

print("Problem 17.13")
print(f"  Delta_x = {dx * 1e9:.2f} nm")
print(f"  Delta_p_min = hbar / Delta_x = {dp:.4e} kgВ·m/s")
print(f"  E_min = (Delta_p)^2 / (2*m_e) = {E_min:.4e} J  ({E_min / e:.2f} eV)")
