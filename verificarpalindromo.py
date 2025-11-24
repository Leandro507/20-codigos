def codigo19():
    t = input("Texto: ").replace(" ", "").lower()
    print("É palíndromo" if t == t[::-1] else "Não é palíndromo")
