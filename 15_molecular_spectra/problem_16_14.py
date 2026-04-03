h = 6.626e-34
c = 3e8
e_ = 1.6e-19
lam = 486e-9
E_photon_J = h * c / lam
E_photon_eV = E_photon_J / e_
n_f = 2
n_i = 4
KE_i_eV = 13.6 / n_i**2
KE_f_eV = 13.6 / n_f**2
dKE_eV = KE_f_eV - KE_i_eV
dKE_J = dKE_eV * e_

print("Problem 16.14")
print(f"  Emitted wavelength lambda = {lam * 1e9:.0f} nm")
print(f"  Photon energy = {E_photon_eV:.3f} eV  (Balmer H_beta, n=4 -> n=2)")
print(f"  KE_n = 13.6/n^2 eV  (virial theorem)")
print(f"  KE(n=4) = {KE_i_eV:.4f} eV")
print(f"  KE(n=2) = {KE_f_eV:.4f} eV")
print(f"  Delta_KE = KE(n=2) - KE(n=4) = {dKE_eV:.4f} eV  = {dKE_J:.4e} J")
print(f"  (Kinetic energy increases as electron moves to lower orbit)")
