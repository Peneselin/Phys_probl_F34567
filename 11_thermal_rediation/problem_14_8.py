import math

sigma = 5.67e-8
T_sun = 5800
R_sun = 6.96e8
d_SE = 1.496e11
exitance = sigma * T_sun**4
solar_constant = exitance * (R_sun / d_SE) ** 2

print("Problem 14.8")
print(f"  T_sun = {T_sun} K")
print(f"  R_sun = {R_sun:.3e} m")
print(f"  EarthвЂ“Sun distance = {d_SE:.3e} m")
print(f"  Surface exitance M = sigma*T^4 = {exitance:.3e} W/mВІ")
print(f"  Solar constant S = M*(R_sun/d)^2 = {solar_constant:.1f} W/mВІ")
