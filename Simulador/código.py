#Simulador básico de jogos para a mega sena.

#random
import random
from time import sleep


#lista
megasena = []
dados = []
jogos = 0

#loop erro
print('\33[33m-=' * 16)
while True:
    try:
        while jogos <= 0:
            jogos = int(input('\33[34mQuantos sorteios você deseja?\nResposta: '))
            if jogos <= 0:
                print('\33[31mApenas números inteiros a cima de 0 são aceitos nesse programa!')
        print('\33[33m-=' * 16)
        break
    except ValueError:
        print('\33[31mApenas números inteiros são aceitos nesse programa!')
#Loop
for c in range(jogos):
    print(f'\33[36mSorteando o jogo {c + 1}...')
    sleep(0.50)
    # menos que 6 números
    while len(dados) < 6:
        numaleatorio = random.randint(1, 60)
        if numaleatorio not in dados:
            dados.append(numaleatorio)
    dados.sort()
    megasena.append(dados[:])
    dados.clear()

#conclusão
print('\33[33m-=' * 16)
for i, jogo in enumerate(megasena, start=1):
    print(f'\33[1;32mJogo {i}: {jogo}')
print('\33[33m-=' * 16)
print('\33[1;35m----------Boa Sorte!!!----------')
print('\33[33m-=' * 16)