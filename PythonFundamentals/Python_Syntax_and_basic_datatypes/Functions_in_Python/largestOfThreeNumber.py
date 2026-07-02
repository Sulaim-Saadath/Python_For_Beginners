def largestThree(a, b, c):
    if (a > b and a >c):
        print(f"{a} is greater")
    elif (b > a and b > c):
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
largestThree(10, 2, 5)