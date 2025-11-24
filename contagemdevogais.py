def codigo12():
    t = input("Texto: ").lower()
    vogais = sum(1 for c in t if c in "aeiou")
    print("Vogais:", vogais)
