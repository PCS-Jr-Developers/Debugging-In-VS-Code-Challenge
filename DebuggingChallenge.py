def add(a, b):
    result = a + b
    return result

def multiply(c, d):
    result = c * d
    return result

def divide(e, f):
    if f == 0:
        result = "Cannot Divide by Zero."
    else:
        result = e / f
    return 0

def main():
    x = 6
    y = 3

    # Step into this function
    z = add(x, y)

    # Step over this function call
    w = multiply(z, y)

    D = divide(x, y)

    print("Result after addition:", z)
    print("Result after multiplication:", w)
    print("Result after division:", D)

if __name__ == "__main__":
    main()
