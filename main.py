import random
import jogador


def calcula_nota_de_corte(lista_jog):
    soma = 0
    for jog in lista_jog:
        soma += jog.tier
        for convidado in jog.convidados:
            soma += convidado.tier
    soma /= NUM_TIMES
    return soma


def sorteia_jogador(nomes):
    pos = random.randint(0, len(nomes) - 1)
    return nomes[pos]


def gera_times(tamanho_time, num_times, jogadores_cadastrados):
    times = []
    lista_jogadores = jogadores_cadastrados.copy()
    for i in range(num_times):
        time = []
        while True:
            jog = sorteia_jogador(lista_jogadores)

            if not jog.convidados:
                time.append(jog)
                lista_jogadores.remove(jog)

            else:
                possivel_time = time.copy()
                possivel_time.append(jog)
                for convidado in jog.convidados:
                    possivel_time.append(convidado)

                if len(possivel_time) <= tamanho_time:
                    time = possivel_time.copy()
                    lista_jogadores.remove(jog)

            if len(time) == tamanho_time:
                times.append(time)
                break
    return times


def calcula_valor_final_time(time):
    soma = 0
    for jog in time:
        soma += jog.tier
    return soma


def calcula_score_time(time, ideal):
    soma = calcula_valor_final_time(time)
    dif = (ideal - soma) ** 2
    return dif


def calcula_score_solucao(times, ideal):
    score = 0
    for time in times:
        score += calcula_score_time(time, ideal)
    return score


def printa_times(times, ideal):
    print(f"IDEAL: {ideal}")
    print('-' * 30)
    for i in range(NUM_TIMES):
        print(f"TIME {i + 1} : {calcula_valor_final_time(times[i])}")
        for j in range(TAMANHO_TIME):
            print(f'{j + 1}. {times[i][j].nome} - {times[i][j].tier}')
        print('-' * 30)


def checa_parametros(tamanho_time, num_times, jogadores_cadastrados):
    convidados = []
    for jog in jogadores_cadastrados:
        for convidado in jog.convidados:
            convidados.append(convidado)

    if len(convidados) + len(jogadores_cadastrados) != tamanho_time * num_times:
        raise Exception("Número de jogadores cadastrados incompatível com o selecionado! Revisar cenário.")


def sorteia_times(tamanho_time, num_times, jogadores_cadastrados):
    solucao = []
    ideal = calcula_nota_de_corte(jogadores_cadastrados)
    score = melhor_score = 100000
    i = 0
    while i < 1000 and score != 0:
        times_sorteados = gera_times(tamanho_time, num_times, jogadores_cadastrados)
        score = calcula_score_solucao(times_sorteados, ideal)
        if score < melhor_score:
            melhor_score = score
            solucao = times_sorteados.copy()

        i += 1
    printa_times(solucao, ideal)


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
