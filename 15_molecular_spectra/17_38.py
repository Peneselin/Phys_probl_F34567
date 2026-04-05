print("=" * 50)
print("Задача 17.38")
print("=" * 50)
print("Набори квантових чисел (n, l, ml, ms)\n")

subshells = {"s": 0, "p": 1, "d": 2}

for name, l in subshells.items():
    print(f"--- {name}-оболонка (l={l}) ---")
    for ml in range(-l, l + 1):
        for ms in [+0.5, -0.5]:
            ms_str = "+1/2" if ms > 0 else "-1/2"
            print(f"  n=n, l={l}, ml={ml:+d}, ms={ms_str}")
    print()
