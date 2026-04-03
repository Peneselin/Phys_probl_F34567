import math

a0 = 5.29e-11
v1 = 2.19e6
e_ = 1.6e-19
T1 = 2 * math.pi * a0 / v1
I = e_ / T1

print("Problem 17.43 вЂ“ Equivalent current on first Bohr orbit")
print(f"  a0 = {a0:.3e} m,  v1 = {v1:.3e} m/s")
print(f"  Period T1 = 2*pi*a0/v1 = {T1:.4e} s")
print(f"  Current I = e/T1 = {I:.4e} A  ({I * 1e3:.3f} mA)")
