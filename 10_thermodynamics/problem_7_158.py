W = 2.10e3
T_cold = 280
T_hot = 350
COP = T_cold / (T_hot - T_cold)
Q_cold = COP * W
Q_hot = Q_cold + W

print("Problem 7.158")
print(f"  Work per cycle W = {W / 1e3:.2f} kJ")
print(f"  T_cold = {T_cold} K,  T_hot = {T_hot} K")
print()
print(f"  COP = T_cold / (T_hot - T_cold) = {COP:.2f}")
print(f"  1) Q_cold = COP * W = {Q_cold:.1f} J  ({Q_cold / 1e3:.2f} kJ)")
print(f"  2) Q_hot  = Q_cold + W = {Q_hot:.1f} J  ({Q_hot / 1e3:.2f} kJ)")
print(f"  3) COP = {COP:.2f}")
