import math

h = 6.626e-34
m_e = 9.11e-31
e = 1.6e-19
V = 30.0
d = 50.0e-6
L = 1.00
lam = h / math.sqrt(2 * m_e * e * V)
delta_y = lam * L / d
print("Problem 17.10 вЂ“ Electron double-slit diffraction fringe spacing")
print(f"  Accelerating voltage V = {V} V")
print(f"  Slit separation d = {d * 1e6:.1f} Вµm,  screen distance L = {L} m")
print(f"  de Broglie wavelength lambda = h/sqrt(2*m_e*eV) = {lam:.4e} m")
print(
    f"  Fringe spacing Delta_y = lambda*L/d = {delta_y:.4e} m  ({delta_y * 1e6:.2f} Вµm)"
)
