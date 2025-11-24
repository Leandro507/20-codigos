def codigo10():
    nome = "".join(random.choice(string.ascii_lowercase) for _ in range(7))
    print("Nome gerado:", nome.capitalize())
