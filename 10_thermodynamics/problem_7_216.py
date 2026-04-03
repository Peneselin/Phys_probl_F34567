R = 8.314
m = 50e-3
T1 = 295
T2 = 400
Q = 2050
delta_T = T2 - T1
c = Q / (m * delta_T)
C_mol = 3 * R
M = C_mol / c
metals = {
    "Aluminium (Al)": 27e-3,
    "Iron (Fe)": 56e-3,
    "Copper (Cu)": 63.5e-3,
    "Zinc (Zn)": 65.4e-3,
    "Silver (Ag)": 108e-3,
    "Lead (Pb)": 207e-3,
}
print("Problem 7.216")
print(f"  m = {m * 1e3:.0f} g,  T1 = {T1} K,  T2 = {T2} K,  Q = {Q} J")
print(f"  Specific heat c = Q / (m * DeltaT) = {c:.2f} J/(kgВ·K)")
print(f"  DulongвЂ“Petit: C_mol = 3R = {C_mol:.2f} J/(molВ·K)")
print(f"  Estimated molar mass M = C_mol / c = {M * 1e3:.1f} g/mol")
print()
print("  Closest match:")

for name, M_ref in metals.items():
    diff = abs(M - M_ref) / M_ref * 100
    marker = " <-- best match" if diff < 5 else ""
    print(f"    {name}: M = {M_ref * 1e3:.1f} g/mol  (deviation {diff:.1f}%){marker}")
