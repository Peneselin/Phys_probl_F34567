R_H = 1.097e7

visible_min = 380e-9
visible_max = 700e-9

print("=" * 50)
print("Задача 16.6")
print("=" * 50)

count = 0
for n in range(3, 20):
    lam = 1 / (R_H * (1/4 - 1/n**2))
    if visible_min <= lam <= visible_max:
        count += 1
        print(f"n={n}  →  λ = {lam*1e9:.1f} нм  (видима)")
    elif lam < visible_min:
        break

print(f"\nКількість ліній серії Бальмера у видимій області: {count}")
