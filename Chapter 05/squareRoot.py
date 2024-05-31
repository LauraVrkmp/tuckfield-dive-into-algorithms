def squareRoot(x, y, error_tolerance):
    our_error = error_tolerance * 2
    while (our_error > error_tolerance):
        z = x / y
        y = (y + z) / 2
        our_error = y**2 - x
    return  y


print(squareRoot(5, 1, 0.00000000000001))