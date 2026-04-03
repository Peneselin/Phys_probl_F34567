import math

k_B = 1.38e-23
e_ = 1.6e-19
T1 = 300
T2 = 350
dE = 0.5 * e_
factor = dE / (2 * k_B)
ratio = math.exp(factor * (1 / T1 - 1 / T2))

print("Problem 18.23")
print(f"  Band gap Delta_E = 0.5 eV")
print(f"  T1 = {T1} K,  T2 = {T2} K")
print(f"  sigma exp(-Delta_E/(2*k_B*T))")
print(f"  R1/R2 = exp(Delta_E/(2*k_B)*(1/T1 - 1/T2))")
print(f"  R1/R2 = {ratio:.2f}")
print(f"  Resistance decreases {ratio:.2f}-fold upon heating from {T1} K to {T2} K")
