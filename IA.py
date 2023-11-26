import random

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

def jogada_valida(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == ' '

def realizar_jogada(tabuleiro, jogador, linha, coluna):
    tabuleiro[linha][coluna] = jogador

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vitoria(tabuleiro, 'O'):
        return -1
    if verificar_vitoria(tabuleiro, 'X'):
        return 1
    if tabuleiro_cheio(tabuleiro):
        return 0

    if maximizando:
        melhor_valor = float('-inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'X'
                    valor = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[i][j] = ' '
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        pior_valor = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'O'
                    valor = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i][j] = ' '
                    pior_valor = min(pior_valor, valor)
        return pior_valor

def movimento_ia(tabuleiro):
    melhor_movimento = None
    melhor_valor = float('-inf')
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'X'
                valor = minimax(tabuleiro, 0, False)
                tabuleiro[i][j] = ' '
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = (i, j)
    return melhor_movimento

def jogar_jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'O'

    while True:
        exibir_tabuleiro(tabuleiro)

        if jogador_atual == 'O':
            linha = int(input("Digite a linha para a sua jogada (0, 1 ou 2): "))
            coluna = int(input("Digite a coluna para a sua jogada (0, 1 ou 2): "))
            if not (0 <= linha <= 2) or not (0 <= coluna <= 2) or not jogada_valida(tabuleiro, linha, coluna):
                print("Jogada inválida. Tente novamente.")
                continue
        else:
            print("Vez da IA...")
            linha, coluna = movimento_ia(tabuleiro)

        realizar_jogada(tabuleiro, jogador_atual, linha, coluna)

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"O jogador {jogador_atual} venceu!")
            break
        elif tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogar_jogo_da_velha()
