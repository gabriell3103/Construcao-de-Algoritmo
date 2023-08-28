# Modifique o programa da árvore de natal para usar comandos for in range() em vez de escrever explicitamente cada linha.
# Você vai precisar de 4 laços com for para desenhar a mesma árvore.

def desenhar_arvore(altura):
    for i in range(altura):
        for j in range(altura - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    for l in range(altura // 3):
        for m in range(altura - 2):
            print(" ", end="")
        print("|||")


altura_arvore = 5
desenhar_arvore(altura_arvore)