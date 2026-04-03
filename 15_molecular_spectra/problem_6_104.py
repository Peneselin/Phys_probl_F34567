print("Problem *6.104")
print()
print("  l = 1  (p-subshell),  s = 1/2")
print("  Possible principal quantum numbers: n = 2, 3, 4, ...")
print()
print("  Total angular momentum j = |l В± s|:")

j_values = [abs(1 - 0.5), abs(1 + 0.5)]

for j in sorted(j_values):
    print(f"    j = {j}")

print("  Spectroscopic term notation ^{2S+1}L_J  (S=1/2, 2S+1=2, L=P):")

for j in sorted(j_values):
    print(f"    ^2 P_{{j={j}}}")


print("  States for the lowest few n values:")

for n in range(2, 6):
    for j in sorted(j_values):
        print(f"    n={n}, l=1, j={j}  ->  {n}P_{j}")
