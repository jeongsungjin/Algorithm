def z_order(n, r, c):
    if n == 0:
        return 0
    
    half = 2**(n - 1)
    size = half * half

    if r < half and c < half:
        return z_order(n - 1, r, c)
    elif r < half and c >= half:
        return size + z_order(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2*size + z_order(n - 1, r - half, c)
    else:
        return 3*size + z_order(n - 1, r - half, c - half)
    
n, r, c = map(int, input().split())
print(z_order(n, r, c))