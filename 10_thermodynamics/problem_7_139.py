kappa = 0.20
A = 1.0
d = 0.50
T_in = 291
T_out = 243
t = 24 * 3600
delta_T = T_in - T_out
Q = kappa * A * delta_T / d * t

print("Problem 7.139")
print(f"  Thickness d = {d * 100:.0f} cm")
print(f"  T_in = {T_in} K,  T_out = {T_out} K,  DeltaT = {delta_T} K")
print(f"  kappa = {kappa} W/(mВ·K),  area A = {A} mВІ,  time = 24 h")
print(f"  Q = kappa * A * DeltaT / d * t")
print(f"  Q = {Q:.0f} J  ({Q / 1e3:.1f} kJ)  ({Q / 1e6:.3f} MJ)")
