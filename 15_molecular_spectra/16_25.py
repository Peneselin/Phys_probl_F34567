import math

a0   = 0.529e-10
eV   = 1.6e-19
E1   = -13.6

r_target = 1e-3

n = math.sqrt(r_target / a0)
n_int = round(n)

E_n = E1 / n_int**2

print("=" * 50)
print("Задача 16.25")
print("=" * 50)
print(f"r = {r_target*1e3:.0f} мм = {r_target} м")
print(f"a₀ = {a0:.3e} м")
print(f"n = sqrt(r/a₀) = sqrt({r_target}/{a0:.3e}) = {n:.1f}")
print(f"n ≈ {n_int}")
print(f"E_n = E₁/n² = {E1}/{n_int}² = {E_n:.4e} еВ")
print(f"E_n = {E_n*eV:.4e} Дж")
