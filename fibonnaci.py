def codigo13():
    n = int(input("Quantos termos? "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
