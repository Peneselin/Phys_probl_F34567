subshells = {
    "s": 0,
    "p": 1,
    "d": 2,
}

print("Problem 17.38")

for name, l in subshells.items():
    print(f"  {name}-subshell  (l = {l}):")

    for ml in range(-l, l + 1):
        for ms_num in [1, -1]:
            ms = ms_num / 2
            print(f"    l={l}, ml={ml:+d}, ms={ms:+.1f}")
            
    print(f"    Total states: {2 * (2 * l + 1)}")
    print()
