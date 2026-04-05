import numpy as np

hbar = 1.054571817e-34
m_e  = 9.10938e-31
k_B  = 1.380649e-23

L  = 0.1e-6
T1 = 1.0
T2 = 10.0

E1 = np.pi**2 * hbar**2 / (2 * m_e * L**2)

def quantum_number(T):
    n = np.sqrt(k_B * T / E1)
    return max(1, round(n))

def prob_center(n):
    return (2 / L) * np.sin(n * np.pi / 2)**2

n1 = quantum_number(T1)
n2 = quantum_number(T2)

P1 = prob_center(n1)
P2 = prob_center(n2)

print("=" * 50)
print("Задача 17.26")
print("=" * 50)
print(f"E₁ = {E1:.3e} Дж  (перший рівень ями)")
print()
print(f"T₁ = {T1} К  →  n₁ = {n1}")
print(f"  k_B·T₁ = {k_B*T1:.3e} Дж")
print(f"  E_n₁   = {n1**2*E1:.3e} Дж")
print(f"  |ψ(L/2)|² = {P1:.3e} м⁻¹")
print()
print(f"T₂ = {T2} К  →  n₂ = {n2}")
print(f"  k_B·T₂ = {k_B*T2:.3e} Дж")
print(f"  E_n₂   = {n2**2*E1:.3e} Дж")
print(f"  |ψ(L/2)|² = {P2:.3e} м⁻¹")
print()

if P1 == 0:
    print("При n₁ центр ями є вузлом (P=0); після переходу ймовірність зростає.")
else:
    ratio = P2 / P1
    word  = "зросте" if ratio > 1 else "зменшиться"
    print(f"Ймовірність {word} у {ratio:.2e} разів")
