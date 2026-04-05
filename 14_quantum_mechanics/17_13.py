hbar = 1.054571817e-34
m_e  = 9.10938e-31
eV   = 1.6e-19

delta_x = 0.10e-9

delta_p = hbar / (2 * delta_x)

T_J  = delta_p**2 / (2 * m_e)
T_eV = T_J / eV

print("=" * 50)
print("Задача 17.13")
print("=" * 50)
print(f"Δx     = {delta_x*1e9:.2f} нм")
print(f"Δp_min = {delta_p:.3e} кг·м/с")
print(f"T_min  = {T_J:.3e} Дж")
print(f"T_min  = {T_eV:.3f} еВ")
