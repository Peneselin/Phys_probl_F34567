import math

lam = 600e-9
D = 6e-3
r = D / 2
b = 3.0
m = r**2 / (lam * b)

print("Problem 13.18")
print(f"  Wavelength lambda = {lam * 1e9:.0f} nm")
print(f"  Aperture diameter D = {D * 1e3:.0f} mm  (radius r = {r * 1e3:.1f} mm)")
print(f"  Screen distance b = {b:.0f} m")
print(f"  Number of Fresnel zones: m = r^2 / (lambda * b) = {m:.1f}")
print()

m_int = round(m)
if m_int % 2 == 1:
    centre = "BRIGHT (odd number of zones вЂ“ amplitudes add up)"
else:
    centre = "DARK (even number of zones вЂ“ amplitudes partially cancel)"

print(f"  m в‰€ {m_int} ({('odd' if m_int % 2 else 'even')}) => centre is {centre}")
