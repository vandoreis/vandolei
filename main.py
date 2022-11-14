class Jogador():
    def __init__(self, nome, tier, convidados=[]):
        self.nome = nome
        self.tier = tier
        self.convidados = convidados


# TIER S
thigas = Jogador('thigas', 40)

# TIER A
marcos = Jogador("marcos", 35)
pani = Jogador("pani", 35)
raissa = Jogador("raissa", 35)
magnus = Jogador("magnus", 35)
lucas = Jogador("lucas", 35)

# TIER B
leite = Jogador("leite", 30)
vando = Jogador("vando", 30)
bruno = Jogador("bruno", 30)
devao = Jogador("devao", 30)
pedro = Jogador("pedro", 30)

# TIER C
bitola = Jogador("bitola", 25)
rato = Jogador("rato", 25)
vinhal = Jogador("vinhal", 25)
teteu = Jogador("teteu", 25)
vargas = Jogador("vargas", 25)
warley = Jogador("warley", 25)

# TIER D
rickao = Jogador("rickao", 20)
bia = Jogador("bia", 20)
thaliny = Jogador("thaliny", 20)
markin = Jogador("markin", 20)
ney = Jogador("ney", 20)
litorate = Jogador("litorate", 20)
sarah = Jogador("sarah", 20)
malu = Jogador("malu", 20)

# TIER E
gabriel = Jogador("gabriel", 15)
ale = Jogador("ale", 15)
jensom = Jogador("jensom", 15)
loloh = Jogador("loloh", 15)
miguel = Jogador("miguel", 15)
gira = Jogador("gira", 15)
marques = Jogador("marques", 15)

# TIER F
rata = Jogador("rata", 5)
gusthavo = Jogador("gusthavo", 5)
poly = Jogador("poly", 5)
fabao = Jogador("fabao", 5)

# TIER Z
moura = Jogador("moura", 0)
igor = Jogador("igor", 0)
giulia = Jogador("giulia", 0)

TAMANHO_TIME = 4
NUM_TIMES = 3

jogadores = [
    vando,
    thigas,
    bruno,
    markin,
    rato,
    teteu,
    litorate,
    warley,
    marcos,
    vargas,
]

thigas.convidados = [lucas]
markin.convidados = [malu]


def calcula_nota_de_corte():
    soma = 0
    for jogador in jogadores:
        soma += jogador.tier
        for convidado in jogador.convidados:
            soma += convidado.tier
    soma /= NUM_TIMES
    return soma


IDEAL = calcula_nota_de_corte()

import random


def sorteia_jogador(nomes):
    pos = random.randint(0, len(nomes) - 1)
    return nomes[pos]


def gera_times():
    times = []
    lista_jogadores = jogadores.copy()
    for i in range(NUM_TIMES):
        time = []
        while True:
            jogador = sorteia_jogador(lista_jogadores)

            if jogador.convidados == []:
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


def calcula_score_time(time):
    soma = calcula_valor_final_time(time)
    dif = (IDEAL - soma) ** 2
    return dif


def calcula_score_solucao(times):
    score = 0
    for time in times:
        score += calcula_score_time(time)
    return score


def printa_times(times):
    print(f"IDEAL: {IDEAL}")
    print('-' * 30)
    for i in range(NUM_TIMES):
        print(f"TIME {i + 1} : {calcula_valor_final_time(times[i])}")
        for j in range(TAMANHO_TIME):
            print(f'{j + 1}. {times[i][j].nome} - {times[i][j].tier}')
        print('-' * 30)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score = melhor_score = 100000
    i = 0
    while i < 1000 and score != 0:
        times_sorteados = gera_times()
        score = calcula_score_solucao(times_sorteados)
        if score < melhor_score:
            melhor_score = score
            solucao = times_sorteados.copy()

        i += 1
        print(i)

    printa_times(solucao)
