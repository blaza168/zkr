from math import gcd

def calculate_inverse_element(a, mod):
    if gcd(a, mod) != 1:
        return None
    for i in range(1, mod):
        if (a * i) % mod == 1:
            return i


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: [a] [mod]")
        exit()
    a, mod = int(sys.argv[1]), int(sys.argv[2])
    inverse = calculate_inverse_element(a, mod)
    if inverse is None:
        print("Inverse element doesnt exist!")
        print("GDC(%d, %d) = %d" % (a, mod, gcd(a, mod)))
    else:
        print("Inverse element: " + str(inverse))