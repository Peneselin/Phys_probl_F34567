import math

sigma = 5.67e-8
b = 2.898e-3
c = 3e8
R_sun = 6.96e8
M_sun = 1.989e30
lam_max = 0.48e-6
T_sun = b / lam_max
P_sun = 4 * math.pi * R_sun**2 * sigma * T_sun**4
dm_dt = P_sun / c**2
time_s = 0.01 * M_sun / dm_dt
time_yr = time_s / (365.25 * 24 * 3600)

print("Problem 14.22")
print(f"  lambda_max = {lam_max * 1e6:.2f} Вµm")
print(f"  T_sun = b / lambda_max = {T_sun:.0f} K")
print(f"  Total radiated power P = {P_sun:.3e} W")
print(f"  dm/dt = P / c^2 = {dm_dt:.3e} kg/s")
print(f"  Time for 1% mass loss = {time_s:.3e} s  (~{time_yr:.2e} years)")
