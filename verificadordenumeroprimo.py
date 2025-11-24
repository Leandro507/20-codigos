def codigo4():
    n = int(input("Número: "))
    if n < 2:
        print("Não é primo")
        return
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Não é primo")
            return
    print("É primo!")
