from utils import calcular_imc, classificar, obter_dado, cores
from time import sleep

print('-' * 50)
print(f'{cores['azul']}Calculador de IMC - Índice de massa corporal{cores['normal']}'.center(60))
print('-' * 50)
peso = obter_dado('Digite seu peso em KG: ')
altura = obter_dado('Digite sua altura em metros: ')

print(f'{cores['amarelo']}Calculando seu IMC...{cores['normal']}')
sleep(0.5)

imc = calcular_imc(peso, altura)
classificação = classificar(imc)
print(f'Seu IMC é: {imc:.2f}')
print(f'Classificação: {classificação}{cores['normal']}')