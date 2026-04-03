import math

k_B = 1.38e-23
e_ = 1.6e-19
delta_T = 100
mass_ratio = 10

delta_E_F = (3 / 4) * k_B * delta_T * math.log(mass_ratio)
delta_E_F_eV = delta_E_F / e_

print("Problem *18.21")
print(f"  m_h*/m_e* = {mass_ratio}")
print(f"  Delta_T = {delta_T} K")
print(f"  E_F = E_gap_centre + (3/4)*k_B*T*ln(m_h*/m_e*)")
print(f"  Delta_E_F = (3/4)*k_B*Delta_T*ln(m_h*/m_e*)")
print(f"  Delta_E_F = {delta_E_F:.4e} J  =  {delta_E_F_eV * 1e3:.2f} meV")
print(f"  Direction: upward (towards conduction band), since m_h* > m_e*")
