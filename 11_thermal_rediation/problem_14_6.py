import math

sigma = 5.67e-8
U = 127
I = 0.31
d = 0.3e-3
L = 5e-2
epsilon = 0.31
P_elec = U * I
A = math.pi * d * L
T = (P_elec / (epsilon * sigma * A)) ** 0.25

print("Problem 14.6")
print(f"  U = {U} V,  I = {I} A  =>  P = {P_elec:.2f} W")
print(f"  Filament: d = {d * 1e3:.1f} mm,  L = {L * 1e2:.0f} cm")
print(f"  Surface area A = pi*d*L = {A:.4e} mВІ")
print(f"  Emissivity ratio epsilon = {epsilon}")
print(f"  T = (P / (epsilon * sigma * A))^(1/4) = {T:.0f} K")
