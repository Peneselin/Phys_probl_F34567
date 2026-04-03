sigma = 5.67e-8
b = 2.898e-3
T1 = 1000
T2 = 3000
M_ratio = (T2 / T1) ** 4
lam1 = b / T1
lam2 = b / T2
delta_lam = lam1 - lam2
M_max_ratio = (T2 / T1) ** 5

print("Problem 14.16")
print(f"  T1 = {T1} K,  T2 = {T2} K")
print()
print(f"  1) Emissive power ratio M2/M1 = (T2/T1)^4 = {M_ratio:.0f}")
print(f"  2) lambda_max(T1) = {lam1 * 1e6:.2f} Вµm")
print(f"     lambda_max(T2) = {lam2 * 1e6:.3f} Вµm")
print(f"     Delta lambda   = {delta_lam * 1e6:.4f} Вµm  ({delta_lam * 1e9:.1f} nm)")
print(f"  3) M_max ratio (в€ќ T^5): M_max2/M_max1 = (T2/T1)^5 = {M_max_ratio:.0f}")
