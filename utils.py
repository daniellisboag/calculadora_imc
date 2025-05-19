cores = {'vermelho' : '\033[1;31m', 'verde' : '\033[1;32m', 'amarelo' : '\033[1;33m', 'azul' : '\033[1;34m', 'normal' : '\033[m'}

def calcular_imc(peso, altura):
   return peso / (altura ** 2)

def classificar(imc):
   if imc < 18.5:
      return f'{cores['amarelo']}Abaixo do peso.'
   elif 18.5 <= imc < 25:
      return f'{cores['verde']}Peso normal.'
   elif 25 <= imc < 30:
      return f'{cores['amarelo']}Sobrepeso.'
   elif 30 <= imc < 35:
      return f'{cores['vermelho']}Obessidade grau I.'
   elif 35 <= imc < 40:
      return f'{cores['vermelho']}Obessidade grau II.'
   else:
      return f'{cores['vermelho']}Obessidade grau III.'

def obter_dado(valor):
   while True:
      try:
         resposta = float(input(valor).replace(',', '.'))
         if resposta <= 0:
            print(f'{cores['vermelho']}Por favor, digite um número maior que zero.{cores['normal']}')
            continue
         return resposta
      except ValueError:
         print(f'{cores['vermelho']}Valor inválido! Digite um número válido.{cores['normal']}')