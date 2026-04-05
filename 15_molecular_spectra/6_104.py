print("=" * 50)
print("Задача *6.104")
print("=" * 50)
print("Збуджений атом гідрогену, l = 1")
print()

l = 1

print(f"l = {l}  →  можливі значення n: n ≥ l+1, тобто n ≥ {l+1}")
print()

spectral_series = {2: "2p", 3: "3p", 4: "4p", 5: "5p"}

print("Можливі стани (спектральні позначення):")
for n, label in spectral_series.items():
    print(f"  n={n}, l={l}  →  {label}")

print()
print("Можливі значення ml (магнітне квантове число):")
for ml in range(-l, l + 1):
    print(f"  ml = {ml:+d}")

print()
print("Можливі значення внутрішнього квантового числа j = l ± s,  s=1/2:")
j_values = [l - 0.5, l + 0.5]
for j in j_values:
    print(f"  j = {j}")
