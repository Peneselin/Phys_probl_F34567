k_B = 1.38e-23
e_ = 1.6e-19
T = 300
dE = 0.66 * e_
alpha = -dE / (2 * k_B * T**2)

print("Problem 18.25")
print(f"  T = {T} K,  Delta_E = 0.66 eV")
print(f"  R в€ќ exp(Delta_E/(2*k_B*T))")
print(f"  alpha = d(ln R)/dT = -Delta_E/(2*k_B*T^2)")
print(f"  alpha = {alpha:.4f} K^-1  ({alpha:.4e} K^-1)")
print(f"  (Negative: resistance decreases with rising temperature)")
