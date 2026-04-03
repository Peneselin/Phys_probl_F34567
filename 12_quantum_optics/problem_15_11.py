lam = 0.1e-6
lam_red = 0.3e-6
fraction = 1 - lam / lam_red

print("Problem 15.11")
print(f"  lambda     = {lam * 1e9:.0f} nm")
print(f"  lambda_red = {lam_red * 1e9:.0f} nm")
print(f"  E_photon proportional to 1/lambda")
print(f"  A = h*c/lambda_red,  E_kinetic = h*c*(1/lambda - 1/lambda_red)")
print(f"  Fraction = E_kinetic / E_photon = 1 - lambda/lambda_red")
print(f"  Fraction = {fraction:.4f}  ({fraction * 100:.1f} %)")
