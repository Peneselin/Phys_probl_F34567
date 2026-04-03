lambda_nm = 550e-9
n_film = 1.2
n_glass = 1.5
d_min = lambda_nm / (4 * n_film)

print("Problem 13.10")
print(f"  n_film  = {n_film}")
print(f"  n_glass = {n_glass}")
print(f"  lambda  = {lambda_nm * 1e9:.0f} nm")
print(f"  Both reflections have pi phase shift в†’ condition: 2*n*d = (m+1/2)*lambda")
print(f"  Minimum thickness (m = 0): d = lambda / (4 * n_film)")
print(f"  d_min = {d_min * 1e9:.2f} nm")
