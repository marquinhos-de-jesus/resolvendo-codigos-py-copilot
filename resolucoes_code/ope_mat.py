# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operacao = input('Digite a operação que deseja realizar (+, -, *, /) ')

if operacao == '+':
    print(f'A soma entre {num1} e {num2} será {num1 + num2}')
elif operacao == '-':
    print(f'A subtração entre {num1} e {num2} será {abs(num1 - num2)}')
elif operacao == '*':
    print(f'A multiplicação entre {num1} e {num2} será {num1 * num2}')
elif operacao == '/':
    print(f'A divisão entre {num1} e {num2} será {num1 / num2}')
else:
    print('Operação Invalida.')