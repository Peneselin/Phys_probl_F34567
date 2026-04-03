R_H = 1.097e7
lam_min_vis = 380e-9
lam_max_vis = 760e-9

print("Problem 16.6 вЂ“ Balmer series lines in the visible spectrum")
print(f"  Visible range: {lam_min_vis * 1e9:.0f}вЂ“{lam_max_vis * 1e9:.0f} nm")

print("  n     lambda (nm)   visible?")

count = 0

for n in range(3, 20):
    inv_lam = R_H * (1 / 4 - 1 / n**2)
    lam = 1 / inv_lam
    visible = lam_min_vis <= lam <= lam_max_vis

    if visible:
        count += 1

    mark = " <-- visible" if visible else ""
    print(f"  n={n}:  {lam * 1e9:.1f} nm{mark}")

    if lam < lam_min_vis:
        break

print(f"  Number of Balmer lines in visible range: {count}")
