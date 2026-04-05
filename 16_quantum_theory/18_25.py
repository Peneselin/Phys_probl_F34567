import math

k_B   = 1.380649e-23
eV    = 1.6e-19

delta_E = 0.66 * eV
T       = 300.0

alpha = -delta_E / (2 * k_B * T**2)

print("=" * 50)
print("Задача 18.25")
print("=" * 50)
print(f"ΔE = 0.66 еВ,  T = {T} К")
print(f"ΔE/(2k_B) = {delta_E/(2*k_B):.2f} К")
print()
print(f"σ ~ exp(-ΔE/2k_BT)  →  α = d(ln σ)/dT = -ΔE/(2k_BT²)")
print(f"α = {alpha:.4f} К⁻¹")
print(f"α = {alpha:.3e} К⁻¹")
