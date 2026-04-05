import math

k_B    = 1.380649e-23
eV     = 1.6e-19

m_ratio = 10.0
dT      = 100.0

delta_E_g = 0.0

delta_mu = (3/4) * k_B * dT * math.log(m_ratio)

print("=" * 50)
print("Задача *18.21")
print("=" * 50)
print(f"m_h/m_e = {m_ratio},  ΔT = {dT} К")
print()
print("Рівень Фермі невиродженого напівпровідника:")
print("  μ = E_g/2 + (3/4)·k_B·T·ln(m_h/m_e)")
print()
print(f"Зсув при ΔT = {dT} К:")
print(f"  Δμ = (3/4)·k_B·ΔT·ln(m_h/m_e)")
print(f"  Δμ = {delta_mu:.4e} Дж")
print(f"  Δμ = {delta_mu/eV:.4f} еВ")
print(f"  Δμ = {delta_mu/eV*1000:.2f} меВ")
print()
print("Рівень Фермі зміщується вгору (до зони провідності),")
print("оскільки m_h > m_e.")
