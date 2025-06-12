#Parte 1: Definindo Espaços
espaco = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

#Parte 2: Vizualizando Tabuleiro
def exibirTabuleiro():
    tabela = (
            " " + espaco[0] + " | " + espaco[1] + " | " + espaco[2] +
            "\n-----------\n" +
            " " + espaco[3] + " | " + espaco[4] + " | " + espaco[5] +
            "\n-----------\n" +
            " " + espaco[6] + " | " + espaco[7] + " | " + espaco[8]
    )
    print(tabela)

#Parte 3: Validando Posições
def verificaPosicao(posicao):
    return espaco[posicao] not in ["x", "○"]

#Parte 4: Verificando o Vencedor
def verificaVencedor(jogador):
    if espaco[0] == espaco[1] == espaco[2] == jogador:
        return True
    elif espaco[3] == espaco[4] == espaco[5] == jogador:
        return True
    elif espaco[6] == espaco[7] == espaco[8] == jogador:
        return True
    elif espaco[0] == espaco[3] == espaco[6] == jogador:
        return True
    elif espaco[1] == espaco[4] == espaco[7] == jogador:
        return True
    elif espaco[2] == espaco[5] == espaco[8] == jogador:
        return True
    elif espaco[0] == espaco[4] == espaco[8] == jogador:
        return True
    elif espaco[2] == espaco[4] == espaco[6] == jogador:
        return True
    else:
        return False

#Parte 5: Laço de Repetição Principal
cont = 1
jogadorAtual = ""

while True:
    if cont % 2 != 0:
        jogadorAtual = "X"
    else:
        jogadorAtual = "○"

    exibirTabuleiro()

    print(f"Jogador {jogadorAtual}, é a sua vez.")
    escolha = int(input("Digite a posicao que voce deseja: "))
    if verificaPosicao(escolha):
        espaco[escolha] = jogadorAtual
    else:
        print("Posicao já ocupada. Tente novamente.")
        continue

    if verificaVencedor(jogadorAtual):
        exibirTabuleiro()
        print("Parabéns, você venceu!🎉🎉🎉")
        break

    if cont == 9:
        exibirTabuleiro()
        print("Essa não! De velha. Não tivemos vencedores.🤧🤧🤧")
        break

    cont += 1

