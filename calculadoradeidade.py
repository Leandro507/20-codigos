def codigo15():
    ano = int(input("Ano de nascimento: "))
    atual = datetime.now().year
    print("Idade:", atual - ano)
