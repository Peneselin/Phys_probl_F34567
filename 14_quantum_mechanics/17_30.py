import numpy as np

hbar = 1.054571817e-34
m_e  = 9.10938e-31
eV   = 1.6e-19

U0_eV = 11.0
E_eV  = 10.0

U0 = U0_eV * eV
E  = E_eV  * eV

kappa = np.sqrt(2 * m_e * (U0 - E)) / hbar

sinh_val = np.sqrt(4 * E * (U0 - E) / U0**2)
kappa_L  = np.arcsinh(sinh_val)
L        = kappa_L / kappa

T_check = 1 / (1 + U0**2 * np.sinh(kappa * L)**2 / (4 * E * (U0 - E)))

print("=" * 50)
print("Задача *17.30")
print("=" * 50)
print(f"E      = {E_eV} еВ")
print(f"U₀     = {U0_eV} еВ")
print(f"U₀ - E = {U0_eV - E_eV} еВ")
print()
print(f"κ      = sqrt(2m(U₀−E)) / ħ = {kappa:.4e} м⁻¹")
print(f"sinh(κL) = {sinh_val:.4f}")
print(f"κL     = arcsinh({sinh_val:.4f}) = {kappa_L:.4f}")
print()
print(f"L = κL / κ = {L:.4e} м")
print(f"L = {L*1e10:.4f} Å")
print()
print(f"Перевірка: T = {T_check:.4f}  (має бути 0.5000)")
