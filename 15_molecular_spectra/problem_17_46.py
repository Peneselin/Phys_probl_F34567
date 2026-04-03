import math

h = 6.626e-34
c = 3e8
k_B = 1.38e-23
T = 300
lam = 0.6943e-6
delta_E = h * c / lam
exponent = -delta_E / (k_B * T)
ratio = math.exp(exponent)

print("Problem *17.46")
print(f"  lambda = {lam * 1e9:.2f} nm,  T = {T} K")
print(f"  Delta_E = h*c/lambda = {delta_E:.4e} J  ({delta_E / (1.6e-19):.3f} eV)")
print(f"  k_B*T = {k_B * T:.4e} J  ({k_B * T / (1.6e-19) * 1e3:.2f} meV)")
print(f"  Exponent = -Delta_E/(k_B*T) = {exponent:.2f}")
print(f"  N2/N1 = exp(-Delta_E/(k_B*T)) = {ratio:.3e}")
print()
print("  Note: This ratio is essentially zero, confirming that population inversion")
print("  (N2 > N1) cannot be achieved through thermal equilibrium alone.")
