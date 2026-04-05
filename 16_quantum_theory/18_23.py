import math

k_B   = 1.380649e-23
eV    = 1.6e-19

delta_E = 0.5 * eV
T1      = 300.0
T2      = 350.0

exp1 = math.exp(delta_E / (2 * k_B * T1))
exp2 = math.exp(delta_E / (2 * k_B * T2))

ratio_sigma = exp1 / exp2
ratio_R     = 1 / ratio_sigma

print("=" * 50)
print("Задача 18.23")
print("=" * 50)
print(f"ΔE = {delta_E/eV} еВ,  T₁ = {T1} К,  T₂ = {T2} К")
print(f"ΔE/(2k_B·T₁) = {delta_E/(2*k_B*T1):.3f}")
print(f"ΔE/(2k_B·T₂) = {delta_E/(2*k_B*T2):.3f}")
print()
print(f"σ ~ exp(-ΔE/2k_BT)")
print(f"R₁/R₂ = σ₂/σ₁ = exp[ΔE/2k_B·(1/T₁−1/T₂)]")
print(f"R₁/R₂ = {ratio_R:.2f}")
print(f"Опір зменшиться у {1/ratio_R:.2f} разів")
