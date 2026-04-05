h  = 6.62607015e-34
c  = 3e8
eV = 1.6e-19

lam = 486e-9

E_photon = h * c / lam

print("=" * 50)
print("Задача 16.14")
print("=" * 50)
print(f"λ = {lam*1e9:.0f} нм  (лінія Hβ серії Бальмера, перехід n=4→2)")
print(f"E_фотона = hc/λ = {E_photon:.3e} Дж")
print(f"E_фотона = {E_photon/eV:.4f} еВ")
print()

E_n = lambda n: -13.6 / n**2

n_i, n_f = 4, 2
E_i = E_n(n_i)
E_f = E_n(n_f)

delta_T = E_f - E_i

print(f"E(n={n_i}) = {E_i:.4f} еВ")
print(f"E(n={n_f}) = {E_f:.4f} еВ")
print(f"ΔT = E(n={n_f}) - E(n={n_i}) = {delta_T:.4f} еВ")
print(f"Кінетична енергія зменшилась на {abs(delta_T):.4f} еВ")
