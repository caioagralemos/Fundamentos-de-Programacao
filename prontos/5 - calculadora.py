# calculadora python com funções básicas

op = input('\n1 para soma\n2 para subtração\n3 para multiplicação\n4 para divisão\ndigite o número da operação: ')
x = int(input('primeiro número: '))
y = int(input('segundo número: '))

def soma(x,y):
    print(x+y)

def subtracao(x,y):
    print(x-y)

def multiplicacao(x,y):
    print(x*y)

def divisao(x,y):
    print(x/y)

if op == '1':
    soma(x,y)
elif op == '2':
    subtracao(x,y)
elif op == '3':
    multiplicacao(x,y)
elif op == '4':
    divisao(x,y)
else:
    print('Algo deu errado!')