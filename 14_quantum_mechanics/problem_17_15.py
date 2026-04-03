hbar = 1.0546e-34
h = 6.626e-34
c = 3e8
lam = 600e-9
t = 1e-8
dE = hbar / t
dnu = dE / h
dlam = lam**2 / c * dnu

print("Problem 17.15")
print(f"  Mean lifetime t = {t:.0e} s")
print(f"  Wavelength lambda = {lam * 1e9:.0f} nm")
print(f"  Energy uncertainty:      Delta_E   = hbar/t = {dE:.4e} J")
print(f"  Frequency linewidth:     Delta_nu  = {dnu:.4e} Hz  ({dnu:.2e} Hz)")
print(f"  Wavelength linewidth:    Delta_lam = {dlam:.4e} m  ({dlam * 1e12:.4f} pm)")
