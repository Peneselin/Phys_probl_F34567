n1 = 1
n2 = 10
gap1 = 2 * n1 + 1
gap2 = 2 * n2 + 1
ratio = gap1 / gap2

print("Problem 17.28")
print(f"  E_n = n^2 * E1")
print(f"  Delta_E_n = E_{{n+1}} - E_n = (2n+1) * E1")
print()
print(f"  Gap at n = {n1}:  Delta_E_{n1}  = {gap1} * E1")
print(f"  Gap at n = {n2}: Delta_E_{n2} = {gap2} * E1")
print(f"  Ratio Delta_E_{n1} / Delta_E_{n2} = {gap1}/{gap2} = {ratio:.4f}")
