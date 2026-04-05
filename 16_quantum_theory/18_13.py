import math

hbar  = 1.054571817e-34
m_e   = 9.10938e-31
eV    = 1.6e-19
N_A   = 6.022e23

rho   = 10.5e3
M     = 0.108

n = rho / M * N_A

E_F = hbar**2 / (2 * m_e) * (3 * math.pi**2 * n)**(2/3)

E_avg = 3/5 * E_F

P = 2/3 * n * E_avg

print("=" * 50)
print("Задача 18.13")
print("=" * 50)
print(f"ρ = {rho:.2e} кг/м³,  M = {M} кг/моль")
print(f"n = {n:.3e} м⁻³  (концентрація електронів)")
print()
print(f"1) E_F = {E_F:.3e} Дж = {E_F/eV:.2f} еВ")
print(f"2) <E> = 3/5·E_F = {E_avg:.3e} Дж = {E_avg/eV:.2f} еВ")
print(f"3) P   = 2/3·n·<E> = {P:.3e} Па = {P/1e9:.2f} ГПа")
