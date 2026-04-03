import math

phi_deg = 63.0
absorption = 0.10
phi_rad = math.radians(phi_deg)
cos2 = math.cos(phi_rad) ** 2
I1_over_I0 = 0.5 * (1 - absorption)
I2_over_I1 = cos2 * (1 - absorption)
I2_over_I0 = I1_over_I0 * I2_over_I1
attenuation = 1.0 / I2_over_I0

print("Problem 13.46")
print(f"  Angle between principal planes: phi = {phi_deg:.0f}В°")
print(f"  Absorption in each Nicol: {absorption * 100:.0f} %")
print(f"  cos^2(phi) = {cos2:.4f}")
print(f"  After 1st Nicol: I1/I0 = {I1_over_I0:.4f}")
print(f"  After 2nd Nicol: I2/I0 = {I2_over_I0:.5f}")
print(f"  Attenuation factor I0/I2 = {attenuation:.1f}")
