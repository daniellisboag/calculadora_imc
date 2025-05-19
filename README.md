# 🧮 Calculadora de IMC (Índice de Massa Corporal)
Este projeto em Python calcula o IMC (Índice de Massa Corporal) do usuário com base em seu peso e altura. Além disso, fornece a classificação segundo os padrões da **Organização Mundial da Saúde (OMS)**.

---

## 🔍 O que é IMC?
O IMC é uma medida utilizada para saber se uma pessoa está no peso ideal, com sobrepeso ou obesidade, levando em conta apenas o peso e a altura.

A fórmula é:
```python
imc = peso / (altura ** 2)
```

---

## ✨ Funcionalidades
- ✅ Entrada de peso e altura com validação
- ✅ Tratamento de erros de entrada (strings, números negativos, etc.)
- ✅ Cálculo automático do IMC
- ✅ Classificação do IMC com base na tabela da OMS
- ✅ Estilização com **cores ANSI** no terminal

---

## 📌 Classificação do IMC
| IMC                   | Classificação              |
|-----------------------|----------------------------|
| Menor que 18.5        | Abaixo do peso             |
| Entre 18.5 e 24.9     | Peso normal                |
| Entre 25.0 e 29.9     | Sobrepeso                  |
| Entre 30.0 e 34.9     | Obesidade Grau I           |
| Entre 35.0 e 39.9     | Obesidade Grau II          |
| 40.0 ou mais          | Obesidade Grau III (mórbida) |

---

## 💡 Exemplos de uso
```less
Digite seu peso em KG: 90
Digite seu peso em KG: 70
Digite sua altura em metros: 1.75
Calculando seu IMC...

Seu IMC é: 22.86
Classificação: Peso normal
```

---

## 🚀 Como executar

1. Clone o repositório:
```code
git clone https://github.com/daniellisboag/calculadora_imc.git
```

2. Entre na pasta:
``` bash
cd calculadora-imc
```

3. Execute o script:
```bash
python imc.py
```

---
