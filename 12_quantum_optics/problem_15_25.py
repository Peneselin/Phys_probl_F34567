import math

h = 6.626e-34
c = 3e8
m_e = 9.11e-31
e = 1.6e-19
lam_C = h / (m_e * c)
lam0 = 20e-12
theta = math.pi / 2
delta_lam = lam_C * (1 - math.cos(theta))
lam1 = lam0 + delta_lam
E_photon0 = h * c / lam0
E_photon1 = h * c / lam1
E_kinetic = E_photon0 - E_photon1
p0 = h / lam0
p1 = h / lam1
p_e = math.sqrt(p0**2 + p1**2)

print("Problem 15.25")
print(f"  Incident wavelength lambda0 = {lam0 * 1e12:.1f} pm")
print(f"  Scattering angle theta = 90В°")
print(f"  Compton wavelength lambda_C = {lam_C * 1e12:.3f} pm")
print()
print(f"  1) Delta lambda = lambda_C*(1-cos90В°) = {delta_lam * 1e12:.3f} pm")
print(f"     Scattered wavelength lambda' = {lam1 * 1e12:.3f} pm")
print(f"  2) E_kinetic = {E_kinetic:.4e} J  ({E_kinetic / e:.2f} eV)")
print(f"  3) Recoil electron momentum p_e = {p_e:.4e} kgВ·m/s")
