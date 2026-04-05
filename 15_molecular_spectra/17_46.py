import math

h   = 6.62607015e-34
c   = 3e8
k_B = 1.380649e-23

T   = 27 + 273.15
lam = 0.6943e-6

E_photon = h * c / lam

ratio = math.exp(-E_photon / (k_B * T))

print("=" * 50)
print("Задача *17.46")
print("=" * 50)
print(f"T   = {T} К")
print(f"λ   = {lam*1e9:.4f} нм")
print(f"E_фотона = hc/λ = {E_photon:.3e} Дж")
print(f"k_B·T = {k_B*T:.3e} Дж")
print(f"E/(k_B·T) = {E_photon/(k_B*T):.2f}")
print()
print(f"N₂/N₁ = exp(-E/k_BT) = {ratio:.3e}")
print(f"Заселеність верхнього рівня у {1/ratio:.2e} разів менша")
