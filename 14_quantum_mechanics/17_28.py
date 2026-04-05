def delta_E_units(n):
    return 2 * n + 1

n_values = [1, 10]

print("=" * 50)
print("Задача 17.28")
print("=" * 50)
print("E_n = n²·E₁  →  ΔE_n = (2n+1)·E₁")
print()

results = {}
for n in n_values:
    dE = delta_E_units(n)
    results[n] = dE
    print(f"n = {n:2d}:  ΔE = E_{n+1} - E_{n} = ({2*n}+1)·E₁ = {dE}·E₁")

ratio = results[10] / results[1]
print()
print(f"Відношення: ΔE(n=10) / ΔE(n=1) = {results[10]} / {results[1]} = {ratio:.1f}")
print(f"Відстань між рівнями 10 і 11 у {ratio:.0f} разів більша,")
print(f"ніж між рівнями 1 і 2.")
