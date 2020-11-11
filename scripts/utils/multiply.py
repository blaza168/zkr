# Calculate: pow(a, n) % mod
def square_multiply(a, n, mod):
    return pow(a, n, mod)


if __name__ == '__main__':
    import sys
    a, n, mod = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    print(square_multiply(a, n, mod))
