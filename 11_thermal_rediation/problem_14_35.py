sigma = 5.67e-8
T = 280
M_grey_kJ_per_m2_per_h = 325
M_grey = M_grey_kJ_per_m2_per_h * 1e3 / 3600
epsilon = M_grey / (sigma * T**4)

print("Problem 14.35")
print(f"  T = {T} K")
print(f"  M_grey = {M_grey_kJ_per_m2_per_h} kJ/(mВІВ·h) = {M_grey:.2f} W/mВІ")
print(f"  sigma*T^4 = {sigma * T**4:.2f} W/mВІ")
print(f"  epsilon = M_grey / (sigma*T^4) = {epsilon:.3f}")
