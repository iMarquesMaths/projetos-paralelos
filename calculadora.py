cores = {'cinza': '\033[37m',
         'vermelho': '\033[31m',
         'negrito': '\033[1m',
         'reset': '\033[m'}


def linha_extra():
    print('{}-{}'.format(cores['cinza'], cores['reset']) * 40)


def cabecalho():
    titulo = 'CALCULADORA DIGITAL'
    linha_extra()
    print(titulo.center(40))
    linha_extra()
    print('')


def calculadora():
    primeiro_valor = input('Digite o primeiro numero: ')
    while not is_float_or_int(primeiro_valor):
        print('"{}" não é um numero, tente novamente '.format(primeiro_valor))
        primeiro_valor = input('Digite o primeiro numero: ')

    segundo_valor = input('Digite o segundo numero: ')
    while not is_float_or_int(segundo_valor):
        print('"{}" não é um numero, tente novamente'.format(segundo_valor))
        segundo_valor = input('Digite o segundo numero: ')

    primeiro_valor = float(primeiro_valor)
    segundo_valor = float(segundo_valor)

    operacao = str(input('''Escolha a operação desejada:
    [+] somar
    [-] subtrair
    [*] multiplicar
    [/] dividir
Por favor, digite a operação: '''))

    while operacao not in '+-*/':
        print('"{}" não é um operador valido, tente novamente: '.format(operacao))
        operacao = str(input('''Escolha a operação desejada:
    [+] somar
    [-] subtrair
    [*] multiplicar
    [/] dividir
Por favor, digite a operação: '''))

    def somar():
        soma = primeiro_valor + segundo_valor
        print('Resultado: {} + {} = {}'.format(primeiro_valor, segundo_valor, soma))

    def subtrair():
        subtracao = primeiro_valor - segundo_valor
        print('Resultado: {} - {} = {}'.format(primeiro_valor, segundo_valor, subtracao))

    def multiplicar():
        multiplicacao = primeiro_valor * segundo_valor
        print('Resultado: {} * {} = {}'.format(primeiro_valor, segundo_valor, multiplicacao))

    def dividir():
        if segundo_valor == 0:
            divisao = primeiro_valor
        else:
            divisao = primeiro_valor / segundo_valor
        print('Resultado: {} / {} = {}'.format(primeiro_valor, segundo_valor, divisao))

    if operacao == '+':
        somar()
        linha_extra()

    elif operacao == '-':
        subtrair()
        linha_extra()

    elif operacao == '*':
        multiplicar()
        linha_extra()

    elif operacao == '/':
        dividir()
        linha_extra()

    else:
        print('Algo de errado não deu certo :/ ')
        print('Reinicie o programa')

    repetir()


def repetir():
    repetir_calculadora = input('Deseja fazer outro calculo? [S/N] ').strip().upper()
    while repetir_calculadora not in 'SN':
        repetir_calculadora = input('Não entendi, entre com S ou N: ').strip().upper()
    if repetir_calculadora == 'S':
        linha_extra()
        calculadora()
    elif repetir_calculadora == 'N':
        linha_extra()
        print('Obrigado por usar este programa, volte sempre!')
        print('Programa encerrado')


def is_float_or_int(x):
    try:
        float(x) or int(x)
        return True
    except:
        return False

cabecalho()
calculadora()
