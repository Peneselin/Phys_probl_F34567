import math

e    = 1.6e-19
m_e  = 9.10938e-31
hbar = 1.054571817e-34
a0   = 0.529e-10

v1 = e**2 / (4 * math.pi * 8.854e-12 * hbar)

T = 2 * math.pi * a0 / v1

I = e / T

print("=" * 50)
print("Задача 17.43")
print("=" * 50)
print(f"a₀ = {a0:.3e} м")
print(f"v₁ = {v1:.3e} м/с")
print(f"T  = 2πa₀/v₁ = {T:.3e} с")
print(f"I  = e/T = {I:.3e} А")
print(f"I  = {I*1e3:.4f} мА")
