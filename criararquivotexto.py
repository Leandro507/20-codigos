def criar_arquivo_texto():
    path = os.path.join(BASE_DIR, "arquivo.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("Conteúdo gerado pelo script.")
    print("Arquivo criado:", path)
