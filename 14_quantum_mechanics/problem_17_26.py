import math

hbar = 1.0546e-34
m_e = 9.11e-31
k_B = 1.38e-23
L = 0.1e-6
E1 = (math.pi**2 * hbar**2) / (2 * m_e * L**2)
T1 = 1.0
T2 = 10.0
n1 = math.sqrt(k_B * T1 / E1)
n2 = math.sqrt(k_B * T2 / E1)
n1_int = round(n1)
n2_int = round(n2)


def prob_at_centre(n, L):
    """Probability density at x=L/2 for quantum number n."""
    return (2 / L) * math.sin(n * math.pi / 2) ** 2


P1 = prob_at_centre(n1_int, L)
P2 = prob_at_centre(n2_int, L)

print("Problem 17.26")
print(f"  L = {L * 1e6:.1f} Вµm")
print(f"  Ground-state energy E1 = {E1:.4e} J")
print()
print(
    f"  T1 = {T1} K: E = k_B*T1 = {k_B * T1:.3e} J,  n в‰€ {n1:.2f}  => n_int = {n1_int}"
)
print(
    f"  T2 = {T2} K: E = k_B*T2 = {k_B * T2:.3e} J,  n в‰€ {n2:.2f}  => n_int = {n2_int}"
)
print()
print(
    f"  P(L/2) for n = {n1_int}: {P1:.4e}  {'(odd -> max)' if n1_int % 2 else '(even -> zero)'}"
)
print(
    f"  P(L/2) for n = {n2_int}: {P2:.4e}  {'(odd -> max)' if n2_int % 2 else '(even -> zero)'}"
)


def is_zero(n):
    return n % 2 == 0


z1 = is_zero(n1_int)
z2 = is_zero(n2_int)
if not z1 and not z2:
    print(f"  Ratio P2/P1 = {P2 / P1:.2f}")
elif z1 and not z2:
    print("  Probability increased from 0 (even n) to maximum 2/L (odd n).")
    print(
        "  The centre probability increases without limit relative to the initial zero."
    )
elif not z1 and z2:
    print("  Probability decreased from maximum 2/L (odd n) to 0 (even n).")
else:
    print("  Both states have even n => zero probability at the centre.")
