import math

slits_per_mm = 100
d = 1e-3 / slits_per_mm
m = 3
total_angle_deg = 20.0
theta_deg = total_angle_deg / 2
theta_rad = math.radians(theta_deg)
lam = d * math.sin(theta_rad) / m

print("Problem 13.26")
print(f"  Grating period d = {d * 1e6:.1f} Вµm")
print(f"  Diffraction order m = {m}")
print(f"  Total rotation angle = {total_angle_deg:.0f}В°  => theta = {theta_deg:.0f}В°")
print(f"  Grating equation: d * sin(theta) = m * lambda")
print(f"  lambda = d * sin(theta) / m = {lam * 1e9:.1f} nm")
