def codigo11():
    valores = input("Digite números separados por espaço: ")
    nums = list(map(float, valores.split()))
    print("Média =", sum(nums)/len(nums))
