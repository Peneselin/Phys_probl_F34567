hbar = 1.054571817e-34
h    = 6.62607015e-34
c    = 3e8
eV   = 1.6e-19

tau = 1e-8
lam = 600e-9

delta_E = hbar / (2 * tau)

delta_lam = lam**2 / (h * c) * delta_E

print("=" * 50)
print("Задача 17.15")
print("=" * 50)
print(f"τ  = {tau:.1e} с")
print(f"λ  = {lam*1e9:.0f} нм")
print(f"ΔE = {delta_E:.3e} Дж")
print(f"ΔE = {delta_E/eV:.3e} еВ")
print(f"Δλ = {delta_lam:.3e} м")
print(f"Δλ = {delta_lam*1e12:.4f} пм")
