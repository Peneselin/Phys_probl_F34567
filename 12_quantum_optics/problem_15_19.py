h = 6.626e-34
c = 3e8
e = 1.6e-19
lam = 200e-9
lam_red = 310e-9
E_kin_J = h * c * (1 / lam - 1 / lam_red)
E_kin_eV = E_kin_J / e

print("Problem 15.19")
print(f"  lambda_red = {lam_red * 1e9:.0f} nm  (work function wavelength)")
print(f"  lambda     = {lam * 1e9:.0f} nm  (incident light)")
print(f"  E_kin = h*c*(1/lambda - 1/lambda_red)")
print(f"  E_kin = {E_kin_J:.4e} J  =  {E_kin_eV:.2f} eV")
