alfabeto = "abcdefghijklmnopqrstuvwyz"


def encript(mensagem, posicoes):
    msg = ""
    # percorre a mensagem
    for i in mensagem:
        # procura as letras no alfabeto
        if i in alfabeto:
            # procura o indice da letra no alfabeto
            i_indice = alfabeto.index(i)
            # concatena depois de somar as posicões com o indice, pegando o resto da divisão para que a posição
            # possa ultrapassar as letras de alfabeto
            msg += alfabeto[(i_indice + posicoes) % len(alfabeto)]
        else:
            # caso o simbolo não esteja no alfabeto apenas adicione ele na mensagem
            msg += i

    return msg


def decript(mensagem, posicoes):
    msg = ""

    for i in mensagem:
        if i in alfabeto:
            i_indice = alfabeto.index(i)
            msg += alfabeto[(i_indice - posicoes) % len(alfabeto)]
        else:
            msg += i

    return msg


print("===== CRIPTOGRAFIA DE MENSAGEM =====")
while True:
    opc = int(input("1 - Criptografar\n2 - Descriptografar\n0 - Sair \n-> "))

    if opc == 0:
        print("Encerrando...")
        break

    if opc == 1:
        mensagem = input("Mensagem a ser criptografada: ")
        posicao = int(input("Quantas posições você deseja avançar: "))
        resultado = encript(mensagem, posicao)
        print("Resultado: " + resultado + "\n====================================")

    if opc == 2:
        mensagem = input("Mensagem a ser descriptografada: ")
        posicao = int(input("Quantas posições você deseja retornar: "))
        resultado = decript(mensagem, posicao)
        print("Resultado: " + resultado + "\n====================================")
