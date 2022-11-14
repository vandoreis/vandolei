import random
import jogador


def calcula_nota_de_corte(jogadores):
    soma = 0
    for jogador in jogadores:
        soma += jogador.tier
        for convidado in jogador.convidados:
            soma += convidado.tier
    soma /= NUM_TIMES
    return soma


def sorteia_jogador(nomes):
    pos = random.randint(0, len(nomes) - 1)
    return nomes[pos]


def gera_times(TAMANHO_TIME, NUM_TIMES, jogadores):
    times = []
    lista_jogadores = jogadores.copy()
    for i in range(NUM_TIMES):
        time = []
        while True:
            jogador = sorteia_jogador(lista_jogadores)

            if not jogador.convidados:
                time.append(jogador)
                lista_jogadores.remove(jogador)

            else:
                possivel_time = time.copy()
                possivel_time.append(jogador)
                for convidado in jogador.convidados:
                    possivel_time.append(convidado)

                if len(possivel_time) <= TAMANHO_TIME:
                    time = possivel_time.copy()
                    lista_jogadores.remove(jogador)

            if len(time) == TAMANHO_TIME:
                times.append(time)
                break
    return times


def calcula_valor_final_time(time):
    soma = 0
    for jogador in time:
        soma += jogador.tier
    return soma


def calcula_score_time(time, IDEAL):
    soma = calcula_valor_final_time(time)
    dif = (IDEAL - soma) ** 2
    return dif


def calcula_score_solucao(times, IDEAL):
    score = 0
    for time in times:
        score += calcula_score_time(time, IDEAL)
    return score


def printa_times(times, IDEAL):
    print(f"IDEAL: {IDEAL}")
    print('-' * 30)
    for i in range(NUM_TIMES):
        print(f"TIME {i + 1} : {calcula_valor_final_time(times[i])}")
        for j in range(TAMANHO_TIME):
            print(f'{j + 1}. {times[i][j].nome} - {times[i][j].tier}')
        print('-' * 30)


def checa_parametros(TAMANHO_TIME, NUM_TIMES, jogadores):
    convidados = []
    for jogador in jogadores:
        for convidado in jogador.convidados:
            convidados.append(convidado)

    if len(convidados) + len(jogadores) != TAMANHO_TIME*NUM_TIMES:
        raise Exception("Número de jogadores cadastrados incompatível com o selecionado! Revisar cenário.")


def sorteia_times(TAMANHO_TIME, NUM_TIMES, jogadores):
    IDEAL = calcula_nota_de_corte(jogadores)
    score = melhor_score = 100000
    i = 0
    while i < 1000 and score != 0:
        times_sorteados = gera_times(TAMANHO_TIME, NUM_TIMES, jogadores)
        score = calcula_score_solucao(times_sorteados, IDEAL)
        if score < melhor_score:
            melhor_score = score
            solucao = times_sorteados.copy()

        i += 1
    printa_times(solucao, IDEAL)


if __name__ == '__main__':
    # PARÂMETROS CUSTOMIZAVEIS
    TAMANHO_TIME = 4
    NUM_TIMES = 3
    jogadores = [
        jogador.vando,
        jogador.thigas,
        jogador.bruno,
        jogador.markin,
        jogador.rato,
        jogador.teteu,
        jogador.litorate,
        jogador.warley,
        jogador.marcos,
        jogador.vargas,
    ]
    jogador.thigas.convidados = [jogador.lucas]
    jogador.markin.convidados = [jogador.malu]

    # OTIMIZADOR
    checa_parametros(TAMANHO_TIME, NUM_TIMES, jogadores)
    sorteia_times(TAMANHO_TIME, NUM_TIMES, jogadores)
