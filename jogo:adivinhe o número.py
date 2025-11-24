def codigo5():
    n = random.randint(1, 10)
    palpite = int(input("Adivinhe (1-10): "))
    print("Acertou!" if palpite == n else f"Errou! Era {n}")
