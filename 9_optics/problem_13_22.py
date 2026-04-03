import math

a = 2e-6
lam = 589e-9

print("Problem 13.22")
print(f"  Slit width a = {a * 1e6:.1f} Вµm")
print(f"  Wavelength lambda = {lam * 1e9:.0f} nm")
print(f"  Condition: a * sin(theta) = m * lambda")
print()
print("  Minima:")

m = 1

while True:
    sin_theta = m * lam / a

    if abs(sin_theta) > 1:
        break

    theta_deg = math.degrees(math.asin(sin_theta))

    print(f"    m = {m:+d}: sin(theta) = {sin_theta:.4f}  => theta = {theta_deg:.1f}В°")
   
    m += 1

print()
print("  (Symmetric minima exist at negative angles as well.)")
