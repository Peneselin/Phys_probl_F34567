import math

h = 6.626e-34
m_e = 9.11e-31
e = 1.6e-19
V = 2000
a = 0.3e-9
lam = h / math.sqrt(2 * m_e * e * V)
m_max = int(2 * a / lam)

print("Problem 6.41")
print(f"  Accelerating voltage V = {V} V")
print(f"  Lattice constant a = {a * 1e9:.1f} nm")
print(f"  de Broglie wavelength lambda = {lam:.4e} m  ({lam * 1e9:.4f} nm)")
print(f"  Bragg condition: 2*a*sin(theta) = m*lambda,  sin(theta) <= 1")
print(f"  Maximum order m_max = floor(2a/lambda) = {m_max}")
print(f"  Number of diffraction maxima = {m_max}")
