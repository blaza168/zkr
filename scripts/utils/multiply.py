from math import pow

# Calculate: pow(a, n) % mod
def square_multiply(a, n, mod):
    n_bin = bin(n)[2:]
    calculation_result = a
    for i in range(1, len(n_bin)):
        if n_bin[i] == '1':
            # Square and multiply
            calculation_result = (pow(calculation_result, 2) * a) % mod
        else:
            # Only square
            calculation_result = pow(calculation_result, 2) % mod

    return calculation_result