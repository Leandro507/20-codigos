def codigo1():
    chars = string.ascii_letters + string.digits
    senha = "".join(random.choice(chars) for _ in range(12))
    print("Senha gerada:", senha)
