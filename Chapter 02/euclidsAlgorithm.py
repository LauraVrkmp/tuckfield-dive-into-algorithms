def gcd(x, y):
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller

    if (remainder == 0):
        return smaller
    else:
        return(gcd(smaller, remainder))
    
print(gcd(105, 33))